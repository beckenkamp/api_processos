from django.contrib.auth.models import User, Group
from api.processos.models import Process
from rest_framework import viewsets
from api.processos.serializers import UserSerializer, GroupSerializer, ProcessSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProcessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def perform_create(self, serializer):
        serializer.save()

        data = self.request.data

        from django.core.mail import send_mail

        send_mail('Novo processo adicionado', 
                  'Um novo processo foi adiciondo. Numero: %s | Dados: %s' % (data['number'],
                                                                              data['data']),
                  'from@example.com',
                  ['to@example.com'], fail_silently=False)
