# Generated by Django 5.1.1 on 2024-11-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'täzelik', 'verbose_name_plural': 'täzelikler'},
        ),
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(default='d', upload_to='news/', verbose_name='Surat'),
            preserve_default=False,
        ),
    ]