from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.models import User, UserPlatform, Platform, Keyword, UserKeyword
from backend.utils.user_controller import validate_password

MAX_USER_KEYWORDS = 8


class UserPlatformPostSerializer(serializers.Serializer):
    platform = serializers.CharField(max_length=255)
    link = serializers.CharField(max_length=255)


class UserPostSerializer(serializers.ModelSerializer):
    platforms = UserPlatformPostSerializer(many=True, required=False)
    keywords = serializers.ListField(
        child=serializers.CharField(max_length=63), required=False
    )

    class Meta:
        model = User
        read_only_fields = ["id"]
        fields = [
            "id",
            "first_name",
            "last_name",
            "user_type",
            "email",
            "password",
            "description",
            "country",
            "gender",
            "date_of_birth",
            "phone",
            "avg_pay",
            "known_as",
            "audience_num",
            "avg_views",
            "business_name",
            "business_link",
            "profile_picture",
            "platforms",
            "keywords",
        ]
        extra_kwargs = {
            "gender": {"required": False},
            "date_of_birth": {"required": False},
            "social_media": {"required": False},
            "country": {"required": False},
            "phone": {"required": False},
            "avg_pay": {"required": False},
            "known_as": {"required": False},
            "audience_num": {"required": False},
            "avg_views": {"required": False},
            "business_name": {"required": False},
            "business_link": {"required": False},
            "profile_picture": {"required": False},
        }

    def create(self, validated_data):

        # Validate password.
        validate_password(validated_data["password"])

        # Check if keywords are too many.
        if "keywords" in validated_data:
            if len(validated_data["keywords"]) > MAX_USER_KEYWORDS:
                raise ValidationError(
                    "A user cannot have more than "
                    + str(MAX_USER_KEYWORDS)
                    + " keywords."
                )

        new_user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            user_type=validated_data["user_type"],
        )

        # Extra fields.
        if "gender" in validated_data:
            new_user.gender = validated_data["gender"]
        if "description" in validated_data:
            new_user.description = validated_data["description"]
        if "country" in validated_data:
            new_user.country = validated_data["country"]
        if "profile_picture" in validated_data:
            new_user.profile_picture = validated_data["profile_picture"]
        if "date_of_birth" in validated_data:
            new_user.date_of_birth = validated_data["date_of_birth"]
        if "avg_pay" in validated_data:
            new_user.avg_pay = validated_data["avg_pay"]
        if "keywords" in validated_data:
            keyword_list = []
            for keyword in validated_data["keywords"]:
                if keyword in keyword_list:
                    continue
                keyword_list.append(keyword)
                keyword = keyword.lower()
                try:  # Check if keyword already exists.
                    keyword = Keyword.objects.get(name=keyword)
                except Keyword.DoesNotExist:
                    keyword = Keyword.objects.create(name=keyword)
                UserKeyword.objects.create(
                    user=new_user,
                    keyword=keyword,
                )

        if new_user.user_type == "influencer":
            if "avg_views" in validated_data:
                new_user.avg_views = validated_data["avg_views"]
            if "known_as" in validated_data:
                new_user.known_as = validated_data["known_as"]
            if "audience_num" in validated_data:
                new_user.audience_num = validated_data["audience_num"]
            if "platforms" in validated_data:
                for platform_temp in validated_data["platforms"]:
                    platform = platform_temp["platform"].title()
                    try:  # Check if platform already exists.
                        platform = Platform.objects.get(name=platform)
                    except Platform.DoesNotExist:
                        platform = Platform.objects.create(name=platform)
                    UserPlatform.objects.create(
                        user=new_user,
                        platform=platform,
                        link=platform_temp["link"],
                    )
        elif new_user.user_type == "business":
            if "business_name" in validated_data:
                new_user.business_name = validated_data["business_name"]
            if "business_link" in validated_data:
                new_user.business_link = validated_data["business_link"]

        new_user.save()
        return new_user


class KeywordGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        read_only_fields = ["id"]
        fields = ["id", "name"]


class PlatformGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        read_only_fields = ["id"]
        fields = ["id", "name"]
