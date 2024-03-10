from django.core.mail import send_mail

def acceptance_mail(request, object):
    subject = f"Hello {object.applicant.name}!, Your appliction for {object.job.name} has been accepted"
    message = f"Please contact job hiring persons for more imformations on your acceptance"
    send_mail(subject, message,  fail_silently=False)