<template>
<div class="mt-2 p-4"> 
    <div class="row">
        
        <h1>Deneme Net Grafikleriniz</h1>
        <hr>
        <div class="col-lg-1 mt-3">
            <button class="button-7" @click="showBranch">TYT</button>
        </div>
        <div class="col-lg-1 mt-3">
            <button class="button-7" @click="showBranch">AYT</button>
        </div>
        <div class="col-lg-2 mt-3">
            <select class="button-7" v-model="ay">
                <option value="0">Ocak</option>
                <option value="1">Şubat</option>
                <option value="2">Mart</option>
                <option value="3">Nisan</option>
                <option value="4">Mayıs</option>
                <option value="5">Haziran</option>
                <option value="6">Temmuz</option>
                <option value="7">Ağustos</option>
                <option value="8">Eylül</option>
                <option value="9">Ekim</option>
                <option value="10">Kasım</option>
                <option value="11">Aralık</option>
            </select>
        </div>
        
    </div> 

    <div v-if="showTYT == true" class="row">
        <div class="col-lg-5">
            <Bar :chart-data="chartDataTYT" />
        </div>
        <div class="col-2"></div>
        <div class="col-lg-5">
            <Line :chart-data="LineChart"/>
        </div>
    </div>
    <div v-if="showAYT == true" class="row">
        <div class="col-lg-5">
            <Bar :chart-data="chartDataAYT" />
        </div>
        <div class="col-2"></div>
        <div class="col-lg-5">
            <Line :chart-data="LineChartAYT"/>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import { Bar, Line} from 'vue-chartjs'
import {ArcElement, PointElement, LineElement, Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement, PointElement, LineElement)

export default {
    name: 'statTop',
    components: { Bar, Line},
    data() {
        return {
            showTYT: true,
            showAYT: false,
            ay: '0',
            kullanıcı:null,
            chartDataTYT: {
            labels: [ 'Türkçe', 'Sosyal', 'Matematik', 'Fen' ],
            datasets: [],
            },
            chartDataAYT: {
                labels: [],
                datasets: [],
            },
            LineChart: {
                labels:'HTAEEKAOŞMNM',
                datasets: []
            },
            LineChartAYT: {
                labels:'HTAEEKAOŞMNM',
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
                    let TYTNet= []
                    let TYT = []
                    let array = []
                    let array2 = []
                    let array3 = []
                    let array4 = []
                    let MatematikNet,TürkçeNet,SosyalNet, FenNet = null
                    if(this.kullanıcı.KullanıcıTYTDenemeleri != null){
                        let zaman = new Date().getMonth()
                        const filtered = this.kullanıcı.KullanıcıTYTDenemeleri.filter((item) => {
                        return (item.zaman == zaman)}) 
                        for (let i = 0; i < filtered.length; i++) {
                            array.push(filtered[i].Mcor)
                            const sum = array.reduce((a, b) => a + b, 0);
                            MatematikNet = (sum / array.length) || 0;

                            array2.push(filtered[i].TRcor)
                            const sum2 = array2.reduce((a, b) => a + b, 0);
                            TürkçeNet = (sum2 / array2.length) || 0;

                            array3.push(filtered[i].SScor)
                            const sum3 = array3.reduce((a, b) => a + b, 0);
                            SosyalNet = (sum3 / array3.length) || 0;

                            array4.push(filtered[i].Scor)
                            const sum4 = array4.reduce((a, b) => a + b, 0);
                            FenNet = (sum4 / array4.length) || 0;
                        }
                        
                        TYTNet.push(TürkçeNet,SosyalNet,MatematikNet,FenNet,40)
                        this.chartDataTYT.datasets.push({ 
                            data: TYTNet,
                            label: 'Bu ay',
                            backgroundColor: [
                            'rgb(255, 0, 0)'],  
                        })
                        for (let i = 5; i < 12; i++) {
                            const asd = this.kullanıcı.KullanıcıTYTDenemeleri.filter((item) => {
                            return (item.zaman == i)})
                            let average = asd.reduce((total, next) => total + next.net, 0) / asd.length
                            if( isNaN(average)) {
                                average = null 
                            }
                            TYT.push(average)
                        }
                        for (let i = 0; i < 5; i++) {
                            const asd = this.kullanıcı.KullanıcıTYTDenemeleri.filter((item) => {
                            return (item.zaman == i)})
                            let average = asd.reduce((total, next) => total + next.net, 0) / asd.length
                            if( isNaN(average)) {
                                average = null 
                            }
                            TYT.push(average)
                        }  
                        TYT.push(0,120)
                        this.LineChart.datasets.push({
                          label: 'TYT Net Grafiği',
                          data: TYT,
                          fill: false,
                          borderColor: 'rgb(75, 192, 192)',
                          tension: 0.1
                        })
                    }
                    let AYTNet= []
                    let AYT = []
                    let arrayAYT = []
                    let arrayAYT2 = []
                    let arrayAYT3 = []
                    let arrayAYT4 = []
                    let arrayAYT5 = []
                    let arrayAYT6 = []
                    let arrayAYT7 = []
                    let a,b,c,d,e,f,g = null
                    if(this.kullanıcı.KullanıcıAYTDenemeleri != null){
                        let zaman = new Date().getMonth()
                        const filtered = this.kullanıcı.KullanıcıAYTDenemeleri.filter((item) => {
                        return (item.zaman == zaman)}) 
                        for (let i = 0; i < filtered.length; i++) {
                            arrayAYT.push(filtered[i].Edebcor)
                            const sum = arrayAYT.reduce((a, b) => a + b, 0);
                            a = (sum / arrayAYT.length) ||  0;
                            arrayAYT2.push(filtered[i].Tar1cor)
                            const sum2 = arrayAYT2.reduce((a, b) => a + b, 0);
                            b = (sum2 / arrayAYT2.length) ||  0;
                            arrayAYT3.push(filtered[i].Co1cor)
                            const sum3 = arrayAYT3.reduce((a, b) => a + b, 0);
                            c = (sum3 / arrayAYT3.length) ||  0;
                            arrayAYT4.push(filtered[i].Matcor)
                            const sum4 = arrayAYT4.reduce((a, b) => a + b, 0);
                            d = (sum4 / arrayAYT4.length) ||  0;
                            arrayAYT5.push(filtered[i].Fizcor)
                            const sum5 = arrayAYT5.reduce((a, b) => a + b, 0);
                            e = (sum5 / arrayAYT5.length) ||  0;
                            arrayAYT6.push(filtered[i].Kimcor)
                            const sum6 = arrayAYT6.reduce((a, b) => a + b, 0);
                            f = (sum6 / arrayAYT6.length) ||  0;
                            arrayAYT7.push(filtered[i].Biycor)
                            const sum7 = arrayAYT7.reduce((a, b) => a + b, 0);
                            g = (sum7 / arrayAYT7.length) || 0;
                        }
                        if(e == null && f == null && g == null) {
                            AYTNet.push(a,b,c,d,40)
                            this.chartDataAYT.labels.push('Edebiyat','Tarih', 'Coğrafya', 'Matematik') 
                            this.chartDataAYT.datasets.push({ 
                            data: AYTNet,
                            label: 'Bu ay',
                            backgroundColor: [
                            'rgb(255, 0, 0)'],  
                            })  
                        }
                        else {
                            AYTNet.push(d,e,f,g,40)
                            this.chartDataAYT.labels.push('Matematik','Fizik','Kimya','Biyoloji') 
                            this.chartDataAYT.datasets.push({ 
                            data: AYTNet,
                            label: 'Bu ay',
                            backgroundColor: [
                            'rgb(255, 0, 0)'],  
                            })  
                        }
                        for (let i = 5; i < 12; i++) {
                            const asd = this.kullanıcı.KullanıcıAYTDenemeleri.filter((item) => {
                            return (item.zaman == i)})
                            let average = asd.reduce((total, next) => total + next.net, 0) / asd.length
                            if( isNaN(average)) {
                                average = null 
                            }
                            AYT.push(average)
                        }
                        for (let i = 0; i < 5; i++) {
                            const asd = this.kullanıcı.KullanıcıAYTDenemeleri.filter((item) => {
                            return (item.zaman == i)})
                            let average = asd.reduce((total, next) => total + next.net, 0) / asd.length
                            if( isNaN(average)) {
                                average = null 
                            }
                            AYT.push(average)
                        }
                        AYT.push(0,120)
                        this.LineChartAYT.datasets.push({
                          label: 'AYT Net Grafiği',
                          data: AYT,
                          fill: false,
                          borderColor: 'rgb(75, 192, 192)',
                          tension: 0.1
                        }) 
                    }
                })
        }
    },
    methods: {
        showBranch() {
            if(this.showTYT == true) {
                this.showTYT = false
                this.showAYT = true
            }
            else {
                this.showTYT = true
                this.showAYT = false
            }
        },
    },
    watch: {
        ay(YeniAy) {
            if (YeniAy) {
                let TYTNet = []
                let array = []
                let array2 = []
                let array3 = []
                let array4 = []                    
                let MatematikNet = null
                let TürkçeNet = null
                let SosyalNet = null
                let FenNet = null
                const filtered = this.kullanıcı.KullanıcıTYTDenemeleri.filter((item) => {
                return (item.zaman == this.ay)}) 
                for (let i = 0; i < filtered.length; i++) {
                    array.push(filtered[i].Mcor)
                    const sum = array.reduce((a, b) => a + b, 0);
                    MatematikNet = (sum / array.length) || 0;
                    array2.push(filtered[i].TRcor)
                    const sum2 = array2.reduce((a, b) => a + b, 0);
                    TürkçeNet = (sum2 / array2.length) || 0;
                    array3.push(filtered[i].SScor)
                    const sum3 = array3.reduce((a, b) => a + b, 0);
                    SosyalNet = (sum3 / array3.length) || 0;
                    array4.push(filtered[i].Scor)
                    const sum4 = array4.reduce((a, b) => a + b, 0);
                    FenNet = (sum4 / array4.length) || 0;
                }
                TYTNet.push(TürkçeNet,SosyalNet,MatematikNet,FenNet)
                this.chartDataTYT.datasets.push({ 
                            data: TYTNet,
                            label: this.ay + '. ay',
                            backgroundColor: [
                            'rgb(0, 0, 250)'], 
                })
                let AYTNet = []
                let arrayAYT = []
                let arrayAYT2 = []
                let arrayAYT3 = []
                let arrayAYT4 = []
                let arrayAYT5 = []
                let arrayAYT6 = []
                let arrayAYT7 = []                    
                let a,b,c,d,e,f,g = null
                const filtered2 = this.kullanıcı.KullanıcıAYTDenemeleri.filter((item) => {
                return (item.zaman == this.ay)}) 
                for (let i = 0; i < filtered2.length; i++) {
                    arrayAYT.push(filtered[i].Edebcor)
                    const sum = arrayAYT.reduce((a, b) => a + b, 0);
                    a = (sum / arrayAYT.length) || 0
                    arrayAYT2.push(filtered[i].Tar1cor)
                    const sum2 = arrayAYT2.reduce((a, b) => a + b, 0);
                    b = (sum2 / arrayAYT2.length) || 0
                    arrayAYT3.push(filtered[i].Co1cor)
                    const sum3 = arrayAYT3.reduce((a, b) => a + b, 0);
                    c = (sum3 / arrayAYT3.length) || 0
                    arrayAYT4.push(filtered[i].Matcor)
                    const sum4 = arrayAYT4.reduce((a, b) => a + b, 0);
                    d = (sum4 / arrayAYT4.length) || 0
                    arrayAYT5.push(filtered[i].Fizcor)
                    const sum5 = arrayAYT5.reduce((a, b) => a + b, 0);
                    e = (sum5 / arrayAYT5.length) || 0
                    arrayAYT6.push(filtered[i].Kimcor)
                    const sum6 = arrayAYT6.reduce((a, b) => a + b, 0);
                    f = (sum6 / arrayAYT6.length) || 0
                    arrayAYT7.push(filtered[i].Biycor)
                    const sum7 = arrayAYT7.reduce((a, b) => a + b, 0);
                    g = (sum7 / arrayAYT7.length) || 0;
                }
                if(e == null && f == null && g == null) {
                    AYTNet.push(a,b,c,d,40)
                    this.chartDataAYT.datasets.push({ 
                    data: AYTNet,
                    label: this.ay + '. ay',
                    backgroundColor: [
                    'rgb(255, 0, 0)'],  
                    })  
                }
                else {
                    AYTNet.push(d,e,f,g,40)
                    this.chartDataAYT.datasets.push({ 
                    data: AYTNet,
                    label: this.ay + '. ay',
                    backgroundColor: [
                    'rgb(255, 0, 0)'],  
                    })  
                }         
            }
        }
    },
}
</script>

<style>

</style>