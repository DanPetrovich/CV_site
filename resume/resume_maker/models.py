from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

import datetime


class CVInfo(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=11)  # TODO наверное, можно сделать лучше
    email = models.EmailField()
    work_experience = models.TextField(default='')
    skills = models.TextField()

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.name})

    class Meta:
        verbose_name_plural = 'CV'
        ordering = ['birth_date']
