# Generated by Django 5.1.1 on 2024-10-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.IntegerField(default=0, primary_key='True', serialize=False)),
                ('order_id', models.IntegerField(default='null', max_length=150)),
                ('product_id', models.IntegerField(default='null', max_length=150)),
                ('quality', models.FloatField(default=0.0, max_length=50)),
                ('rate', models.FloatField(default=0.0, max_length=50)),
                ('ammount', models.FloatField(default=0.0, max_length=50)),
                ('status', models.CharField(default='process pending', max_length=150)),
                ('delivery_date', models.DateField(default='present date')),
                ('cr_date', models.DateField(default='present date')),
            ],
        ),
    ]
