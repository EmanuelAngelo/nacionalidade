# Generated by Django 3.1.4 on 2020-12-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_disciplina_alunos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Matricula'),
        ),
    ]
