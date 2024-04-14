# Generated by Django 5.0.3 on 2024-04-14 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('model3D', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model3d',
            name='product_fk_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='category.category'),
        ),
        migrations.AddField(
            model_name='model3d',
            name='product_fk_tags',
            field=models.ManyToManyField(to='tag.tag'),
        ),
    ]
