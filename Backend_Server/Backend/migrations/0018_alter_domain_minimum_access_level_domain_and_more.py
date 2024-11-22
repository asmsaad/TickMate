# Generated by Django 4.2.6 on 2024-11-21 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0017_domain_minimum_access_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain_minimum_access_level',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Backend.domains'),
        ),
        migrations.CreateModel(
            name='request_view_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Backend.all_requests')),
                ('viewed_by', models.ManyToManyField(blank=True, to='Backend.user_info')),
            ],
        ),
    ]