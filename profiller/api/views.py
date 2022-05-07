# from jmespath import search
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerializer, ProfilDurumSerializer, ProfilFotoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import KendiProfiliYaDaReadonly, DurumSahibiYaDaReadonly
from rest_framework.filters import SearchFilter


class ProfilViewSet(
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):


    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated, KendiProfiliYaDaReadonly]
    filter_backends = [SearchFilter]
    search_fields = ['sehir']



class ProfilDurumViewSet(ModelViewSet):
    queryset = ProfilDurum.objects.all()
    serializer_class = ProfilDurumSerializer
    permission_classes = [IsAuthenticated, DurumSahibiYaDaReadonly] 

    def get_queryset(self):
        queryset = ProfilDurum.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profil__user__username=username)
        return queryset


    def perform_create(self, serializer):
        user_profil = self.request.user.profil
        serializer.save(user_profil = user_profil)
        

class ProfilFotoUpdateViewSet(generics.UpdateAPIView):
    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated] 

    def get_object(self):
        profil_foto = self.request.user.profil
        return profil_foto
        
