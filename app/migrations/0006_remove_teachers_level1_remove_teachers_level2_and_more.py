# Generated by Django 5.1.2 on 2024-10-31 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_teachers_level3_teachers_level4_teachers_skill2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='level1',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='level2',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='level3',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='level4',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='skill1',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='skill3',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='skill4',
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(blank=True, choices=[('python', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('csharp', 'C#'), ('cpp', 'C++'), ('go', 'Go'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('typescript', 'TypeScript'), ('rust', 'Rust'), ('scala', 'Scala'), ('perl', 'Perl'), ('web', 'توسعه وب'), ('mobile', 'توسعه موبایل'), ('data', 'علم داده'), ('ml', 'یادگیری ماشین'), ('game', 'توسعه بازی'), ('embedded', 'سیستم\u200cهای تعبیه\u200cشده'), ('cyber', 'امنیت سایبری'), ('cloud', 'رایانش ابری'), ('iot', 'اینترنت اشیاء'), ('devops', 'دواپس')], max_length=150)),
                ('level1', models.CharField(blank=True, choices=[('low', 'مبتدی'), ('beginner', 'متوسط'), ('advanced', 'پیشرفته'), ('expert', 'حرفه\u200cای'), ('master', 'استاد')], max_length=150)),
                ('connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teachers')),
            ],
        ),
    ]
