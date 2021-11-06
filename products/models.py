
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# customer crate model here


class Customer(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    expire_date = models.DateField()
    mfg_date = models.DateField()
    batch_no = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.price} {self.stock} {self.expire_date} {self.mfg_date} "


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    bank_account_no = models.CharField(max_length=255, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {self.contact_no} {self.email} {self.bank_account_no}"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {self.contact}"


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    joining_date = models.DateField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    salary_date = models.DateField(null=True)
    salary_amount = models.CharField(max_length=255, null=True)
    bank_account_no = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {self.contact} {self.joining_date} {self.salary_date} {self.salary_amount} {self.bank_account_no}"


class Order(models.Model):
    name = models.CharField(max_length=255)
    ProductName = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True)
    OrderDate = models.CharField(max_length=64)
    CheckOut = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.ProductName} {self.OrderDate} {self.CheckOut}"


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} {self.customer_id}"


class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    Qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.id} {self.bill_id} {self.Qty}"

# class CompanyBank(models.Model):
#     id=models.AutoField(primary_key=True)
#     bank_account_no=models.CharField(max_length=255)
#     ifsc_no=models.CharField(max_length=255)
#     company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
#     added_on=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

#     def __str__(self) :
#      return f"{self.id} {self.bank_account_no} {self.company_id}"

# class EmployeeBank(models.Model):
#     id=models.AutoField(primary_key=True)
#     bank_account_no=models.CharField(max_length=255)
#     ifsc_no=models.CharField(max_length=255)
#     employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
#     added_on=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

#     def __str__(self) :
#      return f"{self.id} {self.bank_account_no} {self.employee_id}"

# class EmployeeSalary(models.Model):
#     id=models.AutoField(primary_key=True)
#     employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
#     salary_date=models.DateField()
#     salary_amount=models.CharField(max_length=255)
#     added_on=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

    # def __str__(self) :
    #  return f"{self.id} {self.employee_id} {self.salary_date} {self.salary_amount}"

# class Offer(models.Model):
#     code = models.CharField(max_length=10)
#     description = models.CharField(max_length=255)
#     discount = models.FloatField()

#     def __str__(self) :
#         return f"{self.code} {self.description} {self.discount}"
