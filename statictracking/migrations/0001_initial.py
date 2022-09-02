# Generated by Django 4.0.6 on 2022-08-07 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_res', models.BooleanField()),
                ('cs', models.IntegerField()),
                ('time', models.IntegerField()),
                ('death', models.IntegerField()),
                ('game_properties', models.ManyToManyField(blank=True, related_name='games', to='statictracking.property')),
                ('game_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='statictracking.user')),
            ],
        ),
    ]
