# Generated by Django 4.1.5 on 2023-01-13 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('comment', models.CharField(max_length=128)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conference.room')),
            ],
        ),
    ]
