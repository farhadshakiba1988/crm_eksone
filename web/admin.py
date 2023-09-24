from django.contrib import admin

from web.models import Employees, Customers, EmployeeRoles, FailureReasons, CustomerEmployeeTels, Status, Invoices, \
    InvoiceItems, CustomerEmployees, CustomerEmployeeAddresses, CustomerEmployeeEmails

admin.site.register(Customers)
admin.site.register(EmployeeRoles)
admin.site.register(Employees)
admin.site.register(FailureReasons)
admin.site.register(Status)
admin.site.register(Invoices)
admin.site.register(InvoiceItems)
admin.site.register(CustomerEmployees)
admin.site.register(CustomerEmployeeAddresses)
admin.site.register(CustomerEmployeeEmails)
admin.site.register(CustomerEmployeeTels)
