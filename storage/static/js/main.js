const menuBtn = document.getElementById('menuBtn');
const menu = document.getElementById("menu");

menuBtn.addEventListener("click", ()=>{
	menu.classList.toggle("showMenu")
	menu.classList.toggle("translate-x-[-1200px]")
});

function showMenuBtn() {
	menu.classList.toggle("showMenu")
	menu.classList.toggle("translate-x-[-1200px]")
}