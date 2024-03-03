const menuBtn = document.getElementById('menuBtn');
const menu = document.getElementById("menu");
const modal_btn = document.getElementById("modal_info_btn");

menuBtn.addEventListener("click", ()=>{
	menu.classList.toggle("showMenu")
	menu.classList.toggle("translate-x-[-1200px]")
}); 

modal_btn.addEventListener("click", ()=>{
	menu.classList.remove("showMenu");
	menu.classList.add("translate-x-[-1200px]");
})