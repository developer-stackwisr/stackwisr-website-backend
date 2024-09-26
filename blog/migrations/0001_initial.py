# Generated by Django 5.0.8 on 2024-09-26 10:35

import blog.validators
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/', validators=[blog.validators.validate_image])),
                ('slug', models.SlugField(blank=True, max_length=160, unique=True)),
                ('author', models.CharField(help_text="Author's name", max_length=50)),
                ('title', models.CharField(max_length=250)),
                ('body', ckeditor.fields.RichTextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
