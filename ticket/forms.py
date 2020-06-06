from django import forms
from django.forms import ModelForm
from ticket.models import Ticket, Answer


class OpenTicketForm(ModelForm):
    CHOICES_PRIORITY = (
        ('0', 'Baixa'),
        ('1', 'Média'),
        ('2', 'Alta'),
    )

    CHOICES_SUBJECT = (
        ('maintenance', 'Manutenção'),
        ('account', 'Conta'),
        ('payment', 'Pagamento'),
    )

    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Insira um título',
    }))
    subject = forms.ChoiceField(label='Assunto', choices=CHOICES_SUBJECT, widget=forms.Select(attrs={
        'class': 'form-control',
    }), initial='initial')
    priority = forms.ChoiceField(label='Prioridade', choices=CHOICES_PRIORITY, widget=forms.Select(attrs={
        'class': 'form-control',
    }), initial='initial')
    body = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={
        'rows': '5',
        'class': 'form-control',
        'placeholder': 'Insira a mensagem do ticket',
    }))

    class Meta:
        model = Ticket
        fields = ['title', 'subject', 'priority', 'body']


class AnswerTicketForm(ModelForm):
    answer_text = forms.CharField(required=False, label='Resposta', widget=forms.Textarea(attrs={
        'rows': '5',
        'class': 'form-control',
        'placeholder': 'Insira a mensagem da resposta do ticket',
    }))

    close = forms.BooleanField(required=False, label='Fechar este ticket', widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))

    class Meta:
        model = Answer
        fields = ['answer_text']
