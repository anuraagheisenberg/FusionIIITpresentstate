# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-14 05:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_information', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fdate', models.DateField(default=datetime.date.today)),
                ('description', models.TextField()),
                ('feedback_type', models.CharField(choices=[('maintenance', 'Maintenance'), ('food', 'Food'), ('cleanliness', 'Cleanliness & Hygiene'), ('others', 'Others')], max_length=20)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_option', models.CharField(choices=[('mess1', 'Non_veg_mess'), ('mess2', 'Veg_mess')], default='mess2', max_length=20)),
                ('meal_time', models.CharField(choices=[('MB', 'Monday Breakfast'), ('ML', 'Monday Lunch'), ('MD', 'Monday Dinner'), ('TB', 'Tuesday Breakfast'), ('TL', 'Tuesday Lunch'), ('TD', 'Tuesday Dinner'), ('WB', 'Wednesday Breakfast'), ('WL', 'Wednesday Lunch'), ('WD', 'Wednesday Dinner'), ('THB', 'Thursday Breakfast'), ('THL', 'Thursday Lunch'), ('THD', 'Thursday Dinner'), ('FB', 'Friday Breakfast'), ('FL', 'Friday Lunch'), ('FD', 'Friday Dinner'), ('SB', 'Saturday Breakfast'), ('SL', 'Saturday Lunch'), ('SD', 'Saturday Dinner'), ('SUB', 'Sunday Breakfast'), ('SUL', 'Sunday Lunch'), ('SUD', 'Sunday Dinner')], max_length=20)),
                ('dish', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_change_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('request', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='central_mess.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Mess_meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet_date', models.DateField()),
                ('agenda', models.TextField()),
                ('venue', models.TextField()),
                ('meeting_time', models.CharField(choices=[('10', '10 a.m.'), ('11', '11 a.m.'), ('12', '12 p.m.'), ('13', '1 p.m.'), ('14', '2 p.m.'), ('15', '3 p.m.'), ('16', '4 p.m.'), ('17', '5 p.m.'), ('18', '6 p.m.'), ('19', '7 p.m.'), ('20', '8 p.m.'), ('21', '9 p.m.')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mess_minutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_minutes', models.FileField(upload_to='central_mess/')),
                ('meeting_date', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='central_mess.Mess_meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Mess_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField(default='1')),
                ('start_reg', models.DateField(default=datetime.date.today)),
                ('end_reg', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Messinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_option', models.CharField(choices=[('mess1', 'Non_veg_mess'), ('mess2', 'Veg_mess')], default='mess2', max_length=20)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], max_length=20)),
                ('amount', models.IntegerField(default=2370)),
                ('rebate_count', models.IntegerField(default=0)),
                ('rebate_amount', models.IntegerField(default=0)),
                ('nonveg_total_bill', models.IntegerField(default=0)),
                ('total_bill', models.IntegerField(default=2370)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Nonveg_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('order_interval', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Nonveg_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('order_interval', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('amount_paid', models.IntegerField(default=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Rebate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('leave_type', models.CharField(choices=[('casual', 'Casual'), ('vacation', 'Vacation')], default='casual', max_length=20)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Special_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('request', models.TextField()),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('item1', models.CharField(max_length=50)),
                ('item2', models.CharField(max_length=50)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Vacation_food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.AddField(
            model_name='nonveg_data',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='central_mess.Nonveg_menu'),
        ),
        migrations.AddField(
            model_name='nonveg_data',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='payments',
            unique_together=set([('student_id', 'sem')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthly_bill',
            unique_together=set([('student_id', 'month')]),
        ),
        migrations.AlterUniqueTogether(
            name='messinfo',
            unique_together=set([('student_id', 'mess_option')]),
        ),
    ]
