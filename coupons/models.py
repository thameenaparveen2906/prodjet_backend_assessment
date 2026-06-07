from django.db import models

class Coupon(models.Model):
    DISCOUNT_TYPES = (
        ('FLAT', 'Flat'),
        ('PERCENTAGE', 'Percentage'),
    )

    code = models.CharField(max_length=50, unique=True)
    discountType = models.CharField(max_length=20, choices=DISCOUNT_TYPES)
    discountValue = models.FloatField()
    minCartValue = models.FloatField()
    isActive = models.BooleanField(default=True)
    expiryDate = models.DateTimeField(null=True, blank=True)
    maxDiscount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.code