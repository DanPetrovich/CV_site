from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class CVInfo(models.Model):  # TODO мб надо будет добавить в settings https://youtu.be/k1wZKx6nMjg
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=20)
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    birth_date = models.DateField()
    phone_number = models.TextField()  # TODO наверное, можно сделать лучше
    email = models.EmailField()
    skills = models.TextField()

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.name})

    class Meta:
        verbose_name_plural = 'CV'
        ordering = ['birth_date']
