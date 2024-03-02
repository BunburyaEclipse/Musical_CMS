const swiperr = new Swiper('.naiper', {
	// Optional parameters
	rewind: true,
	followFinger: false,
	centeredSlides: false,
	slidesPerView: 1,
	spaceBetween: 20,
	speed: 2000,
	autoplay: {
		delay: 2000,
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




const swiper2 = new Swiper(".naiper-two", {
	loop: true,
	rewind: {
		delay: 2500,
	},
	autoplay: {
		disableOnInteraction: false,
		pauseOnMouseEnter: false,
		delay: 2500,
	},
	slidesPerView: 1,
	spaceBetween: 20,
	breakpoints: {
		// when window width is >= 320px
		650: {
			slidesPerView: 2,
			spaceBetween: 20
		},
		1024: {
			slidesPerView: 3,
		}
	}
});
