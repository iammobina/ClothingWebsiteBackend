# Generated by Django 2.1.7 on 2019-07-10 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True, max_length=300)),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(blank=True, upload_to='userimage/')),
                ('Name', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('userId', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Confirm', models.CharField(help_text='Confirm your password', max_length=100)),
                ('Phone', models.CharField(blank=True, max_length=15)),
                ('Email', models.EmailField(blank=True, max_length=100)),
                ('Address', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='design',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
