# Generated by Django 2.1.5 on 2019-01-29 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Tag', verbose_name='Etiket'),
        ),
    ]
