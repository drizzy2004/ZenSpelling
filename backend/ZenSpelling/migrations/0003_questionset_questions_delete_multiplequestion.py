# Generated by Django 5.0.2 on 2024-03-19 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZenSpelling', '0002_questionset_multiplequestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionset',
            name='questions',
            field=models.ManyToManyField(to='ZenSpelling.question'),
        ),
        migrations.DeleteModel(
            name='MultipleQuestion',
        ),
    ]