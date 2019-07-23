# Generated by Django 2.2.3 on 2019-07-11 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(choices=[('stripe', 'Stripe'), ('check', 'Check'), ('non-cash', 'Non cash')], default='stripe', max_length=155),
        ),
    ]
