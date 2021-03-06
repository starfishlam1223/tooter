# Generated by Django 2.2 on 2020-06-25 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toots', '0003_toot_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='toot',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TootLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('toot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toots.Toot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='toot',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_user', through='toots.TootLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
