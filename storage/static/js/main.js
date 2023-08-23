const swiper = new Swiper('.naiper', {
    // Optional parameters
    rewind: true,
    followFinger: false,
    centeredSlides: false,
    slidesPerView: 1,
    spaceBetween: 20,
    followFinger: true,
    freeMode: true,
    speed: 8000,
    autoplay: {
      delay: 0,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },

    breakpoints: {
      // when window width is >= 320px
      320: {
        slidesPerView: 1.3,
      },
      // when window width is >= 480px
      600: {
        slidesPerView: 2.2,
      },
      // when window width is >= 640px
      1024: {
        slidesPerView: 3.7,
      }
    }

  });