# Generated by Django 3.2.7 on 2021-10-14 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='province',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='province.province'),
            preserve_default=False,
        ),
    ]
