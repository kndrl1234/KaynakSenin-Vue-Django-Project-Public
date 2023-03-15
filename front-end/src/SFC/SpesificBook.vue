<template>
<title>{{Book.isim}}</title>
<div class="lightbg">
  
  <div class="container">
    <div class="spesificbook row mb-4">
      <h3>{{Book.isim}}</h3>
      <p>Bu sayfa {{Book.yayın}}'larının kitabı için genel sayfadır, puanlamalar yalnızca bu seneye ait değildir.</p>
      <label>Versiyonlar: <a href="">2023</a></label>
      <div class="col-lg-1"></div>
      <div class="mt-5 col-lg-3">
        <img v-bind:src="Book.foto" width="220"/>
        <img v-bind:src="this.kanal.foto" width="220"/>
      </div>
      <div class="col-lg-1"></div>
      <div class="info mt-4 p-3 col-lg-7"> 
        <div class="m-1">
          <label>Yayınevi:</label><a href="">&nbsp;{{Book.yayın}}</a>
        </div>
        <div class="m-1">
          <label for="">Fiyatı: {{Book.fiyat}}</label>
        </div>
        <div v-if="this.tür == '1'" class="m-1">
          <label for="">Soru Sayısı: {{Book.soru_adet}}</label>
        </div>
        <div v-if="this.tür == '1'" class="m-1">
          <label for="">Sayfa Sayısı: {{Book.sayfa}}</label>
        </div>
        <div v-if="this.tür == '2'" class="m-1">
          <label for="">Abone Sayısı:{{this.kanal.abone}}</label>
        </div>
        <div v-if="this.tür == '2'" class="m-1">
          <label for="">Video Sayısı:{{this.kanal.video}}</label>
        </div>
        <div v-if="this.tür == '3' || this.tür == '4'" class="m-1">
          <label for="">Deneme Sayısı: {{Book.adet}}</label>
        </div>
        <div class="m-1">
          <label for="">Satın almak için: <a >{{Book.satın_link}}</a></label>
        </div>
        <div class="m-1">
          <label for="">Video Çözüm: <a v-bind:href="Book.video_çözüm">{{Book.video_çözüm}}</a></label>
        </div>
        <div class="row mt-2">
          <div class="col-lg-3 m-1">
            <h6>Öğretici Puanı:</h6>
          </div>
          <div class="col-lg-8">
            <star-rating v-model:rating="this.Öğretici" :star-size="20" text-class="custom-text" :max-rating="10" :increment="0.1"></star-rating>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-3 m-1">
            <h6>Deneyici Puanı:</h6>
          </div>
          <div class="col-lg-8">
            <star-rating v-model:rating="this.Deneyici" :star-size="20" text-class="custom-text" :max-rating="10" :increment="0.1"></star-rating>
          </div>
        </div>
        <div class="row mt-4 d-flex justify-content-center">
          <div class="col-lg-4">
            <h6>Öğretici Puanı</h6>
           <h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{this.Ö}}/10 <i class="bi icon bi-star-fill "></i></h5> 
          </div>
          <div class="col-lg-3">
            <h6>Deneyici Puanı</h6>
            <h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{this.D}}/10 <i class="bi icon bi-star-fill "></i></h5>
          </div>
        </div>
      </div>
    </div>
    <div class="spesificbook row">
      <div class="p-1">
        <h5>Yorum Yaz:</h5>
        <p>{{kullanıcı}}</p>
        <textarea class="form-control" aria-label="With textarea" v-model="Yorum.Yorum"></textarea>
        <div class="d-flex justify-content-end  ">
            <button class="btn commentbtn m-2" @click="yorumYap">Gönder</button>
        </div>
      </div>
      <hr>
      <div v-for="(yorum) in this.Book.Yorum" v-bind:key="(yorum)" class="">
        <div class="m-2 p-3 comment">
          <div class="row">
            <div class="col-4 mt-2">
              <h6>{{yorum.sahip}}</h6> 
            </div>
            <div class="col-lg-6"></div>
            <div class="col-lg-1 mt-2">{{yorum.zaman}}</div>
            <div class="col-1"  v-if="this.kullanıcı == yorum.sahip">
              <button class="btn" @click="yorumayrıntı(yorum)"><i class="bi icon bi-three-dots-vertical"></i></button>
              <div class="div" v-if="this.yorumdüzenlegöster == true && this.yorumdüzenlespes == yorum.id">
                <div class="d-flex justify-content-end">
                  <button class="btn commentbtn m-2" @click="yorumdüzenle(yorum)">Düzenle</button>
                  <button class="btn commentbtn m-2" @click="yorumsil(yorum)">Sil</button>                  
                </div>
              </div>
            </div>
          </div>
          <hr class="commenthr">
          <div class="m-3"> 
            {{yorum.Yorum}}
          </div>
          <div v-if="düzenleme == yorum.id" class="c">
            <h6>Düzenle:</h6>
            <textarea class="form-control" aria-label="With textarea" v-model="YeniYorum.Yorum"></textarea>
            <div class="d-flex justify-content-end">
                <button class="btn commentbtn m-2" @click="düzenle(yorum)">Düzenle</button>
                <button class="btn commentbtn m-2" @click="iptal">İptal</button>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-10">
              
            </div>
            <div class="col-lg-1">
              <button class="commentbutton" @click="change()"><i class="bi icon bi-hand-thumbs-up"></i></button>
            </div>
            <div class="col-lg-1">
              <button class="commentbutton" @click="change()"><i class="bi icon bi-hand-thumbs-down"></i></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
export default {
  name: 'SpesificBook',
  components: {StarRating},
  data() {
    return {
      tür: null,
      yeniPuanlama: false,
      düzenleme: null,
      yorumdüzenlegöster: false,
      yorumdüzenlespes: null,
      yorumdüzen: false,
      kullanıcı: localStorage.getItem('kullanıcı').slice(1, -1),
      Book: {},
      Yorumlar: {},
      kişi: {},
      kanal: {
        abone: null,
        video: null,
        foto: null
      },
      Deneyici: null,
      Öğretici: null,
      D: null,
      Ö: null,
      Puanlama: {
        deneyici: null,
        öğretici: null,
        kaynak: null,
        sahip: localStorage.getItem('kullanıcı').slice(1, -1)
      },
      Yorum: {
        Yorum: null,
        kaynak: null,
        sahip: localStorage.getItem('kullanıcı').slice(1, -1),
        like: 0,
        dislike: 0,
        zaman: null,
      },
      YeniYorum: {
        id: null,
        Yorum: null,
        kaynak: null,
        sahip: localStorage.getItem('kullanıcı').slice(1, -1),
        like: 0,
        dislike: 0,
        zaman: null,
      },
      YorumBeğeni: {
        Yorum: null,
        zaman: null,
        like: null,
        sahip: null,
      },
      KitapLinki: null,
      id: null,
    }
  },
  mounted() {
    let KitapLinki = document.location.pathname.substring(1);
    this.tür = document.location.pathname.substring(1).slice(0,1)
    axios 
      .get('api/' + KitapLinki)
      .then(response =>{
        this.Book = response.data
        let x = this.Book.Puanlama.filter((post) => {
          return (post.kaynak == decodeURI(KitapLinki.slice(4)))
        })
        let puan1 = x.map((item) => {
          return Number(item.öğretici)
        })
        this.Ö = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)
        let puan2 = x.map((item) => {
          return Number(item.deneyici)
        })
        this.D = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)
        let f = x.filter((post) => {
          return post.sahip == localStorage.getItem('kullanıcı').slice(1, -1)
        })
        if(f[0] != undefined) {
          this.kişi= f[0]
          this.Öğretici = this.kişi.öğretici
          this.Deneyici = this.kişi.deneyici
          this.yeniPuanlama = true
        }
    })  
    if(this.tür == '2') {
      axios
        .get('https://youtube.googleapis.com/youtube/v3/channels?part=statistics&part=snippet&id='+ this.Book.youtube_id + '&key=AIzaSyDEpVAxdFRgsCF-N4WhX8GpLiFKNxy5XoA')
        .then(response=> {
          this.kanal.abone = response.data.items[0].statistics.subscriberCount
          this.kanal.video = response.data.items[0].statistics.videoCount
          this.kanal.foto = response.data.items[0].snippet.thumbnails.medium.url
        })
    }
  },
  watch : {
    Deneyici(Yeni) {
      if(Yeni) {
        if(this.yeniPuanlama == false) {
          this.Puanlama.deneyici = this.Deneyici
          this.Puanlama.kaynak = this.Book.isim
          axios
            .post('/api/' + document.location.pathname.substring(1).slice(0,1) + '/Genel/Puanlar/', this.Puanlama)
            .then(
              response => {
                this.id = response.data.id
                this.yeniPuanlama = true
              }
            )
        }
        else if(this.yeniPuanlama == true && this.id != null) {
          this.Puanlama.deneyici = this.Deneyici
          this.Puanlama.öğretici = this.Öğretici
          this.Puanlama.kaynak = this.Book.isim
          axios
            .patch('/api/' + document.location.pathname.substring(1).slice(0,1) + '/Genel/Puanlar/' + this.id, this.Puanlama)
        }
        else if(this.yeniPuanlama == true && this.id == null) {
          this.Puanlama.deneyici = this.Deneyici
          this.Puanlama.öğretici = this.Öğretici
          this.Puanlama.kaynak = this.Book.isim
          axios
            .patch('/api/' + document.location.pathname.substring(1).slice(0,1) + '/Genel/Puanlar/' + this.kişi.id, this.Puanlama)
        }
      }
    },
    Öğretici(Yeni) {
      if(Yeni) {
        if(this.yeniPuanlama == false) {
          this.Puanlama.öğretici = this.Öğretici
          this.Puanlama.kaynak = this.Book.isim
          axios
            .post('/api/' + document.location.pathname.substring(1).slice(0,1) + '/Genel/Puanlar/', this.Puanlama)
            .then(
              response => {
                this.id = response.data.id
                this.yeniPuanlama = true
              }
            )
        }
        else if(this.yeniPuanlama == true && this.id != null) {
          this.Puanlama.öğretici = this.Öğretici
          this.Puanlama.deneyici = this.Denetleyici
          this.Puanlama.kaynak = this.Book.isim
          axios
            .patch('/api/' + document.location.pathname.substring(1).slice(0,1) + '/Genel/Puanlar/' + this.id, this.Puanlama)
        }
        else if(this.yeniPuanlama == true && this.id == null) {
          this.Puanlama.öğretici = this.Öğretici
          this.Puanlama.deneyici = this.Denetleyici
          this.Puanlama.kaynak = this.Book.isim
          axios
            .patch('/api/' + document.location.pathname.substring(1).slice(0,1) + '/Genel/Puanlar/' + this.kişi.id, this.Puanlama)
        }
      }
    },
  },
  methods: {
    yorumYap() {
      let x = new Date().getMonth()
      let y = new Date().getFullYear()
      this.Yorum.zaman = (x + '/' + y)        
      this.Yorum.kaynak = this.Book.isim
      if(localStorage.getItem('kullanıcı') != '') {
        axios.
          post('/api/'+ this.Book.tür +'/Genel/Yorumlar/', this.Yorum)
          .then(
            document.location.reload(true)
          )
      }
      else {
        alert('Yorum Yapabilmek için Giriş Yapınız!')
      }
    },
    yorumayrıntı(yorum) {
      if(this.yorumdüzenlegöster == true) {
        this.yorumdüzenlegöster = false
      }
      else {
        this.yorumdüzenlegöster = true
        this.yorumdüzenlespes = yorum.id
      }
    
    },
    yorumdüzenle(yorum) {
      this.yorumdüzenlegöster = false
      this.yorumdüzen = true
      this.düzenleme = yorum.id
    },
    yorumsil(yorum) {
      this.yorumdüzenlegöster = false
      axios
        .delete('/api/' + this.Book.tür + '/Genel/Yorumlar/' + yorum.id)
        .then(
          document.location.reload(true)
        )
    },
    iptal() {
      this.düzenleme = false
    },
    düzenle(yorum) {
      let x = (new Date().getMonth() + 1)
      let y = new Date().getFullYear()
      this.YeniYorum.id = yorum.id
      this.YeniYorum.zaman = (x + '/' + y)        
      this.YeniYorum.kaynak = this.Book.isim
      axios
        .patch('/api/' + this.Book.tür + '/Genel/Yorumlar/' + yorum.id + '/', this.YeniYorum)
        .then(
          document.location.reload(true)
        )
    },
  } 
}
</script>

<style>
.icon {
  color: #fa6400;
}
.spesificbook {
  margin-top: 10px;
  color: rgb(110,70,70);
  background-color: white;
  border-radius: 5px;
  padding: 10px;
}
.info {
  background-color: rgb(240, 240, 240);
  border-radius: 10px;
}
.comment {
  background-color: rgb(240, 240, 240);
  border-radius: 10px;
}
.commentbutton {
  border: 0px;
}
.commentbtn {
  background-color: #fa6400; 
  color: white;
}
.commenthr {
  margin: 5px;
}
.PuanlamaBTN {
  border: 0px;
  margin-top: -5px;
}
</style>
