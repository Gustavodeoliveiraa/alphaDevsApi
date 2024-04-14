# Generated by Django 5.0.3 on 2024-03-31 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model3D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_image', models.ImageField(upload_to='model3d/')),
                ('product_description', models.TextField()),
                ('product_release_date', models.DateTimeField(auto_now_add=True)),
                ('product_price', models.FloatField()),
                ('product_height', models.FloatField()),
                ('product_width', models.FloatField()),
            ],
        ),
    ]
