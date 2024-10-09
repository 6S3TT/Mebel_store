# Generated by Django 5.1 on 2024-08-31 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='height',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='products',
            name='length',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='products',
            name='main_foto',
            field=models.ImageField(blank=True, null=True, upload_to='main_product_images'),
        ),
        migrations.AddField(
            model_name='products',
            name='width',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='products.products')),
            ],
        ),
    ]
