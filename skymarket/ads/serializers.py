from rest_framework import serializers

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Ad, Comment
from users.serializers import CurrentUserSerializer


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    def get_author_first_name(self, ad):
        return ad.author.first_name

    def get_author_last_name(self, ad):
        return ad.author.last_name

    def get_author_phone(self, ad):
        return str(ad.author.phone)

    author_first_name = serializers.SerializerMethodField(method_name='get_author_first_name')
    author_last_name = serializers.SerializerMethodField(method_name='get_author_last_name')
    phone = serializers.SerializerMethodField(method_name='get_author_phone')

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description",
                  "author_first_name", "author_last_name", "author_id"]


class CommentSerializer(serializers.ModelSerializer):
    def get_author_first_name(self, comment):
        return comment.author.first_name

    def get_author_last_name(self, comment):
        return comment.author.last_name

    def get_author_image(self, comment):
        return str(comment.author.image)

    author_first_name = serializers.SerializerMethodField(method_name='get_author_first_name')
    author_last_name = serializers.SerializerMethodField(method_name='get_author_last_name')
    author_image = serializers.SerializerMethodField(method_name='get_author_image')

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at",
                  "author_first_name", "author_last_name", "ad_id", "author_image"]


class CommentCreateSerializer(serializers.ModelSerializer):
    def get_author_first_name(self, comment):
        return comment.author.first_name

    def get_author_last_name(self, comment):
        return comment.author.last_name

    def get_author_image(self, comment):
        return str(comment.author.image)

    author_first_name = serializers.SerializerMethodField(method_name='get_author_first_name')
    author_last_name = serializers.SerializerMethodField(method_name='get_author_last_name')
    author_image = serializers.SerializerMethodField(method_name='get_author_image')

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at",
                  "author_first_name", "author_last_name", "ad_id", "author_image"]
