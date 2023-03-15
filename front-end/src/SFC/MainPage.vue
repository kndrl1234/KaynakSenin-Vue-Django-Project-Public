<template>
<title>KaynakSenin - YKS kaynak Veritabanı</title>
<div class="MainTop row">
    <div class="carousel col-xl-8 col-lg-12">
        <carousel></carousel>
    </div>
    <div class="promotion col-xl-4 col-lg-12">
        <promotion></promotion>
    </div>
</div>
<div class="book_list">
    
    <source_list 
        h3="Soru Bankaları"
        spn="Öğrendiklerinizi pekiştirin, daha iyisi için eksiklerinizi bulun"
        fromhomepage= '1'
        ders=""
        publisher1="Acil AYT Matematik"
        publisher2="Soru Bankası 1"
        publisher3="Soru Bankası 2"
        publisher4="Soru Bankası 3"
        publisher5="Soru Bankası 4"
        publisher6="Soru Bankası 5"
        publisher7="Soru Bankası 6"
        publisher8="Soru Bankası 7"
        publisher9="Soru Bankası 8"
        publisher10="Soru Bankası 9"
    />
    <source_list 
        h3="Ders Kanalları"
        spn="Modern eğitim ne bir kitapta ne de bir okulda."  
        fromhomepage="2"  
        ders=""
        publisher1=""
        publisher2=""
        publisher3=""
        publisher4=""
        publisher5=""
        publisher6=""
        publisher7=""
        publisher8=""
        publisher9=""
        publisher10=""
    />
    <source_list
        h3="Alan Denemeleri"
        spn="Bir alana ait bilgilerinizi karma konularla sınayın"
        fromhomepage="4"
        ders=""
        publisher1=""
        publisher2=""
        publisher3=""
        publisher4=""
        publisher5=""
        publisher6=""
        publisher7=""
        publisher8=""
        publisher9=""
        publisher10=""
    />
    <source_list 
        h3="Genel Denemeler"
        spn="Sınav stresini yenmenin en iyi yolu sınava her gün girmektir"
        fromhomepage="3"
        ders=""
        publisher1=""
        publisher2=""
        publisher3=""
        publisher4=""
        publisher5=""
        publisher6=""
        publisher7=""
        publisher8=""
        publisher9=""
        publisher10=""  
    />
    <source_list 
        h3="Matematik Soru Bankaları"
        spn="Piyasadaki en dikkat çeken matematik kitapları"
        fromhomepage="1"
        ders="1"
        publisher1=""
        publisher2=""
        publisher3=""
        publisher4=""
        publisher5=""
        publisher6=""
        publisher7=""
        publisher8=""
        publisher9=""
        publisher10=""  
    />
    <source_list 
        h3="Fizik Soru Bankaları"
        spn="Piyasadaki en dikkat çeken fizik kitapları"
        fromhomepage="1"
        ders="2"
        publisher1=""
        publisher2=""
        publisher3=""
        publisher4=""
        publisher5=""
        publisher6=""
        publisher7=""
        publisher8=""
        publisher9=""
        publisher10=""  
    />
</div>

</template>

<script>
import carousel from '@/components/MainPage/carousel.vue'
import promotion from '@/components/MainPage/promotion.vue'
import source_list from '@/components/MainPage/source_list.vue'

export default {
    name: "MainPage",
    components: {carousel, promotion, source_list},
}
</script>

<style>
.MainTop {
    margin: auto
}
.carousel {
    margin-top: 6px; 
}
.promotion {
    margin-top:10px;
}

</style>