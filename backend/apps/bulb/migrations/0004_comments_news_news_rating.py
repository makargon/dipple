# Generated by Django 4.2 on 2023-04-11 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulb', '0003_alter_news_html_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bulb.news'),
        ),
        migrations.AddField(
            model_name='news',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
