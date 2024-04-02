# Generated by Django 4.2.10 on 2024-04-02 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0003_alter_customersmanagement_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28, verbose_name='Nombre')),
                ('status', models.CharField(max_length=10, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Brands',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28, verbose_name='Nombre')),
                ('status', models.CharField(max_length=10, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('status', models.CharField(max_length=10, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Stores',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Nombre')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('brands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.store')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(blank=True, max_length=30, null=True, verbose_name='Direccion')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.customersmanagement')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]