from rest_framework import serializers
from appGrupo9.models.user import User
from appGrupo9.models.account import Account
from appGrupo9.serializers.accountSerializer import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'phone_number', 'city_owner', 'account']
    
    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
            
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'city_owner': user.city_owner,
            'account': {
                'id': account.id,
                'Casa_Apartamento': account.Casa_Apartamento,
                'Venta_arriendo': account.Venta_arriendo,
                'Superficie': account.Superficie,
                'Nueva_Usada': account.Nueva_Usada,
                'Precio': account.Precio
                }
            }       