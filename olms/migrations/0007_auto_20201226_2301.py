# Generated by Django 3.1.4 on 2020-12-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olms', '0006_auto_20201215_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaves',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('cgranted', 'cgranted'), ('granted', 'granted'), ('rejected', 'rejected'), ('on_leave', 'On Leave'), ('delayed', 'Delayed'), ('completed', 'Completed'), ('expired', 'Expired')], default='pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='outing',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('cgranted', 'cgranted'), ('granted', 'granted'), ('rejected', 'rejected'), ('on_outing', 'On Outing'), ('completed', 'Completed'), ('expired', 'Expired')], default='pending', max_length=9),
        ),
    ]
