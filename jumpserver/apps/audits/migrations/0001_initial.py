# Generated by Django 2.1 on 2018-10-16 06:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20181016_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='FTPLog',
            fields=[
                ('org_id', models.CharField(blank=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('remote_addr', models.CharField(blank=True, max_length=15, null=True, verbose_name='Remote addr')),
                ('asset', models.CharField(max_length=1024, verbose_name='Asset')),
                ('system_user', models.CharField(max_length=128, verbose_name='System user')),
                ('operate', models.CharField(max_length=16, verbose_name='Operate')),
                ('filename', models.CharField(max_length=1024, verbose_name='Filename')),
                ('is_success', models.BooleanField(default=True, verbose_name='Success')),
                ('date_start', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperateLog',
            fields=[
                ('org_id', models.CharField(blank=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('action', models.CharField(choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')], max_length=16, verbose_name='Action')),
                ('resource_type', models.CharField(max_length=64, verbose_name='Resource Type')),
                ('resource', models.CharField(max_length=128, verbose_name='Resource')),
                ('remote_addr', models.CharField(blank=True, max_length=15, null=True, verbose_name='Remote addr')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PasswordChangeLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('change_by', models.CharField(max_length=128, verbose_name='Change by')),
                ('remote_addr', models.CharField(blank=True, max_length=15, null=True, verbose_name='Remote addr')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('users.loginlog',),
        ),
    ]
