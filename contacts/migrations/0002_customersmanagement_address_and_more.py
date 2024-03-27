# Generated by Django 4.2.10 on 2024-03-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersmanagement',
            name='address',
            field=models.CharField(max_length=17, null=True, verbose_name='Adress'),
        ),
        migrations.AddField(
            model_name='customersmanagement',
            name='campaing',
            field=models.CharField(default='Null', max_length=20, verbose_name='Campaing'),
        ),
        migrations.AddField(
            model_name='customersmanagement',
            name='interaction',
            field=models.FileField(max_length=20, null=True, upload_to='', verbose_name='Interaction'),
        ),
        migrations.AddField(
            model_name='customersmanagement',
            name='notes',
            field=models.TextField(max_length=100, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='customersmanagement',
            name='position',
            field=models.CharField(max_length=20, null=True, verbose_name='Position'),
        ),
        migrations.AddField(
            model_name='customersmanagement',
            name='preference',
            field=models.CharField(max_length=17, null=True, verbose_name='Interaction'),
        ),
    ]
