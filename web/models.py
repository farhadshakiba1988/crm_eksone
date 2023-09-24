from django.db import models


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    is_disabled = models.BooleanField(null=True, default=None)


class EmployeeRoles(models.Model):
    employee_role_id = models.AutoField(primary_key=True)
    employee_role_name = models.CharField(max_length=255)


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_role = models.ForeignKey(EmployeeRoles, on_delete=models.RESTRICT, null=True, default=None)
    employee_first_name = models.CharField(max_length=255)
    employee_last_name = models.CharField(max_length=255)
    is_disabled = models.BooleanField(null=True, default=None)


class FailureReasons(models.Model):
    failure_reason_id = models.AutoField(primary_key=True)
    failure_reason_title = models.CharField(max_length=500)
    is_disabled = models.BooleanField(null=True, default=None)


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_begin_date = models.DateTimeField(null=True, default=None)
    project_end_date = models.DateTimeField(null=True, default=None)
    employee = models.ForeignKey(Employees, on_delete=models.RESTRICT, null=True, default=None)
    customer_employee = models.ForeignKey('CustomerEmployees', on_delete=models.RESTRICT, null=True, default=None)
    status = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, default=None)
    failure_reason = models.ForeignKey(FailureReasons, on_delete=models.RESTRICT, null=True, default=None)
    is_disabled = models.BooleanField(null=True, default=None)


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=255)
    is_disabled = models.BooleanField(null=True, default=None)


class Invoices(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_date = models.DateTimeField(null=True, default=None)
    project = models.ForeignKey(Projects, on_delete=models.RESTRICT, null=True, default=None)
    is_disabled = models.BooleanField(null=True, default=None)


class InvoiceItems(models.Model):
    invoice_item_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoices, on_delete=models.RESTRICT, null=True, default=None)
    invoice_item = models.CharField(max_length=255)
    purchase_price = models.FloatField(null=True, default=None)
    sell_price = models.FloatField(null=True, default=None)
    invoice_item_quantity = models.IntegerField(null=True, default=None)
    is_disabled = models.BooleanField(null=True, default=None)


class CustomerEmployees(models.Model):
    customer_employee_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.RESTRICT, null=True, default=None)
    customer_employee_firstname = models.CharField(max_length=255)
    customer_employee_lastname = models.CharField(max_length=255)
    is_disabled = models.BooleanField(null=True, default=None)


class CustomerEmployeeAddresses(models.Model):
    customer_employee_address_id = models.AutoField(primary_key=True)
    customer_employee = models.ForeignKey(CustomerEmployees, on_delete=models.RESTRICT, null=True, default=None)
    address = models.CharField(max_length=255, null=True, default=None)
    is_disabled = models.BooleanField(null=True, default=None)


class CustomerEmployeeEmails(models.Model):
    customer_employee_email_id = models.AutoField(primary_key=True)
    customer_employee = models.ForeignKey(CustomerEmployees, on_delete=models.RESTRICT, null=True, default=None)
    customer_employee_email = models.CharField(max_length=255, null=True, default=None)
    is_disabled = models.BooleanField(null=True, default=None)


class CustomerEmployeeTels(models.Model):
    customer_employee_tel_id = models.AutoField(primary_key=True)
    customer_employee = models.ForeignKey(CustomerEmployees, on_delete=models.RESTRICT, null=True, default=None)
    customer_employee_tel = models.CharField(max_length=255, null=True, default=None)
    is_disabled = models.BooleanField(null=True, default=None)
