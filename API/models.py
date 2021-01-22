from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.message}"
