# Generated by Django 2.2.27 on 2022-04-23 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_auto_20220423_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
