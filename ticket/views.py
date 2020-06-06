from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ticket.forms import OpenTicketForm, AnswerTicketForm
from ticket.models import Ticket, Answer


@login_required
def index(request):
    form = OpenTicketForm(request.POST or None)
    tickets = Ticket.objects.filter(user_id=request.user.id).all()
    context = {
        'form': form,
        'tickets': tickets,
    }
    return render(request, 'ticket/index/index.html', context)


@login_required
def show(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    answer = Answer.objects.filter(ticket_id=ticket.id).all()
    user = User.objects.get(id=ticket.user_id)
    if ticket.user_id != request.user.id and not request.user.is_staff:
        return render(request, 'ticket/errors/404.html')
    form = AnswerTicketForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Close ticket if checkbox is checked
            if request.POST.get('close') == 'on':
                ticket.status = 2
                ticket.save()
                return JsonResponse({
                    'status': True,
                    'message': 'O ticket foi encerrado',
                })
            answerf = form.save(commit=False)
            answerf.answered_by_id = request.user.id
            answerf.ticket_id = id
            ticket.status = 0
            # If who is responding is not the owner ticket
            if answerf.answered_by_id != ticket.user_id:
                if request.POST.get('close') == 'on':
                    ticket.status = 2
                else:
                    ticket.status = 1
            ticket.save()
            # If input answer_text is not empty
            if request.POST.get('answer_text'):
                answerf.save()
                return JsonResponse({
                    'status': True,
                    'message': 'A resposta foi adicionada',
                })
        else:
            return JsonResponse({
                'status': False,
                'message': form.errors.as_json(),
            })
    context = {
        'ticket': ticket,
        'answer': answer,
        'user': user,
        'form': form,
    }
    return render(request, 'ticket/show/show.html', context)


@login_required
def create(request):
    form = OpenTicketForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user_id = request.user.id
            ticket.save()
            return JsonResponse({
                'status': True,
                'message': 'Seu ticket foi criado e está em aberto',
            })
        else:
            return JsonResponse({
                'status': False,
                'message': form.errors.as_json(),
            })
    else:
        return redirect('ticket:index')


@login_required
def panel_index(request):
    tickets = Ticket.objects.filter(status=0).all()
    context = {'tickets': tickets}
    return render(request, 'ticket/panel/index.html', context)
