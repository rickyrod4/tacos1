# Generated by Django 3.0.8 on 2020-09-17 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200917_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='taco',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='home.Taco'),
        ),
    ]