# Generated by Django 3.2.6 on 2021-08-30 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210830_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(default='crm@gmail.com', on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
