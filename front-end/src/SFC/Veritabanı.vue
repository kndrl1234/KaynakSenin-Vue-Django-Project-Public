<template>
<title>Kaynakları Listele - KaynakSenin</title>
<div class="lightbgSrc">
  <div class="src container"> 
    <div class="row mt-5 ">
      <div class="col-lg-6 order-lg-3 KaynakSeninLogo">
        <h5>Kaynakları Listele</h5>
        <h1>KaynakSenin Veritabanı<br></h1>
        <label>YKS için piyasaya sunulmuş kaynakları listeler</label>
        <hr>
        <div class="row">
          <div class="col-2">
            <h6>Tür:</h6>
          </div>
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Type" value="1" v-model="SearchForm.tür"> Soru Bankası
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Type" value="2" v-model="SearchForm.tür"> Ders Kanalları
          </div>
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Type" value="3" v-model="SearchForm.tür"> Genel Deneme
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Type" value="4" v-model="SearchForm.tür"> Branş Denemesi
          </div> 
        </div>
        <div v-if="this.SearchForm.tür != '2'" class="row mt-4">
          <div class="col-2">
            <h6>Oturum:</h6>
          </div>
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Branch" value="" v-model="SearchForm.alan">
          </div>     
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Branch" value="1" v-model="SearchForm.alan"> TYT
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Branch" value="2" v-model="SearchForm.alan"> AYT
          </div>  
          <div  v-if="this.SearchForm.tür === '1'" class="col-3">
            <input  class="form-check-input" type="radio" name="Branch" value="3" v-model="SearchForm.alan"> TYT-AYT
          </div>             
        </div>
        <div v-if="this.SearchForm.tür != '3'" class="row  mt-4">
          <div class="col-2">
            <h6>Ders:</h6>
          </div>
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="" v-model="SearchForm.ders">
          </div> 
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="1" v-model="SearchForm.ders"> Matematik
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="2" v-model="SearchForm.ders"> Geometri
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="3" v-model="SearchForm.ders">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fizik
          </div> 
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="4" v-model="SearchForm.ders">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kimya
          </div> 
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="5" v-model="SearchForm.ders"> Biyoloji
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="6" v-model="SearchForm.ders">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tarih
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="7" v-model="SearchForm.ders"> Coğrafya
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="8" v-model="SearchForm.ders"> Felsefe
          </div> 
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="9" v-model="SearchForm.ders">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Din
          </div>                  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="Subject" value="10" v-model="SearchForm.ders">&nbsp;&nbsp;&nbsp;&nbsp; Türkçe
          </div>       
        </div>
        <div class="row mt-4">
          <div class="col-2">
            <h6>Parametre:</h6>
          </div>
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="" v-model="parametre">
          </div>
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="1" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp;  Öğretici Puanı
          </div>  
          <div class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="2" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp;  Deneyici Puanı
          </div>
          <div v-if="this.SearchForm.tür == '1'" class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="3" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp;  Sayfa sayısı
          </div> 
          <div v-if="this.SearchForm.tür == '1'" class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="4" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp;  Soru sayısı
          </div>  
          <div v-if="this.SearchForm.tür == '3' || this.SearchForm.tür == '4'" class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="5" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp;  Deneme sayısı
          </div>
          <div v-if="this.SearchForm.tür != '2'" class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="6" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp; Fiyat (azdan)
          </div>    
          <div v-if="this.SearchForm.tür != '2'" class="col-lg-2">
            <input class="form-check-input" type="radio" name="parameter" value="7" v-model="parametre">&nbsp;&nbsp;&nbsp;&nbsp; Fiyat (çokdan)
          </div>        
        </div>
        <div class="d-flex mt-3 justify-content-center">
          <button @click="log()" class="button-7">Sırala</button>
        </div>
      </div>
      <div class="col-1 order-2">

      </div>
      <div class="col-lg-5 order-lg-1">
      <div class="row mb-3 p-1">
        <div class="col-3 mt-2"> <h5>Arama:</h5></div>
        <div class="col-6 mt-2"><input type="text" v-model="Search"></div>
        <div class="col-2"><button class="button-7" @click="search">Ara</button></div>
      </div>
      <h5>YKS Kaynak Listesi:</h5>
        <div class="mt-2  " v-if="okay == true">
          <div v-for="(book, index) in ResetFilter" v-bind:key="(book,index)">
            <div class="card">
              <router-link :to="{ name: 'SpesificBook', params: { name: book.tür + '/' + book.isim }}" class="card-header"><h6 class="mt-1">{{index + 1}}. {{book.isim}}</h6></router-link>
              <div class="card-body">
                <div class="row">
                  <div class="col-lg-2 foto"> 
                    <img v-bind:src="book.foto" width="60" height="75" />
                  </div>
                  <div class="col-lg-10 kaynakPuanları">
                    <div class="row">
                      <div class="col-3">
                        Öğretici Puan
                        <div class="KaynakPuanlarıBig">{{book.öğretici}}<i class="bi icon bi-star-fill ms-1" id="star1"></i></div>
                      </div>
                      <div class="col-3">
                        Senin Puanın 
                        <div class="KaynakPuanlarıBig ">{{book.Köğretici}}<i class="bi icon bi-star-fill ms-1" id="star2"></i></div>
                      </div>
                      <div class="col-3">
                        Zorluk Puanı 
                        <div class="KaynakPuanlarıBig ">{{book.deneyici}}<i class="bi icon bi-star-fill ms-1" id="star3"></i></div>
                      </div>
                      <div class="col-3">
                        Senin Puanın 
                        <div class="KaynakPuanlarıBig ">{{book.Kdeneyici}}<i class="bi icon bi-star-fill ms-1" id="star4"></i></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>      
      </div>     
    </div> 
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Veritabanı",
  mounted() {
    this.SearchForm.tür = this.$store.state.fromhomepage,
    this.SearchForm.ders = this.$store.state.ders
    axios
      .get('api/' + this.SearchForm.tür + '/')
      .then(response =>{
        for(let i = 0; i < response.data.length; i++) {
          if(response.data[i].Puanlama.length != 0) {
            let puan1 = response.data[i].Puanlama.map((item) => {
              return Number(item.öğretici)
            })
        
            let x = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)  
            response.data[i].öğretici = x
            let puan2 = response.data[i].Puanlama.map((item) => {
              return Number(item.deneyici)
            })
            let y = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)  
            response.data[i].deneyici = y
            if(localStorage.getItem('kullanıcı').slice(1, -1) != '') {
              let kullanıcı =  response.data[i].Puanlama.filter((post) => {
              return post.sahip == localStorage.getItem('kullanıcı').slice(1, -1)
              })
              response.data[i].Köğretici = kullanıcı[0].öğretici
              response.data[i].Kdeneyici = kullanıcı[0].deneyici
            }
            else {
              response.data[i].Köğretici = '?'
              response.data[i].Kdeneyici = '?'
            }
          }
          else {
            response.data[i].öğretici = '?'
            response.data[i].deneyici = '?'
            response.data[i].Köğretici = '?'
            response.data[i].Kdeneyici = '?'
          }
        }
        this.Results = response.data
        this.ResetFilter = response.data
        this.okay = true 
      })
  },
  data(){
      return {  
        Search: '',
        okay: false,
        parametre: '',
        SearchForm: {
            tür: '',
            alan: '',
            ders: '',
        },
        Results: {},
        ResetFilter: {},
      }
  },
  methods: {
      search () {
        this.asd()
        this.ResetFilter = this.ResetFilter.filter((post) => {
          return post.isim.toLowerCase().includes(this.Search.toLowerCase())
        })
      },
      asd() {
        this.ResetFilter = this.Results
      },
      async log() {
        if(this.SearchForm.tür == '1') {
          await axios
            .get('api/' + this.SearchForm.tür + '/')
            .then(response =>{
              this.Results = response.data
              this.ResetFilter = response.data
              this.okay = true    
            if(this.SearchForm.alan  == '' && this.SearchForm.ders  == '') {    
              this.okay = true 
            }
            else if(this.SearchForm.alan  == '') {
              this.ResetFilter = this.Results.filter((item) => {
              return (item.ders == this.SearchForm.ders)}) 
              console.log(this.ResetFilter)             
              this.okay = true                   
            }
            else if(this.SearchForm.ders  == '') {
              this.ResetFilter = this.Results.filter((item) => {
              return (item.alan == this.SearchForm.alan)})        
              this.okay = true 
            }
            else{
              this.ResetFilter = this.Results.filter((item) => {
              return (item.alan == this.SearchForm.alan && item.ders == this.SearchForm.ders)})                
              this.okay = true                   
            }   
            })
            for(let i = 0; i < this.ResetFilter.length; i++) {
              if(this.ResetFilter[i].Puanlama.length != 0) {
                let puan1 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.öğretici)
                })
                let x = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)  
                this.ResetFilter[i].öğretici = x
                let puan2 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.deneyici)
                })
                let y = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)  
                this.ResetFilter[i].deneyici = y
                if(localStorage.getItem('kullanıcı').slice(1, -1) != '') {
                  let kullanıcı =  this.ResetFilter[i].Puanlama.filter((post) => {
                  return post.sahip == localStorage.getItem('kullanıcı').slice(1, -1)
                  })
                  this.ResetFilter[i].Köğretici = kullanıcı[0].öğretici
                  this.ResetFilter[i].Kdeneyici = kullanıcı[0].deneyici
                }
                else {
                  this.ResetFilter[i].Köğretici = '?'
                  this.ResetFilter[i].Kdeneyici = '?'
                }
              }
              else {
                this.ResetFilter[i].öğretici = '?'
                this.ResetFilter[i].deneyici = '?'
                this.ResetFilter[i].Köğretici = '?'
                this.ResetFilter[i].Kdeneyici = '?'
              }
            }
        }
        else if(this.SearchForm.tür == '2') {
          await axios
            .get('api/' + this.SearchForm.tür + '/')
            .then(response =>{
              this.Results = response.data
              this.ResetFilter = response.data
              this.okay = true    
            if(this.SearchForm.ders  == '') {    
              this.okay = true 
            }
            else {
            this.ResetFilter = this.Results.filter((item) => {
            return (item.ders == this.SearchForm.ders)})   
            this.ResetFilter.push(this.Results.filter((item) => {
            return (item.ders == '11')}))            
            this.okay = true                    
          }   
            })
            for(let i = 0; i < this.ResetFilter.length; i++) {
              if(this.ResetFilter[i].Puanlama.length != 0) {
                let puan1 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.öğretici)
                })
                let x = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)  
                this.ResetFilter[i].öğretici = x
                let puan2 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.deneyici)
                })
                let y = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)  
                this.ResetFilter[i].deneyici = y
                if(localStorage.getItem('kullanıcı').slice(1, -1) != '') {
                  let kullanıcı =  this.ResetFilter[i].Puanlama.filter((post) => {
                  return post.sahip == localStorage.getItem('kullanıcı').slice(1, -1)
                  })
                  this.ResetFilter[i].Köğretici = kullanıcı[0].öğretici
                  this.ResetFilter[i].Kdeneyici = kullanıcı[0].deneyici
                }
                else {
                  this.ResetFilter[i].Köğretici = '?'
                  this.ResetFilter[i].Kdeneyici = '?'
                }
              }
              else {
                this.ResetFilter[i].öğretici = '?'
                this.ResetFilter[i].deneyici = '?'
                this.ResetFilter[i].Köğretici = '?'
                this.ResetFilter[i].Kdeneyici = '?'
              }
            }          
        }
        else if(this.SearchForm.tür == '3') {
          await axios
            .get('api/' + this.SearchForm.tür + '/')
            .then(response =>{
              this.Results = response.data
              this.ResetFilter = response.data
              this.okay = true    
              if(this.SearchForm.alan  == '') {
                this.ResetFilter = this.Results               
                this.okay = true 
              }
              else {
                this.ResetFilter = this.Results.filter((item) => {
                return (item.alan == this.SearchForm.alan)})                 
                this.okay = true                    
              }   
            })
            for(let i = 0; i < this.ResetFilter.length; i++) {
              if(this.ResetFilter[i].Puanlama.length != 0) {
                let puan1 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.öğretici)
                })
                let x = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)  
                this.ResetFilter[i].öğretici = x
                let puan2 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.deneyici)
                })
                let y = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)  
                this.ResetFilter[i].deneyici = y
                if(localStorage.getItem('kullanıcı').slice(1, -1) != '') {
                  let kullanıcı =  this.ResetFilter[i].Puanlama.filter((post) => {
                  return post.sahip == localStorage.getItem('kullanıcı').slice(1, -1)
                  })
                  this.ResetFilter[i].Köğretici = kullanıcı[0].öğretici
                  this.ResetFilter[i].Kdeneyici = kullanıcı[0].deneyici
                }
                else {
                  this.ResetFilter[i].Köğretici = '?'
                  this.ResetFilter[i].Kdeneyici = '?'
                }
              }
              else {
                this.ResetFilter[i].öğretici = '?'
                this.ResetFilter[i].deneyici = '?'
                this.ResetFilter[i].Köğretici = '?'
                this.ResetFilter[i].Kdeneyici = '?'
              }
            }              
        }  
        else if(this.SearchForm.tür == '4') {
          await axios
            .get('api/' + this.SearchForm.tür + '/')
            .then(response =>{
              this.Results = response.data
              this.ResetFilter = response.data
              this.okay = true    
              if(this.SearchForm.alan  == '') {
                this.ResetFilter = this.Results               
                this.okay = true 
              }
              else {
                this.ResetFilter = this.Results.filter((item) => {
                return (item.alan == this.SearchForm.alan)})                 
                this.okay = true                    
              }   
            })
            for(let i = 0; i < this.ResetFilter.length; i++) {
              if(this.ResetFilter[i].Puanlama.length != 0) {
                let puan1 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.öğretici)
                })
                let x = (puan1.reduce((a, b) => a + b) / puan1.length).toFixed(1)  
                this.ResetFilter[i].öğretici = x
                let puan2 = this.ResetFilter[i].Puanlama.map((item) => {
                  return Number(item.deneyici)
                })
                let y = (puan2.reduce((a, b) => a + b) / puan2.length).toFixed(1)  
                this.ResetFilter[i].deneyici = y
                if(localStorage.getItem('kullanıcı').slice(1, -1) != '') {
                  let kullanıcı =  this.ResetFilter[i].Puanlama.filter((post) => {
                  return post.sahip == localStorage.getItem('kullanıcı').slice(1, -1)
                  })
                  this.ResetFilter[i].Köğretici = kullanıcı[0].öğretici
                  this.ResetFilter[i].Kdeneyici = kullanıcı[0].deneyici
                }
                else {
                  this.ResetFilter[i].Köğretici = '?'
                  this.ResetFilter[i].Kdeneyici = '?'
                }
              }
              else {
                this.ResetFilter[i].öğretici = '?'
                this.ResetFilter[i].deneyici = '?'
                this.ResetFilter[i].Köğretici = '?'
                this.ResetFilter[i].Kdeneyici = '?'
              }
          }         
        }            
        else {
          alert('al goredın')
        }
        if(this.parametre == '1') {
          console.log(this.ResetFilter)
          let x = this.ResetFilter.sort((a,b) => {
            return b.öğretici - a.öğretici
        })
          console.log(x)
          this.ResetFilter = x
          this.Results = x
        }
        if(this.parametre == '2') {
          let x = this.ResetFilter.sort((a,b) => {
            return b.deneyici - a.deneyici
        })
          this.ResetFilter = x
          this.Results = x
        }
        else if(this.parametre == '3') {
          this.ResetFilter.sort((a,b) => {
            return b.soru_adet - a.soru_adet
          })
        }
        else if(this.parametre == '4') {
          this.ResetFilter.sort((a,b) => {
            return b.sayfa - a.sayfa
          })
        }
        else if(this.parametre == '5') {
          this.ResetFilter.sort((a,b) => {
            return b.adet - a.adet
          })
        }
        else if(this.parametre == '6') {
          this.ResetFilter.sort((a,b) => {
            return a.fiyat - b.fiyat
          })
        }
        else if(this.parametre == '7') {
          this.ResetFilter.sort((a,b) => {
            return b.fiyat - a.fiyat
          })
        }
        
      },
  }
}
</script>


<style>
a {
text-decoration: none;
}
.lightbgSrc {
  margin-top: -10px;
  padding-left: 50px;
  background-image: linear-gradient(rgba(170,170,170), rgba(220,220,220));
}
.KaynakSeninLogo {
  margin-top: -50px;
}
.src {
  color: rgb(110,70,70);
  background-color: rgb(240,240,240);
  margin-top: 10px;
  padding: 30px;
  border-radius: 5px;
}
.searchbuttton {
  margin-top: 20px;
  background-color: orange;
}
.results1 {
  margin-top: 50px;
}
.kaynakPuanları {
  font-size: 10px;
  font-weight: 600;
  margin-top: 10px;
  margin-left: 20px;
}
.KaynakPuanlarıBig {
  font-size: 15px;
  margin-left: 13px;
}
.foto {
  margin: -10px;
}
#star1 {
  font-size: 20px;
}
#star2 {
  font-size: 20px;
}
#star3 {
  font-size: 20px;
}
#star4 {
  font-size: 20px;
}
</style>



