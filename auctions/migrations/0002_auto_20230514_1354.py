# Generated by Django 3.1 on 2023-05-14 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='descriptions',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidding',
            name='images',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bidding',
            name='productnames',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidding',
            name='startingbids',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidding',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='closebid',
            name='images2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closebid',
            name='images3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closebid',
            name='patrimonio',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='idp',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='images2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='images3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='patrimonio',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
