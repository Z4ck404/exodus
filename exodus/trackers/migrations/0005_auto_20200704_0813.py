# Generated by Django 2.2.13 on 2020-07-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0004_auto_20200409_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tracker',
            name='category',
            field=models.ManyToManyField(blank=True, to='trackers.TrackerCategory'),
        ),
    ]
