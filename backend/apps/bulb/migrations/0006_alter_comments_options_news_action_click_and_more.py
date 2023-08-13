# Generated by Django 4.2 on 2023-04-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulb', '0005_alter_comments_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AddField(
            model_name='news',
            name='action_click',
            field=models.CharField(default='Подробнее', max_length=30),
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]