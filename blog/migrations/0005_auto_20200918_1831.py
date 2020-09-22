# Generated by Django 3.1.1 on 2020-09-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_descforcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('A', 'ai'), ('H', 'cs')], default='A', max_length=1),
        ),
    ]