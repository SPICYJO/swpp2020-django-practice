# Generated by Django 3.1.2 on 2020-10-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(blank=True, default=25, null=True),
        ),
    ]
