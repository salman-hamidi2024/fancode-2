# Generated by Django 5.1.2 on 2024-11-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_roles_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='level',
            field=models.CharField(choices=[('20', 'مبتدی'), ('40', 'متوسط'), ('60', 'پیشرفته'), ('80', 'حرفه\u200cای'), ('100', 'استاد')], max_length=150),
        ),
        migrations.AlterField(
            model_name='roles',
            name='skill',
            field=models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('C#', 'C#'), ('C++', 'C++'), ('Go', 'Go'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('typescript', 'TypeScript'), ('rust', 'Rust'), ('scala', 'Scala'), ('perl', 'Perl'), ('web', 'توسعه وب'), ('mobile', 'توسعه موبایل'), ('data science', 'علم داده'), ('machin learning', 'یادگیری ماشین'), ('game', 'توسعه بازی'), ('embedded', 'سیستم\u200cهای تعبیه\u200cشده'), ('cyber', 'امنیت سایبری'), ('cloud', 'رایانش ابری'), ('iot', 'اینترنت اشیاء'), ('devops', 'دواپس')], max_length=150),
        ),
    ]