const mapa = document.getElementById('map')

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




const swiper2 = new Swiper(".naiper-two", {
	loop: true,
	autoplay: {
		disableOnInteraction: false,
		pauseOnMouseEnter: true,
		delay: 1500,
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

let iniciarMap = () => {
	let coord = {
		lat: -0.1075867,
		lng: -78.4696461,
	}
	let map = new google.maps.Map(mapa, {
		zoom: 10,
		center: coord,
	})
};