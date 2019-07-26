# Generated by Django 2.2.3 on 2019-07-26 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_myquestions_last_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myquestions',
            name='my_collection',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.MyCollections'),
        ),
        migrations.AlterField(
            model_name='myquestions',
            name='original_collection',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Collection'),
        ),
        migrations.AlterField(
            model_name='myquestions',
            name='original_question',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='myquestions',
            name='rep_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]