# Generated by Django 5.2.3 on 2025-07-01 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlaggedComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('flag_reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('original_comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='flag_record', to='api.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
