# Generated by Django 3.1.4 on 2022-06-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('slug', models.SlugField(max_length=144, unique=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]