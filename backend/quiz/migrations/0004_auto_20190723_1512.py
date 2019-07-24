# Generated by Django 2.2.3 on 2019-07-23 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190723_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='myquestions',
            name='original_question',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='myquestions',
            name='last_rep_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='myquestions',
            name='next_rep_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='myquestions',
            name='rep_count',
            field=models.IntegerField(default=0),
        ),
    ]