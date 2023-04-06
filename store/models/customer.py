from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def is_email_exists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
    
    def is_phone_exists(self):
        if Customer.objects.filter(phone=self.phone):
            return True
        else:
            return False
        