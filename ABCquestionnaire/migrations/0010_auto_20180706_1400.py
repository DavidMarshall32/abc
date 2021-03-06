# Generated by Django 2.0 on 2018-07-06 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ABCquestionnaire', '0009_auto_20180705_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(blank=True, max_length=10, verbose_name='StudentNumber')),
                ('choice1', models.CharField(blank=True, max_length=2, verbose_name='V1')),
                ('choice2', models.CharField(blank=True, max_length=2, verbose_name='V2')),
                ('choice3', models.CharField(blank=True, max_length=2, verbose_name='V3')),
                ('choice4', models.CharField(blank=True, max_length=2, verbose_name='V4')),
                ('choice5', models.CharField(blank=True, max_length=2, verbose_name='V5')),
                ('choice6', models.CharField(blank=True, max_length=2, verbose_name='V6')),
                ('choice7', models.CharField(blank=True, max_length=2, verbose_name='V7')),
                ('choice8', models.CharField(blank=True, max_length=2, verbose_name='V8')),
                ('choice9', models.CharField(blank=True, max_length=2, verbose_name='V9')),
                ('choice10', models.CharField(blank=True, max_length=2, verbose_name='V10')),
                ('choice11', models.CharField(blank=True, max_length=2, verbose_name='V11')),
                ('choice12', models.CharField(blank=True, max_length=2, verbose_name='V12')),
                ('choice13', models.CharField(blank=True, max_length=2, verbose_name='V13')),
                ('choice14', models.CharField(blank=True, max_length=2, verbose_name='V14')),
                ('choice15', models.CharField(blank=True, max_length=2, verbose_name='V15')),
                ('choice16', models.CharField(blank=True, max_length=2, verbose_name='V16')),
                ('choice17', models.CharField(blank=True, max_length=2, verbose_name='V17')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Values',
        ),
    ]
