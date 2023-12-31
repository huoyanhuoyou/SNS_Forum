# Generated by Django 4.2.5 on 2023-10-20 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="创建时间"
                    ),
                ),
                ("message", models.TextField(null=True, verbose_name="消息")),
                ("unread", models.BooleanField(default=True, verbose_name="是否未读")),
                (
                    "recipient",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receive_messages",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="接收者",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="send_messages",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="发送者",
                    ),
                ),
            ],
        ),
    ]
