from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_email(order):
    """Send order confirmation email"""
    email_to = order.email_address
    subject = render_to_string(
        'confirmation_email/email-subject.txt', {'order': order})
    content = render_to_string('confirmation_email/email-body.txt', {
                               'order': order, 'email_from': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        content,
        settings.DEFAULT_FROM_EMAIL,
        [email_to]
    )
