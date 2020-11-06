from rest_framework import serializers

from shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'description', 'created_at', 'updated_at')

    def validate(self, data):
        request = self.context['request']

        try:
            # user can has only shop
            if Shop.objects.get(user_id = request.user.id):
                raise serializers.ValidationError('You already have a store!')
        except Shop.DoesNotExist:
            pass

        # set current user
        data['user'] = request.user

        return data
