# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_countries.fields
import feincms.translations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Event category',
                'verbose_name_plural': 'Event categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('short_description', models.TextField(verbose_name='Short Description', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('start_time', models.DateTimeField(help_text='Start Datum und Zeit', verbose_name='Start time')),
                ('end_time', models.DateTimeField(help_text='leave blank for full day events', null=True, verbose_name='End time', blank=True)),
                ('privacy', models.CharField(max_length=10, verbose_name='Privacy', choices=[(b'OPEN', 'open'), (b'CLOSED', 'closed'), (b'SECRET', 'private')])),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('language', models.CharField(max_length=5, verbose_name='Language', choices=[(b'cs', b'CS')])),
                ('categories', models.ManyToManyField(related_name='agenda_event_related', to='agenda.Category', blank=True)),
                ('owner', models.ForeignKey(related_name='owns_agenda_event', verbose_name='Owner', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('picture', models.ForeignKey(related_name='agenda_event_events', blank=True, to='media.Image', null=True)),
            ],
            options={
                'ordering': ['start_time'],
                'abstract': False,
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', verbose_name='language', max_length=10, editable=False, choices=[(b'cs', b'CS')])),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('short_description', models.TextField(verbose_name='Short Description', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('parent', models.ForeignKey(related_name='translations', to='agenda.Event')),
            ],
            options={
                'verbose_name': 'Event Translation',
                'verbose_name_plural': 'Event Translations',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Location')),
                ('street', models.CharField(max_length=255, verbose_name='Street', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name='City', blank=True)),
                ('state', models.CharField(max_length=30, verbose_name='State', blank=True)),
                ('zip', models.CharField(max_length=10, verbose_name='Zip', blank=True)),
                ('country', django_countries.fields.CountryField(default=b'CH', max_length=2, blank=True, null=True, verbose_name='Country')),
                ('latitude', models.DecimalField(null=True, verbose_name='Latitude', max_digits=12, decimal_places=9, blank=True)),
                ('longitude', models.DecimalField(null=True, verbose_name='Longitude', max_digits=12, decimal_places=9, blank=True)),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='agenda.Venue'),
        ),
    ]
