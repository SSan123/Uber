# Generated by Django 4.2 on 2023-05-30 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_studentsaddress_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsaddress',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_address', to='users.students'),
        ),
    ]
