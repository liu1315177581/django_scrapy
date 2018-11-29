# Generated by Django 2.1.1 on 2018-10-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vedio', '0006_type_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='text_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='text_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='date_birth',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='date_birth',
            field=models.CharField(max_length=255, null=True),
        ),
    ]