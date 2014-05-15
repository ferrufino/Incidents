# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class Account(models.Model):
    username = models.CharField(db_column='Username', primary_key=True, max_length=15) # Field name made lowercase.
    type = models.CharField(max_length=15, blank=True)
    def __str__(self):
       return str(self.username)
    class Meta:
        managed = False
        db_table = 'Account'
        

class Administrator(models.Model):
    adminid = models.CharField(db_column='AdminID', primary_key=True, max_length=9) # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=15, blank=True) # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=15, blank=True) # Field name made lowercase.
    email = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    username = models.ForeignKey(Account, db_column='Username', blank=True, null=True) # Field name made lowercase.
    def __str__(self):
       return str(self.username)
    class Meta:
        managed = False
        db_table = 'Administrator'

class Client(models.Model):
    clientid = models.CharField(db_column='ClientId', primary_key=True, max_length=9) # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=15, blank=True) # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=15, blank=True) # Field name made lowercase.
    email = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    username = models.ForeignKey(Account, db_column='Username', blank=True, null=True) # Field name made lowercase.
    def __str__(self):
       return str(self.username)
    class Meta:
        managed = False
        db_table = 'Client'

class Department(models.Model):
    deptid = models.CharField(db_column='DeptID', primary_key=True, max_length=1) # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=15, blank=True) # Field name made lowercase.
    def __unicode__(self):
       return unicode(self.deptname)
    class Meta:
        managed = False
        db_table = 'Department'

class Employee(models.Model):
    empid = models.CharField(db_column='EmpId', primary_key=True, max_length=9) # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=15, blank=True) # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=15, blank=True) # Field name made lowercase.
    email = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    deptid = models.ForeignKey(Department, db_column='DeptID', blank=True, null=True) # Field name made lowercase.
    username = models.ForeignKey(Account, db_column='Username', blank=True, null=True) # Field name made lowercase.
    def __str__(self):
       return str(self.username)
    class Meta:
        managed = False
        db_table = 'Employee'

class Incident(models.Model):
    incidentid = models.CharField(db_column='IncidentId', primary_key=True, max_length=10) # Field name made lowercase.
    type = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=15, blank=True)
    urgency = models.IntegerField(blank=True, null=True)
    impact = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=144, blank=True)
    clientid = models.ForeignKey(Client, db_column='ClientId', blank=True, null=True) # Field name made lowercase.
    adminid = models.ForeignKey(Administrator, db_column='AdminID', blank=True, null=True) # Field name made lowercase.
    datesubmitted = models.DateField(db_column='DateSubmitted', blank=True, null=True) # Field name made lowercase.
    def __unicode__(self):
       return unicode(self.incidentid)
    class Meta:
        managed = False
        db_table = 'Incident'

class IncidentHistory(models.Model):
    incidentid = models.ForeignKey(Incident, db_column='IncidentId', primary_key=True) # Field name made lowercase.
    empid = models.ForeignKey(Employee, db_column='EmpId', primary_key=True) # Field name made lowercase.
    timestart = models.TimeField(db_column='TimeStart', blank=True, null=True) # Field name made lowercase.
    timeend = models.TimeField(db_column='TimeEnd', blank=True, null=True) # Field name made lowercase.
    dateworked = models.DateField(db_column='DateWorked', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=144, blank=True)
    def __str__(self):
       return str(self.incidentid)
    class Meta:
        managed = False
        db_table = 'IncidentHistory'

class IncidentSummary(models.Model):
    incidentid = models.CharField(db_column='IncidentId', primary_key=True, max_length=10) # Field name made lowercase.
    description = models.CharField(max_length=144, blank=True)
    peopleworking = models.BigIntegerField(db_column='peopleWorking') # Field name made lowercase.
    minutesworked = models.DecimalField(db_column='minutesWorked', max_digits=35, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    hoursworked = models.DecimalField(db_column='hoursWorked', max_digits=35, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    def __unicode__(self):
       return unicode(self.IncidentId)
    class Meta:
        managed = False
        db_table = 'incidentsummary'


