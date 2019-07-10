from rest_framework.generics import (
    CreateAPIView, )

from posts.models import Post

from .serializers import (
    PostCreateUpdateSerializer,
)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
