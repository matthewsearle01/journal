# Generated by Django 4.0.3 on 2022-03-08 14:53

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='description',
            new_name='link',
        ),
        migrations.AddField(
            model_name='journal',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
