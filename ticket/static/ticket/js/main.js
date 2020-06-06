$(document).ready(function () {
    $('#new_ticket').submit(function (e) {
        e.preventDefault()

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/ticket/create/',
            data: $('#new_ticket').serialize(),
            success: function (response) {
                if (response.status) {
                    $('#message').removeClass('alert alert-danger').addClass('alert alert-success').html(response.message)
                    $("#reload").load(location.href+" #reload>*","")
                    $('#openTicketModal').modal('toggle')
                    $('#new_ticket')[0].reset()
                } else {
                    if (isJson(response.message)) {
                        $.each(JSON.parse(response.message), function (key, value) {
                            $.each(value, function (key, value) {
                                $('#message').empty()
                                $('#message').removeClass('alert alert-success').addClass('alert alert-danger').append('<div>' + value.message + '</div>')
                            })
                        })
                    } else {
                        $('#message').empty()
                        $('#message').removeClass('alert alert-success').addClass('alert alert-danger').html(response.message)
                    }
                }
            }
        })
    })

    $('#answer_ticket').submit(function (e) {
        e.preventDefault()

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/ticket/show/' + $('input[name=id_ticket]').val() + '/',
            data: $('#answer_ticket').serialize(),
            success: function (response) {
                if (response.status) {
                    $('#message').removeClass('alert alert-danger').addClass('alert alert-success').html(response.message)
                    $('#answer_ticket textarea').empty()
                    $("#reload").load(location.href+" #reload>*","")
                } else {
                    if (isJson(response.message)) {
                        $.each(JSON.parse(response.message), function (key, value) {
                            $.each(value, function (key, value) {
                                $('#message').empty()
                                $('#message').removeClass('alert alert-success').addClass('alert alert-danger').append('<div>' + value.message + '</div>')
                            })
                        })
                    } else {
                        $('#message').empty()
                        $('#message').removeClass('alert alert-success').addClass('alert alert-danger').html(response.message)
                    }
                }
            }
        })
    })
})

function isJson(string) {
    try {
        JSON.parse(string)
    } catch (error) {
        return false
    }
    return true
}