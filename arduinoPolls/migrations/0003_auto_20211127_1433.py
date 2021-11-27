# Generated by Django 3.2.5 on 2021-11-27 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arduinoPolls', '0002_lecturas'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturas',
            name='Arduino',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='arduinoPolls.arduino'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lecturas',
            name='Lectura_1',
            field=models.FloatField(help_text='CO2', null=True),
        ),
        migrations.AlterField(
            model_name='lecturas',
            name='Lectura_2',
            field=models.FloatField(help_text='CO', null=True),
        ),
        migrations.AlterField(
            model_name='lecturas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
