from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Calendar(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    date = models.DateField()


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    rating = models.IntegerField(
    default=10,
    validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
        ]
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False) 

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('product_detail', args=[self.product.slug])


class Time(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="time")
    time = models.IntegerField(
    default='--:--',
    validators=[
        MaxValueValidator(21),
        MinValueValidator(10)
        ]
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False) 