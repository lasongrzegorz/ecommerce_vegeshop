from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import datetime as dt
import random


def generate_order_id():
	date_str = f"{dt.date.today().strftime('%Y%m%d')}_{dt.datetime.now().strftime('%H%M%S')}"
	rand_str = str(random.randint(1, 100))
	return f'{date_str}_{rand_str}'


def send_mail_confirmation(html_template, context):

	subject = 'html django subject here'
	sent_from = 'grelas@wp.pl'
	recipient = ['grelas@wp.pl']
	html_content = get_template(html_template).render(context=context)
	text_content = 'This is an important message.'
	msg = EmailMultiAlternatives(subject, text_content, sent_from, recipient)
	msg.attach_alternative(html_content, 'text/html')
	msg.send(fail_silently=False)
