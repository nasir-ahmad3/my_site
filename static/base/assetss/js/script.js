let nav = document.querySelector('body > nav')

window.addEventListener('scroll', e => {
	if (window.scrollY != 0 && window.scrollY > 0){
		nav.classList.add('stiky')
	}else{
		nav.classList.remove('stiky')
	}

})
// responsive nav bar 
let btn = document.querySelector('.button-menu')

btn.addEventListener('click', e => {
	nav.classList.toggle('active')
})