# Generated by Django 2.1.1 on 2018-12-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='reader',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='readers.Reader'),
            preserve_default=False,
        ),
    ]