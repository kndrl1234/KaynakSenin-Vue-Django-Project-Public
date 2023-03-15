
from django.db import models
from PIL import Image

class Mesaj(models.Model):
    anaKonu = models.CharField(max_length=100 ,null=True, blank=True)
    başlık = models.CharField(max_length=200, null=True, blank=True)
    mesaj = models.TextField(null=True, blank=True)

########Parametre########
class Tür(models.Model):
    Tür = models.CharField(max_length=20)
    def __str__(self):
        return self.Tür

class Alan(models.Model):
    Alan = models.CharField(max_length=10)
    def __str__(self):
        return self.Alan

class Ders(models.Model):
    Ders = models.CharField(max_length=30)
    def __str__(self):
        return self.Ders
########Parametre########


########Kullanıcı########
class Kullanıcı(models.Model):
    fotoUrl: models.TextField(null=True, blank=True)
    yorum = models.TextField(null=True,blank=True)
    isim = models.CharField(max_length=200)
    eposta = models.EmailField(primary_key=True)
    def __str__(self):
        return self.eposta    

class KullanıcıTYTDeneme(models.Model):
    kullanıcı = models.ForeignKey(Kullanıcı, on_delete=models.CASCADE, related_name='KullanıcıTYTDenemeleri')
    net = models.DecimalField(max_digits=10, decimal_places=2)
    TRcor = models.IntegerField(null=True,blank=True)
    TRwro = models.IntegerField(null=True,blank=True)
    SScor = models.IntegerField(null=True,blank=True)
    SSwro = models.IntegerField(null=True,blank=True)
    Mcor = models.IntegerField(null=True,blank=True)
    Mwro = models.IntegerField(null=True,blank=True)
    Scor = models.IntegerField(null=True,blank=True)
    Swro = models.IntegerField(null=True,blank=True)
    kaynak = models.TextField(null=True,blank=True)
    sayı = models.TextField(null=True,blank=True)
    zaman = models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.kullanıcı)       

class KullanıcıAYTDenemeleri(models.Model):
    kullanıcı = models.ForeignKey(Kullanıcı, on_delete=models.CASCADE, related_name='KullanıcıAYTDenemeleri')
    yanlış = models.IntegerField(null=True,blank=True)
    net = models.DecimalField(max_digits=10, decimal_places=2)
    Edebcor = models.IntegerField(null=True,blank=True)
    Edebwro = models.IntegerField(null=True,blank=True)
    Tar1cor = models.IntegerField(null=True,blank=True)
    Tar1wro = models.IntegerField(null=True,blank=True)
    Co1cor = models.IntegerField(null=True,blank=True)
    Co1wro = models.IntegerField(null=True,blank=True)
    Matcor = models.IntegerField(null=True,blank=True)
    Matwro = models.IntegerField(null=True,blank=True)
    Fizcor = models.IntegerField(null=True,blank=True)
    Fizwro = models.IntegerField(null=True,blank=True)
    Kimcor = models.IntegerField(null=True,blank=True)
    Kimwro = models.IntegerField(null=True,blank=True)
    Biycor = models.IntegerField(null=True,blank=True)
    Biywro = models.IntegerField(null=True,blank=True)
    kaynak = models.TextField(null=True,blank=True)
    sayı = models.TextField(null=True,blank=True)
    zaman = models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.kullanıcı)     

########Kullanıcı########


########SoruBankası########
class SoruBankası(models.Model):
    tür = models.ForeignKey(Tür, on_delete=models.SET_NULL, null=True)
    ders = models.ForeignKey(Ders, on_delete=models.SET_NULL, null=True)
    alan = models.ForeignKey(Alan, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(null=True, blank=True)
    isim = models.CharField(max_length=100, primary_key=True)
    yayın = models.CharField(max_length=100)
    soru_adet =  models.PositiveIntegerField(blank=True,null=True)
    satın_link = models.TextField(blank=True,null=True)
    fiyat = models.PositiveIntegerField(blank=True,null=True)
    sayfa = models.IntegerField(blank=True,null=True)
    video_çözüm = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class SoruBankasıYorum(models.Model):
    Yorum = models.TextField()
    kaynak = models.ForeignKey(SoruBankası, on_delete=models.CASCADE, related_name='Yorum')
    sahip = models.CharField(max_length=100)
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return str(self.id)

class SoruBankasıYorumBeğeni(models.Model):
    Yorum = models.ForeignKey(SoruBankasıYorum, on_delete=models.CASCADE, related_name='YorumBeğeni')
    sahip = models.CharField(max_length=100)
    like = models.BooleanField()
    zaman = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.zaman

class SoruBankasıPuanlama(models.Model):
    öğretici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    deneyici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    sahip = models.CharField(max_length=100)
    kaynak = models.ForeignKey(SoruBankası, on_delete=models.CASCADE, related_name='Puanlama')
    def __str__(self):
        return str(self.kaynak)
########SoruBankası########


########YoutubeKanal########
class Kanal(models.Model):
    tür = models.ForeignKey(Tür, on_delete=models.SET_NULL, null=True)
    youtube_id = models.CharField(max_length=100)
    isim = models.CharField(max_length=100, primary_key=True)
    Ders = models.ForeignKey(Ders, on_delete=models.SET_NULL, null=True)  
    def __str__(self):
        return self.isim


class KanalYorum(models.Model):
    Yorum = models.TextField()
    kaynak = models.ForeignKey(Kanal, on_delete=models.CASCADE, related_name='Yorum')
    sahip = models.CharField(max_length=100)
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return str(self.id)

class KanalYorumBeğeni(models.Model):
    Yorum = models.ForeignKey(KanalYorum, on_delete=models.CASCADE, related_name='YorumBeğeni')
    sahip = models.CharField(max_length=100, primary_key=True)
    like = models.BooleanField()
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.sahip

class KanalPuanlama(models.Model):
    öğretici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    deneyici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    sahip = models.CharField(max_length=100)
    kaynak = models.ForeignKey(Kanal, on_delete=models.CASCADE, related_name='Puanlama')
    def __str__(self):
        return str(self.kaynak)
########YoutubeKanal########


########BranşDenemesi########
class BranşDenemesi(models.Model):
    tür = models.ForeignKey(Tür, on_delete=models.SET_NULL, null=True)
    isim = models.CharField(max_length=100, primary_key=True)
    yayın = models.CharField(max_length=30)
    foto = models.ImageField(null=True, blank=True)
    ders = models.ForeignKey(Ders, on_delete=models.SET_NULL, null=True)  
    alan = models.ForeignKey(Alan, on_delete=models.SET_NULL, null=True)
    adet =  models.PositiveIntegerField(blank=True,null=True)
    fiyat = models.PositiveIntegerField(blank=True,null=True)
    video_çözüm = models.CharField(max_length=100)
    satın_link = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.isim

class BranşDenemesiYorum(models.Model):
    Yorum = models.TextField()
    kaynak = models.ForeignKey(BranşDenemesi, on_delete=models.CASCADE, related_name='Yorum')
    sahip = models.CharField(max_length=100)
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return str(self.id)

class BranşDenemesiYorumBeğeni(models.Model):
    Yorum = models.ForeignKey(BranşDenemesiYorum, on_delete=models.CASCADE, related_name='YorumBeğeni')
    sahip = models.CharField(max_length=100, primary_key=True)
    like = models.BooleanField()
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.sahip

class BranşDenemesiPuanlama(models.Model):
    öğretici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    deneyici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    sahip = models.CharField(max_length=100)
    kaynak = models.ForeignKey(BranşDenemesi, on_delete=models.CASCADE, related_name='Puanlama')
    def __str__(self):
        return str(self.kaynak)
########BranşDenemesi########


########GenelDeneme########
class GenelDeneme(models.Model):
    tür = models.ForeignKey(Tür, on_delete=models.SET_NULL, null=True)
    isim = models.CharField(max_length=100, primary_key=True)
    yayın = models.CharField(max_length=30)
    foto = models.ImageField(null=True, blank=True) 
    alan = models.ForeignKey(Alan, on_delete=models.SET_NULL, null=True)
    adet =  models.PositiveIntegerField(blank=True,null=True)
    fiyat = models.PositiveIntegerField(blank=True,null=True)
    video_çözüm = models.CharField(max_length=100)
    satın_link = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.isim


class GenelDenemeYorum(models.Model):
    Yorum = models.TextField()
    kaynak = models.ForeignKey(GenelDeneme, on_delete=models.CASCADE, related_name='Yorum')
    sahip = models.CharField(max_length=100)
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return str(self.id)

class GenelDenemeYorumBeğeni(models.Model):
    Yorum = models.ForeignKey(GenelDenemeYorum, on_delete=models.CASCADE, related_name='YorumBeğeni')
    sahip = models.CharField(max_length=100, primary_key=True)
    like = models.BooleanField()
    zaman = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.sahip

class GenelDenemePuanlama(models.Model):
    öğretici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    deneyici = models.DecimalField(blank=True,null=True, max_digits=2, decimal_places=1)
    sahip = models.CharField(max_length=100)
    kaynak = models.ForeignKey(GenelDeneme, on_delete=models.CASCADE, related_name='Puanlama')
    def __str__(self):
        return str(self.kaynak)
########GenelDeneme########
