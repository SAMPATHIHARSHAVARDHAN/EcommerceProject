# Generated by Django 5.1.1 on 2024-10-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quality',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='ammount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default='null'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(default='null'),
        ),
        migrations.AlterField(
            model_name='order',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='process pending', max_length=50),
        ),
    ]
