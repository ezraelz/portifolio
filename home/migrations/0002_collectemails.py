# Generated by Django 5.1.3 on 2024-11-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
        ),
    ]