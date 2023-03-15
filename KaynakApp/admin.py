
from django.contrib import admin
from KaynakApp.models import Mesaj,Tür,Alan,Ders,Kullanıcı,KullanıcıTYTDeneme,KullanıcıAYTDenemeleri
from KaynakApp.models import SoruBankası,SoruBankasıYorum,SoruBankasıYorumBeğeni,SoruBankasıPuanlama
from KaynakApp.models import Kanal,KanalYorum,KanalYorumBeğeni,KanalPuanlama,BranşDenemesi,BranşDenemesiYorum,BranşDenemesiYorumBeğeni
from KaynakApp.models import BranşDenemesiPuanlama,GenelDeneme,GenelDenemeYorum,GenelDenemeYorumBeğeni,GenelDenemePuanlama

admin.site.register(Mesaj)
admin.site.register(Tür)
admin.site.register(Alan)
admin.site.register(Ders)
admin.site.register(Kullanıcı)
admin.site.register(KullanıcıTYTDeneme)
admin.site.register(KullanıcıAYTDenemeleri)
admin.site.register(SoruBankası)
admin.site.register(SoruBankasıYorum)
admin.site.register(SoruBankasıYorumBeğeni)
admin.site.register(SoruBankasıPuanlama)
admin.site.register(Kanal)
admin.site.register(KanalYorum)
admin.site.register(KanalYorumBeğeni)
admin.site.register(KanalPuanlama)
admin.site.register(BranşDenemesi)
admin.site.register(BranşDenemesiYorum)
admin.site.register(BranşDenemesiYorumBeğeni)
admin.site.register(BranşDenemesiPuanlama)
admin.site.register(GenelDeneme)
admin.site.register(GenelDenemeYorum)
admin.site.register(GenelDenemeYorumBeğeni)
admin.site.register(GenelDenemePuanlama)
