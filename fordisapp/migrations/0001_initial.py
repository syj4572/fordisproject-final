# Generated by Django 3.0.3 on 2020-08-26 03:39

from django.db import migrations, models
import fordisapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userEmail', models.EmailField(max_length=30, primary_key=True, serialize=False, verbose_name='이메일(아이디)')),
                ('nickName', models.CharField(max_length=12, verbose_name='닉네임')),
                ('password', models.CharField(max_length=12, verbose_name='비밀번호')),
                ('registerDate', models.DateField(auto_now_add=True, verbose_name='가입시간')),
                ('guardianName', models.CharField(blank=True, max_length=12, verbose_name='보호자명')),
                ('guardianCallNum', models.CharField(blank=True, max_length=12, verbose_name='보호자전화번호')),
                ('guardianBasicMsg', models.CharField(blank=True, max_length=100, verbose_name='보호자기본메세지')),
                ('photo', models.FileField(blank=True, upload_to=fordisapp.models.date_upload_to)),
            ],
        ),
    ]
