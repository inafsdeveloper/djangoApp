# Generated by Django 4.2.11 on 2024-04-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('overview', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
    ]
