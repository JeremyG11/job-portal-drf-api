from django.db import models
from account.models import CustomUser as User


class Events(models.Model):
    posted_by = models.ForeignKey(
        User, related_name="Events", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateTimeField()
    object = models.Manager()

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title
