from celery import Celery
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Configuração do Celery
celery = Celery('celery_worker', broker=os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0'), backend=os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0'))

# Função para envio de email
@celery.task
def enviar_email_async(destinatario, assunto, mensagem):
    remetente = os.environ.get('EMAIL_SENDER', 'gabriel.oliveira6@estudante.ifms.edu.br')
    senha = os.environ.get('EMAIL_PASSWORD', 'gyqz nmrm erjy fmqb')

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print(f"Email enviado para {destinatario}")
    except Exception as e:
        print(f"Falha ao enviar email: {e}")
