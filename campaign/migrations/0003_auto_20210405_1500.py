# Generated by Django 3.1.7 on 2021-04-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_campaign_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.CharField(default='In Review', max_length=50, null=True),
        ),
    ]
