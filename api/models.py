from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    text = models.TextField(default='')
    src = models.TextField(default='')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__() + ' note'


class Image(models.Model):
    src = models.CharField(max_length=128, default='')
    note = models.ForeignKey(Note, related_name='images', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.src.__str__() + ' ' + self.note.__str__()


class UserCategory(models.Model):
    name = models.CharField(max_length=128, default='')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
