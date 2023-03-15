
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from KaynakApp.models import Mesaj,Kullanıcı,KullanıcıTYTDeneme,KullanıcıAYTDenemeleri
from KaynakApp.models import SoruBankası,SoruBankasıYorum,SoruBankasıYorumBeğeni,SoruBankasıPuanlama
from KaynakApp.models import Kanal,KanalYorum,KanalYorumBeğeni,KanalPuanlama,BranşDenemesi,BranşDenemesiYorum,BranşDenemesiYorumBeğeni
from KaynakApp.models import BranşDenemesiPuanlama,GenelDeneme,GenelDenemeYorum,GenelDenemeYorumBeğeni,GenelDenemePuanlama
from KaynakApp.API.serializers import KullanıcıTYTDenemeSerializer,KullanıcıAYTDenemeleriSerializer
from KaynakApp.API.serializers import MesajSerializer,KullanıcıSerializer,SoruBankasıSerializer
from KaynakApp.API.serializers import SoruBankasıYorumBeğeniSerializer,SoruBankasıYorumSerializer,SoruBankasıPuanlamaSerializer
from KaynakApp.API.serializers import KanalYorumBeğeniSerializer,KanalYorumSerializer,KanalPuanlamaSerializer,KanalSerializer
from KaynakApp.API.serializers import BranşDenemesiYorumBeğeniSerializer,BranşDenemesiYorumSerializer,BranşDenemesiPuanlamaSerializer,BranşDenemesiSerializer
from KaynakApp.API.serializers import GenelDenemeYorumBeğeniSerializer,GenelDenemeYorumSerializer,GenelDenemePuanlamaSerializer,GenelDenemeSerializer

class MesajAPIView(generics.ListCreateAPIView):
    queryset = Mesaj.objects.all()
    serializer_class = MesajSerializer

class KullanıcıAPIView(generics.ListCreateAPIView):
    queryset = Kullanıcı.objects.all()
    serializer_class = KullanıcıSerializer 

class KullanıcıSpesificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kullanıcı.objects.all()
    serializer_class = KullanıcıSerializer

class KullanıcıTYTDenemeAPIView(generics.ListCreateAPIView):
    queryset = KullanıcıTYTDeneme.objects.all()
    serializer_class = KullanıcıTYTDenemeSerializer

class KullanıcıAYTDenemeAPIView(generics.ListCreateAPIView):
    queryset = KullanıcıAYTDenemeleri.objects.all()
    serializer_class = KullanıcıAYTDenemeleriSerializer

########SoruBankası########
class SoruBankasıAPIView(generics.ListCreateAPIView):
    queryset = SoruBankası.objects.all()
    serializer_class = SoruBankasıSerializer

class SoruBankasıSpesificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoruBankası.objects.all()
    serializer_class = SoruBankasıSerializer

class SoruBankasıYorumAPIView(generics.ListCreateAPIView):
    queryset = SoruBankasıYorum.objects.all()
    serializer_class = SoruBankasıYorumSerializer

class SoruBankasıSpesificYorumAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoruBankasıYorum.objects.all()
    serializer_class = SoruBankasıYorumSerializer

class SoruBankasıPuanlamaAPIView(generics.ListCreateAPIView):
    queryset = SoruBankasıPuanlama.objects.all()
    serializer_class = SoruBankasıPuanlamaSerializer

class SoruBankasıSpesificPuanlamaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoruBankasıPuanlama.objects.all()
    serializer_class = SoruBankasıPuanlamaSerializer

class SoruBankasıYorumBeğeniAPIView(generics.ListCreateAPIView):
    queryset = SoruBankasıYorumBeğeni.objects.all()
    serializer_class = SoruBankasıYorumBeğeniSerializer

class SoruBankasıSpesificYorumBeğeniAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoruBankasıYorumBeğeni.objects.all()
    serializer_class = SoruBankasıYorumBeğeniSerializer
########SoruBankası########

########GenelDeneme########
class GenelDenemeAPIView(generics.ListCreateAPIView):
    queryset = GenelDeneme.objects.all()
    serializer_class = GenelDenemeSerializer

class GenelDenemeSpesificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenelDeneme.objects.all()
    serializer_class = GenelDenemeSerializer

class GenelDenemeYorumAPIView(generics.ListCreateAPIView):
    queryset = GenelDenemeYorum.objects.all()
    serializer_class = GenelDenemeYorumSerializer

class GenelDenemeSpesificYorumAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenelDenemeYorum.objects.all()
    serializer_class = GenelDenemeYorumSerializer

class GenelDenemeYorumBeğeniAPIView(generics.ListCreateAPIView):
    queryset = GenelDenemeYorumBeğeni.objects.all()
    serializer_class = GenelDenemeYorumBeğeniSerializer

class GenelDenemeSpesificYorumBeğeniAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenelDenemeYorumBeğeni.objects.all()
    serializer_class = GenelDenemeYorumBeğeniSerializer    

class GenelDenemePuanlamaAPIView(generics.ListCreateAPIView):
    queryset = GenelDenemePuanlama.objects.all()
    serializer_class = GenelDenemePuanlamaSerializer
    
class GenelDenemeSpesificPuanlamaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenelDenemePuanlama.objects.all()
    serializer_class = GenelDenemePuanlamaSerializer
########GenelDeneme########

########BranşDenemesi########
class BranşDenemesiAPIView(generics.ListCreateAPIView):
    queryset = BranşDenemesi.objects.all()
    serializer_class = BranşDenemesiSerializer

class BranşDenemesiSpesificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BranşDenemesi.objects.all()
    serializer_class = BranşDenemesiSerializer

class BranşDenemesiYorumAPIView(generics.ListCreateAPIView):
    queryset = BranşDenemesiYorum.objects.all()
    serializer_class = BranşDenemesiYorumSerializer

class BranşDenemesiSpesificYorumAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BranşDenemesiYorum.objects.all()
    serializer_class = BranşDenemesiYorumSerializer
    
class BranşDenemesiYorumBeğeniAPIView(generics.ListCreateAPIView):
    queryset = BranşDenemesiYorumBeğeni.objects.all()
    serializer_class = BranşDenemesiYorumBeğeniSerializer

class BranşDenemesiSpesificYorumBeğeniAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BranşDenemesiYorumBeğeni.objects.all()
    serializer_class = BranşDenemesiYorumBeğeniSerializer

class BranşDenemesiPuanlamaAPIView(generics.ListCreateAPIView):
    queryset = BranşDenemesiPuanlama.objects.all()
    serializer_class = BranşDenemesiPuanlamaSerializer

class BranşDenemesiSpesificPuanlamaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BranşDenemesiPuanlama.objects.all()
    serializer_class = BranşDenemesiPuanlamaSerializer
########BranşDenemesi########

########Kanal########
class KanalAPIView(generics.ListCreateAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSerializer

class KanalSpesificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSerializer

class KanalYorumAPIView(generics.ListCreateAPIView):
    queryset = KanalYorum.objects.all()
    serializer_class = KanalYorumSerializer

class KanalSpesificYorumAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KanalYorum.objects.all()
    serializer_class = KanalYorumSerializer

class KanalYorumBeğeniAPIView(generics.ListCreateAPIView):
    queryset = KanalYorumBeğeni.objects.all()
    serializer_class = KanalYorumBeğeniSerializer

class KanalYorumSpesificBeğeniAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KanalYorumBeğeni.objects.all()
    serializer_class = KanalYorumBeğeniSerializer

class KanalPuanlamaAPIView(generics.ListCreateAPIView):
    queryset = KanalPuanlama.objects.all()
    serializer_class = KanalPuanlamaSerializer

class KanalSpesificPuanlamaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KanalPuanlama.objects.all()
    serializer_class = KanalPuanlamaSerializer
########Kanal########
