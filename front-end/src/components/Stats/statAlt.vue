<template>
<div class="mt-2 p-4">
    <div class="row">
         <h1>Aylık Yanlış/Boş Ders Grafiğiniz ve Deneme Sıralamalarınız</h1>
         <hr>
        <div class="col-lg-1 mt-3">
            <button class="button-7" @click="showBar">TYT</button>
        </div>
        <div class="col-lg-6 mt-3">
            <button class="button-7" @click="showBar">AYT</button>
        </div>
    </div>
    
    <div class="row">
        <div class="col-lg-5" v-if="showTYTBar  == true">
            Sosyal Bilimler ve Fen Bilimleri 2 ile çarpılarak oranlanmıştır.
            <Pie :chart-data="PieChartDers"/>
        </div>
        <div class="col-lg-5" v-if="showAYTBar  == true">
            <Pie :chart-data="PieChartaytDers"/>
        </div>
        <div class="col-2">

        </div>
        <div class="col-lg-5">
            <h3>Çözdüğünüz Denemelerden arayınız: </h3>
            <hr>
            <div class="mt-4 row">
                <div class="col-lg-2">
                    <h5>Kaynak:</h5>
                </div>
                <div class="col-lg-8">
                    <input class="formforresource" type="text" @keyup="arama" v-model="this.Deneme">
                </div>
                <div v-if="this.dataçekme == true">
                    <div v-for="book in searchbar" v-bind:key="book" class="aramakutusu" >
                        <button class="btn button-sm" @click="DenemeSeçildi(book)">{{book.isim}}</button>
                    </div>
                </div>   
                
            </div>
            <div class="d-flex justify-content-start mt-2">
                    <div v-for="n in this.adet" v-bind:key="n">
                        <button class="btn denemebtn btn-sm" @click="denemestat(n)">{{n}}</button>
                    </div>   
                </div>
            <div class="p-3 denemearkaplan" v-if="this.Göster == false">
                <div class="mb-5">
                    <h5>Deneme Sonucunuz:</h5>
                </div>
                <div class="mb-5">
                    <h5>Denemeyi Çözen kişi sayısı:</h5>
                </div>
                <div class="mb-5">
                    <h5>Bu ay çözenler içerisinde sıralamanız:</h5>
                </div>
                <div class="mb-5">
                    <h5>Genel çözenler içerisinde sıralamanız:</h5>
                </div>
            </div>
            <div class="p-3 denemearkaplan" v-if="this.Göster == true">
                <div class="mb-4">
                    <h5>Deneme Sonucunuz: {{test.net}}</h5>
                    <div class="bg-light">
                        <table>
                          <tr>
                            <th></th>
                            <th>Ders 1</th>
                            <th>Ders 2</th>
                            <th>Ders 3</th>
                            <th>Ders 4</th>
                          </tr>
                          <tr>
                            <td>Doğru</td>
                            <td>{{test.TRcor}}</td>
                            <td>{{test.SScor}}</td>
                            <td>{{test.Mcor}}</td>
                            <td>{{test.Scor}}</td>
                          </tr>
                          <tr>
                            <td>Yan&Boş</td>  
                            <td>{{test.TRwro}}</td>
                            <td>{{test.SSwro}}</td>
                            <td>{{test.Mwro}}</td>
                            <td>{{test.Swro}}</td>
                          </tr>
                        </table>
                    </div>
                </div>
                <div class="mb-4">
                    <h5>Denemeyi Çözen kişi sayısı: {{this.girenkişi}}</h5>
                </div>
                <div class="mb-4">
                    <h5>Bu ay çözenler içerisinde sıralamanız: {{this.sıra}}</h5>
                </div>
                <div class="mb-4">
                    <h5>Genel çözenler içerisinde sıralamanız: {{this.genelsıra}}</h5>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import {Pie} from 'vue-chartjs'
import {ArcElement, PointElement, LineElement, Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement, PointElement, LineElement)

export default {
    name: 'statAlt',
    components: {Pie},
    data() {
        return {
            alan: null,
            searchbar: {},
            ResetFilter: {},
            showTYTBar: true,
            showAYTBar: false,
            dataçekme: false,
            Deneme: null,
            adet: null,
            kullanıcı: null,
            Göster: false,
            girenkişi: null,
            sıra: null,
            genelsıra: null,
            test: {},
            PieChartDers: {
                labels: [
                'Türkçe',
                'Sosyal Bilimler',
                'Matematik',
                'Fen Bilimleri'
              ],
              datasets: []
            },
            PieChartaytDers: {
                labels: [
                'Edebiyat','Tarih', 'Coğrafya', 'Matematik','Fizik','Kimya','Biyoloji'
              ],
              datasets: []
            }
        }
    },
    mounted() {
        if( localStorage.getItem('kullanıcı') != '') {
            axios
                .get('/api/Kullanıcılar/' + localStorage.getItem('kullanıcı').slice(1, -1) + '/')
                .then( response=> {
                    this.kullanıcı = response.data
                    const TRyanlış = this.kullanıcı.KullanıcıTYTDenemeleri.map((item) =>{
                        return item.TRwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Myanlış = this.kullanıcı.KullanıcıTYTDenemeleri.map((item) =>{
                        return item.Mwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const SSyanlış = this.kullanıcı.KullanıcıTYTDenemeleri.map((item) =>{
                        return 2*item.SSwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Syanlış = this.kullanıcı.KullanıcıTYTDenemeleri.map((item) =>{
                        return 2*item.Swro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    this.PieChartDers.datasets.push({ 
                        data: [TRyanlış, SSyanlış, Myanlış, Syanlış],
                        backgroundColor: [
                          'rgb(255, 0, 0)',
                          'rgb(255, 255, 0)',
                          'rgb(0, 0, 255)',
                          'rgb(0, 255, 0)'
                        ],
                        hoverOffset: 4
                    })
                    const Edeb = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Edebwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Tar1 = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Tar1wro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Co1 = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Co1wro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Mat = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Matwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Fiz = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Fizwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Kim = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Kimwro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    const Biy = this.kullanıcı.KullanıcıAYTDenemeleri.map((item) =>{
                        return item.Biywro
                    }).reduce((partialSum, a) => partialSum + a, 0)
                    this.PieChartaytDers.datasets.push({ 
                        data: [Edeb, Tar1, Co1, Mat, Fiz, Kim, Biy],
                        backgroundColor: [
                          'rgb(255, 0, 0)',
                          'rgb(255, 255, 0)',
                          'rgb(0, 0, 255)',
                          'rgb(0, 255, 0)'
                        ],
                        hoverOffset: 4
                    })
                        })
        }
    },
    methods: {
        arama() {
            if(this.dataçekme == false) {
                axios
                .get('api/3/')
                .then( response => {
                    this.searchbar = response.data
                    this.ResetFilter = response.data})
                this.asd()
                this.searchbar = Object.values(this.searchbar).filter((post) => {
                  return post.isim.toLowerCase().includes(this.Deneme.toLowerCase())
                })
                this.dataçekme = true
            }
            else if(this.dataçekme == true && this.Deneme == '') {
                this.searchbar = null
            }
            else {
                this.asd()
                this.searchbar = Object.values(this.searchbar).filter((post) => {
                  return post.isim.toLowerCase().includes(this.Deneme.toLowerCase())
                })
                this.dataçekme = true
            }
        },
        asd() {
            this.searchbar = this.ResetFilter
        },
        DenemeSeçildi(book) {
            this.Deneme = book.isim
            this.alan = book.alan
            this.adet= book.adet
            this.dataçekme = false
        },
        denemestat(n) {
            if(this.alan == 1) {
                axios 
                    .get('/api/Kullanıcılar/Genel/TYTDeneme/')
                    .then( response => {
                        let BuDeneme = response.data.filter((item) => {
                            return (item.kaynak == this.Deneme && item.sayı == n)
                        })
                        let kullanıcıtesti = BuDeneme.filter((item) => {
                            return (item.kullanıcı == localStorage.getItem('kullanıcı').slice(1, -1))
                        })
                        let BuDenemeSıralama = BuDeneme.map((item) => {
                            return item.net 
                        })
                        let zaman = new Date().getMonth()
                        let BuDenemeBuAy = BuDeneme.filter((item) => {
                            return item.zaman == zaman
                        })
                        let BuDenemeBuAySıralama = BuDenemeBuAy.map((item) => {
                            return item.net 
                        })
                        this.girenkişi = BuDeneme.length
                        this.test = kullanıcıtesti[0]
                        let x = BuDenemeSıralama.sort(function(a, b){return b - a})
                        this.genelsıra = x.indexOf(this.test.net) + 1
                        let y = BuDenemeBuAySıralama.sort(function(a, b){return b - a})
                        this.sıra = y.indexOf(this.test.net) + 1
                    })
            }
            else if(this.alan == 2) {
                axios 
                    .get('/api/Kullanıcılar/Genel/AYTDeneme/')
                    .then( response => {
                        let x = response.data.filter((item) => {
                            return (item.kaynak == this.Deneme && item.sayı == n)
                        })
                        console.log(x)
                    })
            }
            this.Göster = true
        },
        showBar() {
            if(this.showTYTBar == true) {
                this.showTYTBar = false
                this.showAYTBar = true
            }
            else {
                this.showTYTBar = true
                this.showAYTBar = false
            }
        }
    }
}
</script>

<style>
.denemearkaplan {
    background-color: rgb(230,230,230);
    border-radius: 10px;
}
.denemebtn {
    padding-left: 10px;
    padding-right: 10px;
    margin-left: 8px;
    border-radius: 10px 10px 0px 0px;
    background-color: rgb(250,100,0);
    color: #fff;
    font-size: 16px;
    font-weight: 600;
}
table {

  border-collapse: collapse;
  width: 100%;
}
td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 3px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>