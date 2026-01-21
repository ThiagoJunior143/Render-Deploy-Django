from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('appliance', 'Appliance'),
        ('electronics', 'Electronics'),
        ('phones', 'Phones'),
        ('fashion', 'Fashion'),
        ('beauty', 'Beauty'),
        ('computing', 'Computing'),
    )

    title = models.CharField(max_length=255)
    image = models.URLField(max_length=500)
    price = models.PositiveIntegerField()
    slash_price = models.PositiveIntegerField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
 
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
