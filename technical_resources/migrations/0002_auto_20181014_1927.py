# Generated by Django 2.1.2 on 2018-10-14 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technical_resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='technical_resources.Category'),
        ),
    ]