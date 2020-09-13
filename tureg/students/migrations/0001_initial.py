# Generated by Django 3.1.1 on 2020-09-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
                ('semester', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('seat', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('courses', models.ManyToManyField(blank=True, related_name='course', to='students.Subject')),
            ],
        ),
    ]
