<template>
<div class="promotions flex-container">
    <div class="div1">

    </div>
    <div class="mt-3 countdown">
        <div class="mt-3 d-flex justify-content-center">
            <h4>2023 YKS Sayacı</h4>
        </div>
        <hr>
        <div class="row d-flex justify-content-center">
            <div class="col-2">

            </div>
            <div class="col-3">
                <h1>{{gün}}</h1>
                <h5>Gün</h5>
            </div>
            <div class="col-3">
                <h1>{{saat}}</h1>
                <h5>Saat</h5>
            </div>
            <div class="col-4">
                <h1>{{dakika}}</h1>
                <h5>Dakika</h5>
            </div>
        </div>
    </div>
</div>
</template>


<script>
export default {
    name: 'promotion',
    data() {
        return {
            gün: null,
            saat: null,
            dakika: null
        }
    },
    mounted() {
        const SınavTarihi = new Date('June 18, 2023 10:15:00').getTime()
            const şimdi = new Date().getTime()
            const gap = SınavTarihi - şimdi 
            const second = 1000
            const minute = second * 60
            const hour = minute * 60
            const day = hour * 24
            this.gün = Math.floor(gap / day)
            this.saat = Math.floor((gap % day) / hour)
            this.dakika = Math.floor((gap % hour) / minute)
    }
}
</script>


<style>
.flex-container {
    margin-left: 30px;
    margin-right: 20px;
    display: flex;
    flex-direction: column;
}
.div1 {
    height: 350px;
    margin-top: 10px;
} 
.countdown {
    border: 3px solid;
    border-color: #fa6400;
    color: white;
    border-radius: 10px;
}
</style>