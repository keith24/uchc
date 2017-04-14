# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170225_0854'),
    ]

    operations = [
#        migrations.CreateModel(
#            name='HomePage',
#            fields=[
#                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
#                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
#                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
#                ('content_de', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
#                ('content_ru', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
#                ('content_fr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
#            ],
#            options={
#                'ordering': ('_order',),
#                'verbose_name': 'Homepage',
#                'verbose_name_plural': 'Homepages',
#            },
#            bases=('pages.page', models.Model),
#        ),
    ]
