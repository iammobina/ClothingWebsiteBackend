from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView)
from rest_framework.permissions import AllowAny

from posts.models import Post

from .serializers import (
    PostCreateUpdateSerializer,
    PostDetailSerializer)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
