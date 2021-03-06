# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 13:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnsibleOperLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_ip', models.GenericIPAddressField(verbose_name='操作者IP')),
                ('module', models.CharField(max_length=128, verbose_name='模块')),
                ('args', models.CharField(blank=True, max_length=256, null=True, verbose_name='模块参数')),
                ('server', models.TextField(verbose_name='服务器')),
                ('result', models.TextField(verbose_name='执行结果')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='操作时间')),
            ],
            options={
                'verbose_name': '模块执行记录',
                'verbose_name_plural': '模块执行记录',
                'db_table': 'modulelog',
            },
        ),
        migrations.CreateModel(
            name='AnsibleRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='role名称')),
                ('file', models.FileField(upload_to='roles/')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加日期')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': 'AnsibleRole信息表',
                'verbose_name_plural': 'AnsibleRole信息表',
                'db_table': 'ansiblerole',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=32, unique=True, verbose_name='组名')),
                ('vars', models.TextField(blank=True, null=True, verbose_name='变量')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '动态主机表',
                'verbose_name_plural': '动态主机表',
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='PlayBookLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_ip', models.GenericIPAddressField(verbose_name='操作者IP')),
                ('name', models.CharField(max_length=64, verbose_name='剧本名称')),
                ('result', models.TextField(verbose_name='执行结果')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='执行时间')),
            ],
            options={
                'verbose_name': '剧本执行日志',
                'verbose_name_plural': '剧本执行日志',
                'db_table': 'playbooklogs',
            },
        ),
        migrations.CreateModel(
            name='PlayBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('file', models.FileField(upload_to='playbook/%Y/%m/%d/')),
                ('content', models.TextField(verbose_name='内容')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '剧本信息',
                'verbose_name_plural': '剧本信息',
                'db_table': 'playbooks',
            },
        ),
    ]
