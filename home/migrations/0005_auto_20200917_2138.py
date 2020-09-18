# Generated by Django 3.0.8 on 2020-09-17 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20200917_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='taco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='home.Taco'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tacos_ordered', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taco',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tacos_on_order', to='home.Order'),
        ),
    ]