from rest_framework import serializers
from .models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

    def validate_discountValue(self, value):
        if value <= 0:
            raise serializers.ValidationError("Discount must be greater than 0")
        return value

    def validate(self, data):
        if data.get('discountType') == 'PERCENTAGE':
            if data.get('discountValue') > 100:
                raise serializers.ValidationError("Percentage cannot be more than 100")
        return data