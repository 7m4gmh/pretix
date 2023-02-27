# Generated by Django 3.2.16 on 2023-02-01 10:58

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0233_ignore_from_quota_while_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='scheduledeventexport',
            name='export_form_data',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='scheduledorganizerexport',
            name='export_form_data',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterIndexTogether(
            name='logentry',
            index_together={('datetime', 'id')},
        ),
        migrations.AlterIndexTogether(
            name='order',
            index_together={('datetime', 'id'), ('last_modified', 'id')},
        ),
        migrations.AlterIndexTogether(
            name='transaction',
            index_together={('datetime', 'id')},
        ),
    ]