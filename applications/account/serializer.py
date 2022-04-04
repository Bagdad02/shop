from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)


    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError('password didnt match!')
        return attrs

    def validate_email(self,email):
        if not email.endswith("gmail.com"):
            raise serializers.ValidationError("Your email must end with 'gmail.com'")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        #TODO: Send maill


        return user
