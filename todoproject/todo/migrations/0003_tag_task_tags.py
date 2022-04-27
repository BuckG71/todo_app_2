# Generated by Django 4.0.4 on 2022-04-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_comment_comment_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='todo.tag'),
        ),
    ]
