# Generated by Django 4.2.11 on 2024-04-05 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserCred',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to='data_backend.usercred')),
                ('contact_no', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('discipline', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teacher', serialize=False, to='data_backend.usercred')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=100)),
                ('whatsapp_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_backend.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_backend.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='data_backend.teacher'),
        ),
    ]