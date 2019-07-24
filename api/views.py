from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer, NoteSerializer
from .models import Note


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):

    def get_serializer_context(self):
        if self.kwargs:
            return {"pk": self.kwargs['pk']}
        else:
            return {}

    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer