<template>
<div class="mt-2 p-4"> 
    <div class="row">
        <h3>Deneme Net Grafikleriniz (Giriş Yapmanız Gerekir)</h3>
        <hr>
        <div class="col-lg-1 mt-3">
            <button class="button-7" >TYT</button>
        </div>
        <div class="col-lg-1 mt-3">
            <button class="button-7">AYT</button>
        </div>
        <div class="col-lg-2 mt-3">
            <select class="button-7">
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

    <div class="row">
        <div class="col-lg-5">
            <Bar :chart-data="chartDataTYT" />
        </div>
        <div class="col-2"></div>
        <div class="col-lg-5">
            <Line :chart-data="LineChart"/>
        </div>
    </div>
</div>
<div class="mt-3 p-4">
    <div class="row">
         <h3>Aylık Yanlış/Boş Ders Grafiğiniz ve Deneme Sıralamalarınız</h3>
         <hr>
        <div class="col-lg-1 mt-3">
            <button class="button-7">TYT</button>
        </div>
        <div class="col-lg-6 mt-3">
            <button class="button-7" >AYT</button>
        </div>
    </div>
    
    <div class="row">
        <div class="col-lg-5">
            Sosyal Bilimler ve Fen Bilimleri 2 ile çarpılarak oranlanmıştır.
            <Pie :chart-data="PieChartDers"/>
        </div>
        <div class="col-2">

        </div>
        <div class="col-lg-5">
            <h3>Çözdüğünüz Denemelerden arayınız: </h3>
            <hr>
            <div class="mt-4 row">
                <div class="col-2">
                    <h5>Kaynak:</h5>
                </div>
                <div class="col-8">
                    <input class="formforresource" type="text">
                </div> 
            </div>
            <div class="p-3 denemearkaplan">
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
        </div>
    </div>
</div>
</template>

<script>
import { Bar, Line,Pie} from 'vue-chartjs'
import {ArcElement, PointElement, LineElement, Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement, PointElement, LineElement)

export default {
    name: 'NoLog',
    components: { Bar, Line,Pie},
    data() {
        return {
            chartDataTYT: {
                labels: [ 'Türkçe', 'Sosyal', 'Matematik', 'Fen' ],
                datasets: [ {
                    data: ['32', '17', '26', '13','0','40'],
                    label: 'Bu ay',
                    backgroundColor: [
                    'rgb(255, 0, 0)'], 
                }],
            },
            LineChart: {
                labels:'HTAEEKAOŞMNM',
                datasets: [{
                    label: 'TYT Net Grafiği',
                    data: ['57','65','71','68','75','85','77','76','83','89','88','94','0','120'],
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            PieChartDers: {
                labels: [
                'Türkçe',
                'Sosyal Bilimler',
                'Matematik',
                'Fen Bilimleri'
              ],
              datasets: [{ 
                data: ['8', '6', '13', '6'],
                backgroundColor: [
                  'rgb(255, 0, 0)',
                  'rgb(255, 255, 0)',
                  'rgb(0, 0, 255)',
                  'rgb(0, 255, 0)'
                ],
                hoverOffset: 4
            }]
            },
        }   
    },
}
</script>

<style>

</style>