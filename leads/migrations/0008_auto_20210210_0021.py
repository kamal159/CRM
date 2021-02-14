# Generated by Django 3.1.5 on 2021-02-09 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20210206_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
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
        migrations.AlterField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]