# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170225_0854'),
    ]

    operations = [
#        migrations.CreateModel(
#            name='Club',
#            fields=[
#                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
#                ('founded', models.DateField()),
#                ('city', models.CharField(default=b'', max_length=50)),
#                ('city_en', models.CharField(default=b'', max_length=50, null=True)),
#                ('city_de', models.CharField(default=b'', max_length=50, null=True)),
#                ('city_ru', models.CharField(default=b'', max_length=50, null=True)),
#                ('city_fr', models.CharField(default=b'', max_length=50, null=True)),
#                ('country', django_countries.fields.CountryField(max_length=2)),
#                ('website', models.URLField(default=b'')),
#                ('blurb', models.TextField(default=b'')),
#                ('blurb_en', models.TextField(default=b'', null=True)),
#                ('blurb_de', models.TextField(default=b'', null=True)),
#                ('blurb_ru', models.TextField(default=b'', null=True)),
#                ('blurb_fr', models.TextField(default=b'', null=True)),
#                ('img1', models.ImageField(default=b'', upload_to=b'')),
#                ('img2', models.ImageField(default=b'', upload_to=b'')),
#                ('img3', models.ImageField(default=b'', upload_to=b'')),
#                ('img4', models.ImageField(default=b'', upload_to=b'')),
#                ('img5', models.ImageField(default=b'', upload_to=b'')),
#            ],
#            options={
#                'ordering': ['founded'],
#                'verbose_name': 'Club',
#                'verbose_name_plural': 'Clubs',
#            },
#            bases=('pages.page',),
#        ),
#        migrations.CreateModel(
#            name='ClubIndex',
#            fields=[
#                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
#            ],
#            options={
#                'ordering': ('_order',),
#                'verbose_name': 'Clubs Index',
#                'verbose_name_plural': 'Clubs Indicies',
#            },
#            bases=('pages.page',),
#        ),
    ]
