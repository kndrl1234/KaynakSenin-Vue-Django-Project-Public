<template>
<div class="books card">
  <img v-bind:src="this.kaynak.foto" height="200"  class="card-img-top" v-bind:alt="this.kaynak.isim" />
  <div class="d-flex justify-content-center text-light ratingbaşlık  mt-2">
    {{this.kaynak.isim}}
  </div>
  <div class="card-body">
    <div class="row text-light">
      <div class="col-6 ratingbaşlık">
        Öğretici Puanı
      </div>
      <div class="col-6 ratingbaşlık">
        Zorluk Puanı
      </div>
    </div>
    <div class="row text-light">
      <div class="col-1"></div>
      <div class="col-5 d-flex flex-row" id="ratingleft">
        <i class="bi bi-star-fill icon"></i>
        <h4 class="cardrating">{{Ö}}</h4>
      </div>
      <div class="col-5 d-flex flex-row" id="ratingright">
        <i class="bi bi-star-fill icon"></i>
        <h4 class="cardrating">{{D}}</h4>
      </div>
    </div>
    <div class="mt-2">
      <router-link :to="{ name: 'SpesificBook', params: { name: fromhomepage + '/' + name }}" class="nav-link active"><button class="btn cardbtn btn-sm">Kaynak Hakkında</button></router-link>
    </div>
    
  </div>
</div>
</template>

<script>
import axios from 'axios'


export default {
  name: "card",
  props: ['name', 'ders', 'fromhomepage', 'isim'],
  data() {
    return {
      kaynak: {},
      Ö: null,
      D: null
    }
  },  
  mounted() {
    axios
      .get('/api/' + this.fromhomepage + '/' + this.name)
      .then( response => {
        this.kaynak = response.data
        let puan1 = this.kaynak.Puanlama.map((item) => {
          return Number(item.öğretici)
        })
        this.Ö = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)
        let puan2 = this.kaynak.Puanlama.map((item) => {
          return Number(item.deneyici)
        })
        this.D = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)
      })
  }
}
</script>


<style>
.books {
  white-space: normal; 
  margin: 30px;
  display: inline-block;
  background-color: rgb(25,25,25);
  height:350px;
  width:200px;   
}
#ratingleft{
 margin-left: -15px;
}
#ratingright{
margin-left: 10px;
}
.cardrating {
  margin-left: 3px;
  font-size: 24px;
}
.ratingbaşlık {
  font-size: 11px;
  font-weight: 600;
}
.cardbtn {
  align-items: center;
  background-clip: padding-box;
  background-color: rgb(250,100,0);
  border: 1px solid transparent;
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 14px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 1rem;
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}
.cardbtn:hover,
.cardbtn:focus {
  background-color: #fb8332;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
}

</style>

