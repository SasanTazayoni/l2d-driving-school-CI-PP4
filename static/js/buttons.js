const authBtns = document.querySelectorAll('.auth-button')
const blueBtns = document.querySelectorAll('.blue-button')

authBtns.forEach(btn => {
    btn.onmousemove = function(e) {
        let x = e.pageX - btn.offsetLeft
        let y = e.pageY - btn.offsetTop

        btn.style.setProperty('--x', x + 'px')
        btn.style.setProperty('--y', y + 'px')
    }
})

console.log(blueBtns)

blueBtns.forEach(btn => {
    btn.addEventListener('mouseover', function (e) {
        let x = e.clientX - e.target.getBoundingClientRect().left
        let y = e.clientY - e.target.getBoundingClientRect().top
        let ripples = document.createElement('span')
        ripples.style.left = x + 'px'
        ripples.style.top = y + 'px'
        this.appendChild(ripples)

        setTimeout(() => {
            ripples.remove()
        }, 600)
    })
})