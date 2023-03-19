from rest_framework import serializers

from .models import Category, Product, Review

from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',     
        )

#add field during user creation
class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'is_staff')

class ProductForReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "address",
            "get_absolute_url",
            "phone",
            "map_url",
            "avg_rating",
            "get_image",
            "get_thumbnail",
        )

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    #product = ProductForReviewSerializer(read_only=True)
    class Meta:
        model = Review
        read_only_fields = (
            'user',
            'datetime',
        ),
        fields = (
            'id',
            'content',
            'rating',
            'user',
            'datetime',
        )

    def create(self, validated_data):
        #product_id = validated_data["product_id"]
        # get the product object using the slug
        #product = Product.objects.filter(id=product_id).first()

        # Create the review object with the validated data and user/product objects
        review = Review.objects.create(
            #user_id=user.id,
            #product=product,
            content=validated_data["content"],
            rating=validated_data["rating"],
        )

        return review    

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "address",
            "get_absolute_url",
            "phone",
            "map_url",
            "avg_rating",
            "get_image",
            "get_thumbnail",
            "reviews"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
            "get_image",
            "get_thumbnail",
        )


