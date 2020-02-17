# Generated by Django 2.1.11 on 2020-02-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboPortal', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='portaluser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portaluser',
            name='user_team_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
