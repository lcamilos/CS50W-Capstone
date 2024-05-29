# Generated by Django 4.2.5 on 2024-05-04 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacherdeptinfo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherSubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Division List',
            },
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='div_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teachersubinfo'),
        ),
        migrations.DeleteModel(
            name='TeacherDivInfo',
        ),
    ]
