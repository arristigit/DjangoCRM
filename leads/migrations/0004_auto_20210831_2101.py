# Generated by Django 3.2.6 on 2021-08-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_alter_agent_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=True),
        ),
    ]