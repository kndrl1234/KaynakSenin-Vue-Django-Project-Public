<template>
    <div class="AddTYT">
        <div class="row">
            <div class="col-lg-4">
                <h4>Temel Yeterlilik Denemesi ekle</h4>
            </div>
            <div class="mt-1 col-lg-3">
                Kaynak: <input class="formforresource" type="text" @keyup="arama" v-model="this.Deneme">
                <div v-if="this.dataçekme == true">
                    <div v-for="book in searchbar" v-bind:key="book" class="aramakutusu" >
                        <button class="btn button-sm" @click="DenemeSeçildi(book)">{{book.isim}}</button>
                    </div>                
                </div>
            </div>
            <div class="mt-1 col-lg-4" v-if="this.adet != null">
                Deneme: <input class="formforresource" type="text" placeholder="1. deneme ise 1"  v-model="this.result.sayı">
            </div>
        </div>
        <form onsubmit="return send()">
        <div class="row mt-2">
            <div class="col-lg-3">
                <div class="row">
                    <div class="subjectname col-2">
                        <h5>Tr:</h5>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-6"><input type="number" class="formforresource"  min="0" max="40" v-model="this.result.TRcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource"  min="0" max="40" v-model="this.result.TRwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="row">
                    <div class="subjectname col-2">
                        <h5>Sos:</h5>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-6"><input type="number" class="formforresource"  min="0" max="20" v-model="this.result.SScor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="20" v-model="this.result.SSwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
                        <div class="col-lg-3">
                <div class="row">
                    <div class="subjectname col-2">
                        <h5>Mat:</h5>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="40" v-model="this.result.Mcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="40" v-model="this.result.Mwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="row">
                    <div class="subjectname col-2">
                        <h5>Fen:</h5>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-6"><input type="number" class="formforresource"  min="0" max="20" v-model="this.result.Scor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="20" v-model="this.result.Swro"></div>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
        <div class="mt-2 d-flex justify-content-center">
           <input type="submit" class="button-send" value="EKLE" @click="send">
        </div>
        </form>    
    </div>
</template>


<script>import axios from "axios"

export default {
    name: 'add_TYT',
    data() {
        return {
            searchbar: {},
            ResetFilter: {},
            dataçekme: false,
            showArama: false,
            Deneme: null,
            adet: null,
            result: {
                kullanıcı: localStorage.getItem('kullanıcı').slice(1, -1),
                net: null,
                TRcor: null,
                TRwro: null,
                SScor: null,
                SSwro: null,
                Mcor: null,
                Mwro: null,
                Scor: null,
                Swro: null,     
                sayı: null,
                kaynak: null,
                zaman: null
            }
        }
    },
    methods: {
        arama() {
            if(this.dataçekme == false) {
                axios
                .get('api/3/')
                .then( response => {
                    let x = response.data.filter((post) => {
                      return post.alan === 1
                    })
                    this.searchbar = x
                    this.ResetFilter = x})
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
            this.adet= book.adet
            this.dataçekme = false
        },
        send() {
            let send = true
            for(let i =0; i < 10; i++) {
                let x = document.getElementsByClassName("formforresource")[i].validity.valid
                if(x == false) {
                    send = false 
                }
            }
            if (send == true) {
                this.result.zaman = new Date().getMonth()
                let correct = this.result.TRcor +  this.result.SScor + this.result.Mcor + this.result.Scor
                let wrong = (this.result.TRwro + this.result.SSwro + this.result.Mwro + this.result.Swro)
                let sumwro = wrong / 4
                this.result.net = correct - sumwro
                this.result.TRwro = 40 - this.result.TRcor
                this.result.SSwro = 20 - this.result.SScor
                this.result.Mwro = 40 - this.result.Mcor
                this.result.Swro = 20 - this.result.Scor
                this.result.kaynak = this.Deneme
                axios
                    .post('/api/Kullanıcılar/Genel/TYTDeneme/', this.result)
                    .then(
                        alert('Deneme başarıyla eklendi'),
                        document.location.reload(true)
                    )
            }
        }
    }
}
</script>


<style>
.AddTYT{
    background-color: grey;
    border-radius: 10px;
    color: white;
    padding: 10px;
}
.formforresource{
    line-height:80%;
}
.subjectname {
    margin-top: -1px;
}
.aramakutusu {
    background-color: rgb(240,240,240);
    padding: 5px;
    color: black;
    border-radius: 3px;
}
.button-send {
  align-items: center;
  background-color: #fa6400;
  border: 1px solid transparent;
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 15px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  min-height: 1rem;
  padding: calc(.4rem - 1px) calc(1.5rem - 1px);
}
</style>