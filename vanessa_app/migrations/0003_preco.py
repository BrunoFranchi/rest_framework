# Generated by Django 3.2.11 on 2022-01-20 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vanessa_app', '0002_alter_servico_nivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precos', models.IntegerField(choices=[(30, 30), (40, 40), (50, 50)])),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vanessa_app.servico')),
            ],
        ),
    ]