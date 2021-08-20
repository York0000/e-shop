from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class EmployeeModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='employee')
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
