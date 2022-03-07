from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        nome = request.POST['message-name']
        email = request.POST['message-email']
        message = request.POST['message']

        titulo = 'Confirmação de agendamento'
        mensagem = '''
                    Olá! Tudo bem?
    
                    Muito obrigada por se agendar .
    
                    Em até 48 horas úteis, a nossa equipe entrará
                    em contato com vocie para concluirmos a sua
                    matrícula.
    
                    Atenciosamente,
                    --
                    Morena'''
        send_mail(
            titulo,
            mensagem,
            settings.EMAIL_HOST_USER,
            [email], fail_silently=False
        )

        return render(request, 'contact.html', {'message_name': nome})
    else:
        return render(request, 'contact.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})

def appointment(request):
    if request.method == 'POST':
        nome = request.POST['your-name']
        email = request.POST['your-email']
        phone = request.POST['your-phone']
        adress = request.POST['your-address']
        schedule = request.POST['your-schedule']
        date = request.POST['your-date']
        message = request.POST['your-message']

        return render(request, 'appointment.html', {
            'your_name': nome,
            'your_email': email,
            'your_phone': phone,
            'your_address': adress,
            'your_schedule': schedule,
            'your_date': date,
            'your_message': message
        })

        titulo = 'Confirmação de agendamento'
        mensagem = '''
                        Olá! Tudo bem?

                        Muito obrigada por se agendar .

                        Em até 48 horas úteis, a nossa equipe entrará
                        em contato com vocie para concluirmos a sua
                        matrícula.

                        Atenciosamente,
                        --
                        Morena'''
        send_mail(
            titulo,
            mensagem,
            settings.EMAIL_HOST_USER,
            [email], fail_silently=False
        )
    else:
        return render(request, 'home.html', {})
