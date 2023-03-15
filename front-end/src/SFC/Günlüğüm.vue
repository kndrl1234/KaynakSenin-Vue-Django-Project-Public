<template>
<title>Verilerim - KaynakSenin</title>
<div class="lightbg">
    <div class="container mydiary">
        <h2>Günlüğüm</h2>
        <button class="button-7" @click="showStat">Verilerim</button>
        <button class="button-7" @click="showTest">Deneme Ekle</button>
        <button class="button-7" @click="Genelİstatistik">Genel İstatistik</button>         
        <hr>

        <div class="maindiary">
            <div v-if="IsTestOpen == true">
                <p>Kaynağı çözmüş diğer kişilerin istatistikleri için kaynağın ismini girmeniz gerekir. Eğer kaynak yok ise
                kaynağın adını yazıp bırakın biz ekleriz.  
                </p>
                <div  class="mt-4">
                    <add_TYT></add_TYT>
                </div>     
                <div  class="mt-2">
                    <add_AYT></add_AYT>
                </div>              
            </div>
            <div v-if="this.kullanıcı == false">
                <NoLog></NoLog>
            </div>
            <div v-if="this.kullanıcı == true">
                <stats></stats>
            </div>
        </div>         
    </div>
</div>
</template>

<script>
import add_AYT from '@/components/Diary/add_AYT.vue'
import add_TYT from '@/components/Diary/add_TYT.vue'
import NoLog from '@/components/Diary/NoLog.vue'
import stats from '@/components/Diary/stats.vue'
export default {
    name: "Günlüğüm",
    components: {add_AYT, add_TYT,stats,NoLog},    
    data() {
        return {
        kullanıcı: false,
        IsTestOpen: false,
        }
    },
    mounted() {
        if(localStorage.getItem('kullanıcı') != '') {
            this.kullanıcı = true
        }
    },
    methods: {
        showStat() {
            this.IsTestOpen = false
        },
        showTest() {
            if(this.kullanıcı == false) {
                alert('Giriş yapmanız gerekiyor')
            }
            else if(this.kullanıcı == true) {
                if(this.IsTestOpen == true) {
                this.IsTestOpen = false
                }
                else {
                    this.IsTestOpen = true
                }   
            }
        },
        Genelİstatistik() {
            alert('Genel İstatistiklerin gelmesi için önce sitenin büyümesi gerek')
        }
    }    
}
</script>


<style>
.lightbg {
    background-image: linear-gradient(rgba(170,170,170), rgba(220,220,220));
    padding: 30px;
}
.mydiary {
    background-color: rgb(248,240,240);
    font-family: Calibri;
    border-radius: 10px;
    padding: 10px;
}
.maindiary {
    background-color: white;
    border-radius: 10px;
    padding: 10px;
}
</style>

