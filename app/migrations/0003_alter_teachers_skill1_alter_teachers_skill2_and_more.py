# Generated by Django 5.1.2 on 2024-10-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_courses_core'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='skill1',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('csharp', 'C#'), ('cpp', 'C++'), ('go', 'Go'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('typescript', 'TypeScript'), ('rust', 'Rust'), ('scala', 'Scala'), ('perl', 'Perl'), ('web', 'توسعه وب'), ('mobile', 'توسعه موبایل'), ('data', 'علم داده'), ('ml', 'یادگیری ماشین'), ('game', 'توسعه بازی'), ('embedded', 'سیستم\u200cهای تعبیه\u200cشده'), ('cyber', 'امنیت سایبری'), ('cloud', 'رایانش ابری'), ('iot', 'اینترنت اشیاء'), ('devops', 'دواپس')], max_length=150),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='skill2',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('csharp', 'C#'), ('cpp', 'C++'), ('go', 'Go'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('typescript', 'TypeScript'), ('rust', 'Rust'), ('scala', 'Scala'), ('perl', 'Perl'), ('web', 'توسعه وب'), ('mobile', 'توسعه موبایل'), ('data', 'علم داده'), ('ml', 'یادگیری ماشین'), ('game', 'توسعه بازی'), ('embedded', 'سیستم\u200cهای تعبیه\u200cشده'), ('cyber', 'امنیت سایبری'), ('cloud', 'رایانش ابری'), ('iot', 'اینترنت اشیاء'), ('devops', 'دواپس')], max_length=150),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='skill3',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('csharp', 'C#'), ('cpp', 'C++'), ('go', 'Go'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('typescript', 'TypeScript'), ('rust', 'Rust'), ('scala', 'Scala'), ('perl', 'Perl'), ('web', 'توسعه وب'), ('mobile', 'توسعه موبایل'), ('data', 'علم داده'), ('ml', 'یادگیری ماشین'), ('game', 'توسعه بازی'), ('embedded', 'سیستم\u200cهای تعبیه\u200cشده'), ('cyber', 'امنیت سایبری'), ('cloud', 'رایانش ابری'), ('iot', 'اینترنت اشیاء'), ('devops', 'دواپس')], max_length=150),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='skill4',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('csharp', 'C#'), ('cpp', 'C++'), ('go', 'Go'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('typescript', 'TypeScript'), ('rust', 'Rust'), ('scala', 'Scala'), ('perl', 'Perl'), ('web', 'توسعه وب'), ('mobile', 'توسعه موبایل'), ('data', 'علم داده'), ('ml', 'یادگیری ماشین'), ('game', 'توسعه بازی'), ('embedded', 'سیستم\u200cهای تعبیه\u200cشده'), ('cyber', 'امنیت سایبری'), ('cloud', 'رایانش ابری'), ('iot', 'اینترنت اشیاء'), ('devops', 'دواپس')], max_length=150),
        ),
    ]