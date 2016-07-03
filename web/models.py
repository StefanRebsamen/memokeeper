from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Label(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Label {}".format(self.name)


@python_2_unicode_compatible
class Memo(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    labels = models.ManyToManyField(Label)
    def __str__(self):
        return "Memo title: {}, labels: {}".format(self.title, ", ".join(s.name for s in self.labels.all() ))


@python_2_unicode_compatible
class Attachement(models.Model):
    name = models.CharField(max_length=50)
    #content = models.FileField()
    memo = models.ForeignKey(Memo)

    def __str__(self):
        return "Attachement {}".format(self.name)
