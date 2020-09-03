# Generated by Django 3.0.3 on 2020-08-30 22:37

from django.db import migrations, models
import fordisapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('fordisapp', '0004_auto_20200828_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportMsg', models.TextField(max_length=50, null=True, verbose_name='신고메세지')),
                ('reportPhoto', models.FileField(blank=True, null=True, upload_to=fordisapp.models.date_upload_to)),
                ('reportDate', models.DateField(auto_now_add=True, verbose_name='신고시간')),
            ],
        ),
    ]