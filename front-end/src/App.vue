<template>
<div class="app">
<nav id="navbar" class="navbar navbar-expand-lg navbar-dark">
  <div class="container-fluid">
    <router-link to="/" ><button class="mainbtn navbar-brand"><img src="@/assets/3.png" alt=""></button></router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link to="/Kaynaklar" class="nav-link active">Kaynaklar</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/Gunlugum" class="nav-link active">Günlüğüm</router-link>
        </li>        
        <li class="nav-item">
          <router-link to="/Mesaj" class="nav-link active">İletişim</router-link>
        </li>
      </ul>
      <div class=" d-flex">
        <div v-if="kullanıcı == ''" class="">
        <button @click='handleSignIn' class="button-9">Google ile giriş</button>
        </div>
        <div v-if="kullanıcı != ''" class="mt-3 me-2 text-light">
        <h5>{{kullanıcı}}</h5>
        </div>        
        <div v-if="kullanıcı != ''" class="btn-group mt-1">
          <button type="button" class="btn button-9 dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
            İşlemler
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><button @click='HesapSil'  class="dropdown-item" type="button">Hesabı Sil</button></li>
            <li><button @click='handleSignOut'  class="dropdown-item" type="button">Çıkış</button></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</nav>

<router-view/>
<div class="footer mt-4">
  <div class="d-flex justify-content-center">
    -hello world-
  </div>
</div>
</div>
</template>

<script>
import {inject} from 'vue'
import axios from 'axios';
export default {
  name: 'App',
  data() {
    return {
      Vue3GoogleOauth: '',
      YeniKullanıcı: {
        yorum: '',
        isim: null,
        eposta: null
      },
      kullanıcı: localStorage.getItem('kullanıcı').slice(1, -1)
    }
  },
  methods: {
    async handleSignIn() {
        const googleUser = await this.$gAuth.signIn();
        localStorage.setItem("kullanıcı", JSON.stringify(googleUser.getBasicProfile().getEmail()))
        this.YeniKullanıcı.isim = JSON.stringify(googleUser.getBasicProfile().getName()).slice(1, -1)
        this.YeniKullanıcı.eposta = JSON.stringify(googleUser.getBasicProfile().getEmail()).slice(1, -1)
        this.YeniKullanıcı.yorum = JSON.stringify(googleUser.getBasicProfile().getImageUrl()).slice(1, -1)
        axios
          .post('/api/Kullanıcılar/', this.YeniKullanıcı)
          document.location.reload(true)
    },
    async handleSignOut() {
        await this.$gAuth.signOut();
        localStorage.setItem("kullanıcı", '')
        document.location.reload(true)
    },
    HesapSil() {
      var cevap = confirm("Hesabı silmek istediğinize emin misiniz?")
      if(cevap == true) {
        axios
        .delete('/api/Kullanıcılar/' + this.kullanıcı)
        .then(
          alert('Kullanıcı başarıyla silinmiştir'),
          this.$gAuth.signOut(),
          localStorage.setItem("kullanıcı", ''),
          document.location.reload(true)
        )
      }
    }
  },
  created() {
    this.Vue3GoogleOauth = inject('Vue3GoogleOauth');
  },
}
</script>

<style>
.app {
  background-color: rgb(10,10,10);
}
.mainbtn {
  margin-left: 10px;
  background-color: rgb(20,20,20);
  border-radius: 10px;
  border-color: rgb(250, 120,0);
  border-width: 5px;
}
#navbar {
  padding-right: 20px;
  background-color: rgb(20,20,20);
}
.sign {
  margin-left:20px;
  background-color: rgb(250, 120,0);
  border-radius: 30px;
}
.rtrlnk {
  color: white;
  text-decoration: none;
}
.button-9 {
  align-items: center;
  background-clip: padding-box;
  background-color: #fa6400;
  border: 1px solid transparent;
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;  
  line-height: 1.25;
  margin-left: 10px;
  min-height: 1rem;
  padding: calc(.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}
</style>
