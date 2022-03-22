# Generated by Django 3.2.10 on 2022-03-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('isbn_number', models.PositiveBigIntegerField(blank=True, null=True, unique=True)),
                ('number_of_pages', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cover_link', models.URLField()),
                ('publication_language', models.CharField(max_length=255)),
            ],
        ),
    ]
