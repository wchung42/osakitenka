# Generated by Django 2.2 on 2019-05-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_userprofiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='credit_card_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]