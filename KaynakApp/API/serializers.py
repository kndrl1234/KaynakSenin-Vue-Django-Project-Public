
from rest_framework  import serializers
from KaynakApp.models import Mesaj,Kullanıcı,KullanıcıTYTDeneme,KullanıcıAYTDenemeleri
from KaynakApp.models import SoruBankası,SoruBankasıYorum,SoruBankasıYorumBeğeni,SoruBankasıPuanlama
from KaynakApp.models import Kanal,KanalYorum,KanalYorumBeğeni,KanalPuanlama,BranşDenemesi,BranşDenemesiYorum,BranşDenemesiYorumBeğeni
from KaynakApp.models import BranşDenemesiPuanlama,GenelDeneme,GenelDenemeYorum,GenelDenemeYorumBeğeni,GenelDenemePuanlama

class MesajSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesaj
        fields = '__all__'   

########Kullanıcı########

class KullanıcıTYTDenemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KullanıcıTYTDeneme
        fields = '__all__'   

class KullanıcıAYTDenemeleriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KullanıcıAYTDenemeleri
        fields = '__all__'   

class KullanıcıSerializer(serializers.ModelSerializer):
    KullanıcıTYTDenemeleri = KullanıcıTYTDenemeSerializer(many=True, read_only=True)
    KullanıcıAYTDenemeleri = KullanıcıAYTDenemeleriSerializer(many=True, read_only=True)
    class Meta:
        model = Kullanıcı
        fields = '__all__' 
########Kullanıcı########


########SoruBankası########
class SoruBankasıYorumBeğeniSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoruBankasıYorumBeğeni
        fields = '__all__' 

class SoruBankasıYorumSerializer(serializers.ModelSerializer):
    YorumBeğeni = SoruBankasıYorumBeğeniSerializer(many=True, read_only=True)
    class Meta:
        model = SoruBankasıYorum
        fields = '__all__' 

class SoruBankasıPuanlamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoruBankasıPuanlama
        fields = '__all__' 

class SoruBankasıSerializer(serializers.ModelSerializer):
    Yorum = SoruBankasıYorumSerializer(many=True, read_only=True)
    Puanlama = SoruBankasıPuanlamaSerializer(many=True, read_only=True)
    class Meta:
        model = SoruBankası
        fields = '__all__' 
########SoruBankası########


########YoutubeKanal########
class KanalYorumBeğeniSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanalYorumBeğeni
        fields = '__all__' 

class KanalYorumSerializer(serializers.ModelSerializer):
    YorumBeğeni = KanalYorumBeğeniSerializer(many=True, read_only=True)
    class Meta:
        model = KanalYorum
        fields = '__all__' 

class KanalPuanlamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanalPuanlama
        fields = '__all__' 

class KanalSerializer(serializers.ModelSerializer):
    Yorum = KanalYorumSerializer(many=True, read_only=True)
    Puanlama = KanalPuanlamaSerializer(many=True, read_only=True)    
    class Meta:
        model = Kanal
        fields = '__all__' 
########YoutubeKanal########


########BranşDenemesi########
class BranşDenemesiYorumBeğeniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranşDenemesiYorumBeğeni
        fields = '__all__' 

class BranşDenemesiYorumSerializer(serializers.ModelSerializer):
    YorumBeğeni = BranşDenemesiYorumBeğeniSerializer(many=True, read_only=True)
    class Meta:
        model = BranşDenemesiYorum
        fields = '__all__' 

class BranşDenemesiPuanlamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranşDenemesiPuanlama
        fields = '__all__' 

class BranşDenemesiSerializer(serializers.ModelSerializer):
    Yorum = BranşDenemesiYorumSerializer(many=True, read_only=True)
    Puanlama = BranşDenemesiPuanlamaSerializer(many=True, read_only=True)
    class Meta:
        model = BranşDenemesi
        fields = '__all__' 
########BranşDenemesi########


########GenelDeneme########
class GenelDenemeYorumBeğeniSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenelDenemeYorumBeğeni
        fields = '__all__' 

class GenelDenemeYorumSerializer(serializers.ModelSerializer):
    YorumBeğeni = GenelDenemeYorumBeğeniSerializer(many=True, read_only=True)
    class Meta:
        model = GenelDenemeYorum
        fields = '__all__' 

class GenelDenemePuanlamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenelDenemePuanlama
        fields = '__all__' 

class GenelDenemeSerializer(serializers.ModelSerializer):
    Yorum = GenelDenemeYorumBeğeniSerializer(many=True, read_only=True)
    Puanlama = GenelDenemePuanlamaSerializer(many=True, read_only=True)
    class Meta:
        model = GenelDeneme
        fields = '__all__'         