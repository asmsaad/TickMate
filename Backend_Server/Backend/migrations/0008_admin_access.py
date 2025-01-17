# Generated by Django 4.2.6 on 2024-11-20 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_rename_access_priority_admin_access_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('access_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Backend.access_level')),
                ('department', models.ManyToManyField(blank=True, to='Backend.departments')),
                ('domain', models.ManyToManyField(blank=True, to='Backend.domains')),
                ('location', models.ManyToManyField(blank=True, to='Backend.locations')),
                ('service', models.ManyToManyField(blank=True, to='Backend.services')),
                ('sub_domain', models.ManyToManyField(blank=True, to='Backend.sub_domains')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Backend.user_info')),
            ],
        ),
    ]
