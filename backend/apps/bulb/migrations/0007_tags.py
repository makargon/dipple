# Generated by Django 4.2 on 2023-04-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulb', '0006_alter_comments_options_news_action_click_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
    ]
