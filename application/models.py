

from django.db import models

# Create your models here.


class Application(models.Model):
    applicant = models.ForeignKey('account.CustomUser',related_name='applications', on_delete=models.CASCADE, null=False)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, null=False)
    resume = models.FileField(upload_to='resumes/applications', default='resume.docx')
    is_accepted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    acceptance_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.applicant}'s application"