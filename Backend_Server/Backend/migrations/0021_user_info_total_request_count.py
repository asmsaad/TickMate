# Generated by Django 4.2.6 on 2024-11-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0020_alter_all_requests_comment_alter_all_requests_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='total_request_count',
            field=models.IntegerField(default=0),
        ),
    ]