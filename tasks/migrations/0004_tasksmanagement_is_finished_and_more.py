# Generated by Django 4.2.10 on 2024-03-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasksmanagement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksmanagement',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasksmanagement',
            name='description',
            field=models.TextField(max_length=200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='tasksmanagement',
            name='priority',
            field=models.CharField(choices=[('NORMAL', 'N'), ('MEDIANA', 'M'), ('ALTA', 'A')], default='NORMAL', max_length=10),
        ),
        migrations.AlterField(
            model_name='tasksmanagement',
            name='title',
            field=models.CharField(max_length=50, verbose_name='task title'),
        ),
    ]