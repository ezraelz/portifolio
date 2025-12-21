from django.db import models

class Faq(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    message = models.TextField(verbose_name='Discription')
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=False, auto_now_add=True)
    email = models.EmailField(verbose_name='Email', max_length=254)
    
    def __str__(self) -> str:
        return self.email
    
class CollectEmails(models.Model):
    email = models.EmailField(verbose_name='email', max_length=254)
    created_at = models.DateTimeField(verbose_name='created at', auto_now=False, auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email
