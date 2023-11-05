// Obtener el contenedor de imágenes
const gallery = document.getElementById('gallery');

function createImg(src) {
	let div = document.createElement("DIV")
	div.classList.add('masonry-item')
	let img = document.createElement("img")
	img.src = src;
	div.appendChild(img)
	return div
}

const url_api = 'https://api.jikan.moe/v4/anime/20/pictures';

// Obtener las imágenes de la API
async function get_data(url) {
	try {
		let response = await fetch(url);
		let res_data = await response.json();

		let imagenes = res_data.data.map(item => item.webp.image_url);
		return imagenes;
	} catch (error) {
		console.error('Error fetching data:', error);
		return [];
	}
}

const fragment = document.createDocumentFragment();

async function add_images() {
	let imagenes = await get_data(url_api);
	for (const imagen of imagenes) {
		fragment.appendChild(createImg(imagen))
	}
	console.log(fragment);
	gallery.appendChild(fragment);
}

add_images();

window.onload = () => {
	const grid = document.querySelector(".masonry-grid");
	const masonry = new Masonry(grid, {
		columnWidth: 1,
		itemSelector: '.masonry-item',
		gutter: 25,
	});
};