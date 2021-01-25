# Generated by Django 3.1.4 on 2021-01-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oams', '0007_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='year',
            field=models.CharField(choices=[('p1', 'P1'), ('p2', 'P2'), ('e1', 'E1'), ('e2', 'E2'), ('e3', 'E3'), ('e4', 'E4')], default=None, max_length=10, null=True),
        ),
    ]
