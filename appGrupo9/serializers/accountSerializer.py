from appGrupo9.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['Casa_Apartamento', 'Venta_arriendo', 'Superficie', 'Nueva_Usada', 'Precio']