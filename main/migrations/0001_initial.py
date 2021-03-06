# Generated by Django 2.0.7 on 2018-07-21 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paci', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('office', models.IntegerField()),
                ('rent', models.PositiveIntegerField()),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renter', to='main.Complex')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='main.Renter'),
        ),
    ]
