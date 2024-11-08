from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializes user object
    """

    class Meta:
        model = User
        fields = ["id", "email", "name", "password"]
        
    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user