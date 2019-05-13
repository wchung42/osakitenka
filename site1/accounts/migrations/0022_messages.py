# Generated by Django 2.2 on 2019-05-12 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0021_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='send_mes', to=settings.AUTH_USER_MODEL)),
                ('friend_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receive_mes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
