# Generated by Django 4.2.2 on 2023-06-23 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0017_rename_file_question_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='uploaded_files',
            new_name='upload_files',
        ),
    ]