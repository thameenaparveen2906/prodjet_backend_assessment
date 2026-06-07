from django.urls import path
from .views import *

urlpatterns = [
    path('coupons', create_coupon),
    path('coupons/list', list_coupons),
    path('coupons/apply', apply_coupon_view),
    path('coupons/<str:code>/disable', disable_coupon),
]