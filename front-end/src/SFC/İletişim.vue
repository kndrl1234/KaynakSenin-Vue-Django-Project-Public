<template>
<title>İletişime Geç - KaynakSenin</title>
<div class="contact d-flex justify-content-center">
  <h1>Bizimle İletişime Geçin</h1>
</div>
<div class="contactformplace container">
<div class="contactdescription">
    <h5 class="mb-3">İstekleriniz, şikayetleriniz ve bug tespitleriniz için bize kolayca ulaşabilirsiniz</h5>
    <h6>Site Email:</h6>
    <h6>Admin Email:</h6>
    <h6>Telefon:</h6>
</div>

<div class="d-flex justify-content-center">
    <h2 class=" text-light">Hızlı İletişim Formu</h2>
</div>
<div class="contactsrc">
<h6>Aşağıdaki konulardan birini seçiniz:</h6>
  <select class="contactx form-select form-select-sm" v-model="ContactForm.anaKonu">
    <option value="Genel Şikayet">Genel Şikayet</option>
    <option value="Bug Var">Bug Var</option>
    <option value="Eksik Kaynak">Eksik Kaynak</option>
    <option value="Site Yanlış Bilgi İçeriyor">Site Yanlış Bilgi İçeriyor</option>
    <option value="Rica/Tavsiye/Öneri<">Rica/Tavsiye/Öneri</option>
    <option value="Başka Bir Neden">Başka Bir Neden</option>
  </select>

<div class="exampleFormControlTextarea1">
    <h6>Mesaj Başlığı:</h6>
    <input class="form-control form-control-sm" type="text" aria-label=".form-control-sm example" v-model="ContactForm.başlık">
</div>

<div class="exampleFormControlTextarea1">
    <h6>Mesajınızı aşağıya yazabilirsiniz:</h6>
    <textarea class="form-control"  rows="10" v-model="ContactForm.mesaj"></textarea>
</div>

<div class="d-flex justify-content-center">
    <button type="button" class="button-7" @click="sendmessage">Gönder</button>
</div>

</div>
</div>
</template>

<script>
import axios from "axios"

export default {    
    name: "İletişim",
    data() {
        return {
            ContactForm: {
                anaKonu: '',
                başlık: '',
                mesaj: '',
            }
        }
    },
    methods: {
        sendmessage() {
            if(this.ContactForm.message == '') {
                alert("E bişi yazsaydın?")
            }
            else {
                axios
                    .post('/api/Mesajlar/', this.ContactForm)
                    .then(
                        alert('Gönderildi, ilginiz için teşekkür ederiz.'),
                        this.$router.push({ name: "MainPage" })
                    )

            }
        }
    }
}
</script>


<style>
.contact {
    margin-top: 20px;
    color:white;
    font-weight: 200;
}
.contactdescription {
    color:white;
    padding: 10px;
}
.contactformplace {
    margin-top: 10px;
    background-color: rgb(20, 20, 20);
    border-radius: 30px;
    padding-top: 20px;
}
.contactsrc {
    color:white;
    background-color: grey;
    border-radius: 30px;
    padding: 20px;
    margin-top: 10px;
}
.exampleFormControlTextarea1 {
    margin-top: 20px;
    margin-bottom: 20px;
}
.button-7 {
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
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 2rem;
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
.button-7:hover,
.button-7:focus {
  background-color: #fb8332;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
}
</style>



