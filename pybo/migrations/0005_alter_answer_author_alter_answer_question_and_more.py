# Generated by Django 4.2.1 on 2023-06-14 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0004_answer_modify_date_question_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pybo.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
