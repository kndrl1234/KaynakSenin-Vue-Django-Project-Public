<template>
<div class="listdesc">
    <h3>Öne Çıkan {{h3}}</h3>
    <div class="x row justify-content-between">
        <div class="span col-xl-5">
            <span class="">{{spn}}</span>
        </div>
        <div class="col-xl-2">
            <router-link to="/Kaynaklar" class="router-link" @click="send"><button type="button" class="btnmore">Tam liste için</button></router-link>
        </div>
    </div>
</div>
<div class="list">
  
  <card 
    :name="publisher1"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher2"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card
    :name="publisher3"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher4"
    :fromhomepage="fromhomepage"
    :ders="ders" 
  />

  <card 
    :name="publisher5"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher6"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher7"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher8"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher9"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />

  <card 
    :name="publisher10"
    :fromhomepage="fromhomepage"
    :ders="ders"
  />
</div>
</template>


<script>
import card from '@/components/MainPage/card.vue'
export default {
    name: 'book_list',
    components: { card },
    methods: {
      send() {
        this.$store.state.fromhomepage = this.fromhomepage
        this.$store.state.ders = this.ders
      }
    },
    props: [
    'h3', 'spn', 'fromhomepage', 'ders',
    'publisher1',
    'publisher2',
    'publisher3',
    'publisher4',
    'publisher5',
    'publisher6',
    'publisher7',
    'publisher8',
    'publisher9',
    'publisher10',
    ]
}
</script>


<style>
.router-link{
    text-decoration: none;
    color:#fff;
}
.btnmore {
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
  min-height: 3rem;
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
.btnmore:hover,
.btnmore:focus {
  background-color: #fb8332;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
}
.x {
    margin:auto;
}
.span {
    margin-left: -10px;
    margin-top: 15px;
}
.listdesc {
    color: white;
    margin-top:120px;
    margin-left:70px;
}
.list {
    margin-left: 40px;
    margin-right: 50px;
    overflow: auto;
    white-space: nowrap;
}

.list::-webkit-scrollbar {
  width: 50px;
}

::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px rgb(250,100,0); 
  border-radius: 10px;
}
 
::-webkit-scrollbar-thumb {
  background: rgb(250,100,0); 
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgb(250,100,0); 
}
</style>