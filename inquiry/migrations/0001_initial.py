# Generated by Django 5.0.4 on 2024-06-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer', models.AutoField(primary_key=True, serialize=False)),
                ('answer_content', models.TextField()),
                ('answer_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question', models.AutoField(primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=30)),
                ('question_content', models.TextField()),
                ('question_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]