# Generated by Django 5.1.4 on 2025-01-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_projectstatusrequest_requester_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='crypto_wallet_address',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
    ]
