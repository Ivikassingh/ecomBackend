# Generated by Django 3.1.4 on 2020-12-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='linkId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='linkmapper',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]