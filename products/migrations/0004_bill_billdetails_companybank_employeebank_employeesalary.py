# Generated by Django 3.2.7 on 2021-10-02 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211001_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField()),
                ('salary_amount', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('ifsc_no', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('ifsc_no', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.company')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.bill')),
            ],
        ),
    ]
