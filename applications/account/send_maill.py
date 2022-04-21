from django.core.mail import send_mail


def send_confirmation_email(code,email):
    full_link = f'http://localhost:7500/account/activate/{code}'

    send_mail(
        'привет',# title
        full_link, #body
        'bagdadzhunushov@gmail.com', #from email
        [email],
    )