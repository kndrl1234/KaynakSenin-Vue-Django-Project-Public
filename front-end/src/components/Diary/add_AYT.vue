<template>
    <div class="AddTYT">
        <form onsubmit="return send()">
            <div class="row">
            <div class="col-lg-4">
                <h4>Alan Yeterlilik Denemesi ekle</h4>
            </div>
            <div class="mt-1 col-lg-3">
                Kaynak: <input class="formforresource" type="text" @keyup="arama" v-model="this.Deneme">
                <div v-if="this.dataçekme == true">
                    <div v-for="book in searchbar" v-bind:key="book" class="aramakutusu" >
                        <button class="btn button-sm" @click="DenemeSeçildi(book)">{{book.isim}}</button>
                    </div>                
                </div>
            </div>
            <div class="mt-1 col-lg-3" v-if="this.adet != null">
                Deneme: <input class="formforresource" type="text" placeholder="1. deneme ise 1" v-model="this.result.sayı">
            </div>
            <div class="mt-1 col-lg-2">
                Alan:  
                <select class="formforresource" name="" id="" v-model="this.branch">
                    <option value="1">Eşit Ağırlık</option>
                    <option value="2">Sayısal</option>                
                </select>
            </div>
        </div>
        <div class="row mt-2" v-if="this.branch == '1'">
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Edebiyat</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="24" style="width: 60px" v-model="this.result.Edebcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="24" style="width: 60px" v-model="this.result.Edebwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Tarih-1</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="10" style="width: 60px" v-model="this.result.Tar1cor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="10" style="width: 60px" v-model="this.result.Tar1wro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Coğrafya-1</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="6" style="width: 60px" v-model="this.result.Co1cor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="6" style="width: 60px" v-model="this.result.Co1wro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Matematik</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="40" style="width: 60px" v-model="this.result.Matcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="40" style="width: 60px" v-model="this.result.Matwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
        <div class="row mt-2" v-if="this.branch == '2'">
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Matematik</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="40" style="width: 60px" v-model="this.result.Matcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="40" style="width: 60px" v-model="this.result.Matwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Fizik</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="14" style="width: 60px" v-model="this.result.Fizcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="14" style="width: 60px" v-model="this.result.Fizwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Kimya</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="13" style="width: 60px" v-model="this.result.Kimcor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="13" style="width: 60px" v-model="this.result.Kimwro"></div>
                        </div>
                    </div>  
                </div>
            </div>
            <div class="col-lg-3">
                <div class="subjectname">
                    <h6>Biyoloji</h6>
                </div>
                <div class="row">
                    <div class="col-5">
                        <div class="row">
                            <div class="col-1">D:</div>
                            <div class="col-2 input"><input type="number" class="formforresource" min="0" max="13" style="width: 60px" v-model="this.result.Biycor"></div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-1">Y:</div>
                            <div class="col-6"><input type="number" class="formforresource" min="0" max="13" style="width: 60px" v-model="this.result.Biywro"></div>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
        <div class="mt-2 d-flex justify-content-center">
           <input type="submit" class="button-send" value="EKLE" @click="send()">
        </div>
        </form>
    </div>
</template>


<script>import axios from "axios"

export default {
    name: 'add_AYT',
    data() {
        return {
            searchbar: {},
            ResetFilter: {},
            dataçekme: false,
            showArama: false,
            Deneme: null,
            adet: null,
            branch: null,
            result: {
                kullanıcı: localStorage.getItem('kullanıcı').slice(1, -1),
                yanlış: null,
                net: null,
                Edebcor:null,
                Edebwro:null,
                Tar1cor:null,
                Tar1cwro:null,
                Co1cor:null,
                Co1wro:null,
                Matcor:null,
                Matwro:null,
                Fizcor:null,
                Fizwro:null,
                Kimcor:null,
                Kimwro:null,
                Biycor:null,
                Biywro:null,
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
                      return post.alan === 2
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
            for(let i =0; i < 19; i++) {
                let x = document.getElementsByClassName("formforresource")[i].validity.valid
                if(x == false) {
                    send = false 
                }
            }
            if(send == true) {
                this.result.zaman = new Date().getMonth();
            if (this.branch == 1) {
                let correct = this.result.Edebcor +  this.result.Tar1cor + this.result.Co1cor + this.result.Matcor
                let wrong = (this.result.Edebwro + this.result.Tar1wro + this.result.Co1wro + this.result.Matwro)
                let sumwro = wrong / 4
                this.result.net = correct - sumwro
                this.result.Edebwro = 24 - this.result.Edebcor
                this.result.Tar1cor = 10 - this.result.Tar1cor
                this.result.Co1wro = 6 - this.result.Co1cor
                this.result.Matwro = 40 - this.result.Matcor
            }
            else if (this.branch == 2) {
                let correct = this.result.Fizcor +  this.result.Kimcor + this.result.Biycor + this.result.Matcor
                let wrong = (this.result.Fizwro + this.result.Kimwro + this.result.Biywro + this.result.Matwro)
                let sumwro = wrong / 4
                this.result.net = correct - sumwro
                this.result.Fizwro = 14 - this.result.Fizcor
                this.result.Kimwro = 13 - this.result.Kimcor
                this.result.Biywro = 13 - this.result.Biycor
                this.result.Matwro = 40 - this.result.Matcor
            }
            this.result.kaynak = this.Deneme
            axios
                .post('/api/Kullanıcılar/Genel/AYTDeneme/', this.result)
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
.yanlış{
    margin-left: 5px;
}
.input {
    margin-left: -5px
}
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