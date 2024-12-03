# Generated by Django 4.2.6 on 2024-11-29 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0021_user_info_total_request_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification_token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, default='', max_length=10000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Backend.user_info')),
            ],
        ),
    ]
