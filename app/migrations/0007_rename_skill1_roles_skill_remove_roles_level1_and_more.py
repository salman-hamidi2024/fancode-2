# Generated by Django 5.1.2 on 2024-11-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_teachers_level1_remove_teachers_level2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roles',
            old_name='skill1',
            new_name='skill',
        ),
        migrations.RemoveField(
            model_name='roles',
            name='level1',
        ),
        migrations.AddField(
            model_name='roles',
            name='level',
            field=models.CharField(blank=True, choices=[('20', 'مبتدی'), ('40', 'متوسط'), ('60', 'پیشرفته'), ('80', 'حرفه\u200cای'), ('100', 'استاد')], max_length=150),
        ),
    ]
