# Generated by Django 2.0.2 on 2018-04-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('disambiguation', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('labelcode', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('disambiguation', models.CharField(max_length=150)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MusicShop.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('country', models.CharField(max_length=150)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MusicShop.Artist')),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MusicShop.Label')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstrelease', models.DateField()),
                ('title', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
                ('release', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MusicShop.Release')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('language', models.CharField(max_length=150)),
                ('recording', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MusicShop.Recording')),
            ],
        ),
        migrations.AddField(
            model_name='recording',
            name='release',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MusicShop.Release'),
        ),
    ]
