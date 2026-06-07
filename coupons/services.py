from .models import Coupon
from django.utils import timezone


def apply_coupon(code, cart_value):
    try:
        coupon = Coupon.objects.get(code=code)
    except Coupon.DoesNotExist:
        return {"error": "Invalid coupon code"}

    if not coupon.isActive:
        return {"error": "Coupon is inactive"}
    
    if coupon.expiryDate:
        if coupon.expiryDate < timezone.now():
            return {"message": "Coupon has expired"}

    if cart_value < coupon.minCartValue:
        return {"error": f"Cart value should be at least ₹{coupon.minCartValue}"}
    
    if coupon.discountType == "FLAT":
        discount = coupon.discountValue
    else:
        discount = (coupon.discountValue / 100) * cart_value
    
    if coupon.maxDiscount:
            discount = min(discount, coupon.maxDiscount)


    final_amount = max(cart_value - discount, 0)

    return {
        "cartValue": cart_value,
        "discount": discount,
        "finalAmount": final_amount,
        "message": "Coupon applied successfully"
    }