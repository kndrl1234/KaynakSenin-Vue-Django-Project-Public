<template>
<div id="carouselExampleDark" class="carousel carousel-light slide" data-bs-ride="carousel">
  <div id="" class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide a"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="3" aria-label="Slide 4"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active" data-bs-interval="10000">
      <img src="@/assets/a1.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>KaynakSenin'e hoşgeldin!</h5>
        <p>Geleceğiniz için en iyi kaynakları bulmanıza yardımcı olalım.</p>
      </div>
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Veritabanımıza göz atın.</h5>
        <p>Kaynaklar için yapılan yorumları ve puanlamaları görün.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Bir dakikadan kısa sürede denemelerinizi ekleyin.</h5>
        <p>Denemeyi çözen kişiler içerisinde kaçıncısınız öğrenin.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Gelişiminizi izleyin.</h5>
        <p>Kaydettiğiniz denemelerin analizlerini günlüğüm sayfasında bulabilirsiniz.</p>
      </div>
    </div>
  </div>

</div>
</template>


<script>
export default {
    name: 'carousel',
}
</script>


<style>
</style>