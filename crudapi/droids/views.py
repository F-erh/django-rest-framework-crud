from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Droid
from .permissions import IsOwnerOrReadOnly
from .serializers import DroidSerializer
from .pagination import CustomPagination
from .filters import DroidFilter


class ListCreateDroidAPIView(ListCreateAPIView):
    serializer_class = DroidSerializer
    queryset = Droid.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DroidFilter

    def perform_create(self, serializer):
        # Assign the user who created the Droid
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyDroidAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DroidSerializer
    queryset = Droid.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





