# Generated by Django 2.2.14 on 2020-07-31 12:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200731_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2019)])),
            ],
        ),
        migrations.AddField(
            model_name='matches',
            name='year',
            field=models.ForeignKey(default=2019, on_delete=django.db.models.deletion.CASCADE, to='main.MatchYear'),
            preserve_default=False,
        ),
    ]