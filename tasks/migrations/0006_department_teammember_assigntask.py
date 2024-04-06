# Generated by Django 4.2.11 on 2024-04-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_tasksmanagement_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Departamento')),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'TeamMembers',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='AssignTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='task title')),
                ('description', models.TextField(max_length=200, verbose_name='description')),
                ('priority', models.CharField(choices=[('Normal', 'N'), ('Mediana', 'M'), ('Alta', 'A')], default='Normal', max_length=10)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
                ('due_date', models.DateField(null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='date')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.department')),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.teammember')),
            ],
            options={
                'verbose_name_plural': 'AssignTasks',
                'ordering': ['-title'],
            },
        ),
    ]