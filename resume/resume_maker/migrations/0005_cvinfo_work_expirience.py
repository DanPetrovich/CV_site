# Generated by Django 3.2.16 on 2022-12-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0004_alter_cvinfo_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvinfo',
            name='work_expirience',
            field=models.TextField(default=''),
        ),
    ]
