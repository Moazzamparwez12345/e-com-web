# Generated by Django 4.2.7 on 2024-03-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_products_prod_cata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_img',
            field=models.FileField(default=None, max_length=500, null=True, upload_to='Products'),
        ),
    ]