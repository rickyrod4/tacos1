<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-09-17 20:42

from django.conf import settings
=======
# Generated by Django 3.0.8 on 2020-08-18 21:46

>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ordered_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tacos_ordered', to=settings.AUTH_USER_MODEL)),
=======
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc
            ],
        ),
        migrations.CreateModel(
            name='Taco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('tortilla', models.CharField(choices=[('flour', 'Flour'), ('corn', 'Corn')], default='flour', max_length=10)),
                ('taco_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity_ordered', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tacos_on_order', to='home.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(choices=[('egg', 'Egg'), ('potato', 'Potato'), ('bean', 'Bean'), ('cheese', 'Cheese'), ('carne asada', 'Carne Asada'), ('chicken fajita', 'Chicken Fajita'), ('beef fajita', 'Beef Fajita'), ('pastor', 'Pastor'), ('barbacoa', 'Barbacoa'), ('lengua', 'Lengua'), ('bacon', 'Nacon'), ('nopales', 'Nopales'), ('sausage', 'Sausage')], max_length=255)),
                ('ingredient_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('taco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='home.Taco')),
=======
                ('taco_type', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorite', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_taco', to='home.User')),
                ('tacos_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taco_history', to='home.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ordered_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tacos_ordered', to='home.User')),
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc
            ],
        ),
    ]
