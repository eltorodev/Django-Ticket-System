$(document).ready(function () {
    $('#user_register').submit(function (e) {
        e.preventDefault()

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/accounts/register/',
            data: $('#user_register').serialize(),
            success: function (response) {
                if (response.status) {
                    $('#message').removeClass('alert alert-danger').addClass('alert alert-success').html(response.message)
                    $('.form-group').hide('slow')
                    $('#user_register button[name=submit]').prop({ disabled: true }).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>')
                    setTimeout(function () {
                        location.href = '/accounts/login/'
                    }, 2000)
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

    $('#user_login').submit(function (e) {
        e.preventDefault()

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/accounts/login/',
            data: $('#user_login').serialize(),
            success: function (response) {
                if (response.status) {
                    $('#message').removeClass('alert alert-danger').addClass('alert alert-success').html(response.message)
                    $('.form-group').hide('slow')
                    $('#user_login button[name=submit]').prop({ disabled: true }).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>')
                    setTimeout(function () {
                        location.reload()
                    }, 2000)
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
        return false;
    }
    return true;
}