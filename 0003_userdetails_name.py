# Generated by Django 3.2.7 on 2022-03-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220330_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='name',
            field=models.CharField(default='Abhijeet', max_length=200),
            preserve_default=False,
        ),
    ]