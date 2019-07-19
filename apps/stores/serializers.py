from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Store
from apps.users.serializers import UserSerializer
from apps.users.models import User


class StoreSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    pk = serializers.IntegerField(
        read_only=True
        )

    def get_owner(self, obj):
        return obj.owner.username

    class Meta:
        model = Store
        fields = (
            'name',
            'description',
            'owner',
            'pk'
        )


class SalesSerializer(serializers.Serializer):
    month = serializers.CharField()
    amount = serializers.FloatField()


class StoreAnalysisSerializer(serializers.Serializer):
    current_net = serializers.FloatField()
    percentage_net_change = serializers.IntegerField()
    current_sales = serializers.FloatField()
    percentage_sales_change = serializers.IntegerField()
    current_profit = serializers.FloatField()
    percentage_profit_change = serializers.IntegerField()
    sales = SalesSerializer(many=True)

# class StaffSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, write_only=True)

#     class Meta:
#         model = Staff
#         fields = (
#             'username',
#             'email',
#             'password',
#         )

#     def create(self, validated_data):
#         return Staff.objects.create_staff(**validated_data)
