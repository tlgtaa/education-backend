# Generated by Django 2.2.7 on 2019-11-05 22:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_CourseGenitiveName'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('paid', models.DateTimeField('Date when order got paid', null=True, blank=True, help_text='If set during creation, order automaticaly gets shipped')),
                ('shipped', models.DateTimeField('Date when order was shipped', null=True, blank=True)),
                ('course', orders.models.ItemField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.Course')),
                ('record', orders.models.ItemField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.Record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]