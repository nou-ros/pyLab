from rest_framework import serializers

from profile_app import models

#basic serialier. Created to reaserch various APIView and APIViewsets operations. \
# We did not use any model information here. 
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView and APIviewSet"""
    name = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #we make the password only available while creating and updating
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }
    
    #we have to override create function so password don't get visible 
    def create(self, validated_data):
        """Create and return a new user""" 
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}