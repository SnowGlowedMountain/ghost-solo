window.addEventListener("scroll", () => {
    const scrolled = window.scrollY
    if (scrolled > 150) {
        document.querySelector("header").style.background = "#020202"
    }
    else {
        document.querySelector("header").style.background = "transparent"
        
    }
})

const burger = document.querySelector(".burger")

burger.addEventListener("click", () => {
    document.querySelector(".mobile-menu").style.display = "flex"
})

document.querySelector(".x").addEventListener("click", () => {
    document.querySelector(".mobile-menu").style.display = "none"
})

let expanded = false

document.querySelector(".mobile-a").addEventListener("click", () => {
    if (!expanded) {
        expanded = true
        document.querySelector(".mobile-expansion").style.display = "flex"
    }
    else {
        expanded = false
        document.querySelector(".mobile-expansion").style.display = "none"
    }
})

// document.querySelector("#bgsec").style.top = `${document.querySelector("#hero").offsetHeight +
// document.querySelector("#featuredListings").offsetHeight +document.querySelector("#austin").offsetHeight +
// document.querySelector("#testimonials").offsetHeight}px`

// // const hoverDivs = document.querySelectorAll("div:has(div:has(.underline)>.underline)")
// const underlines = document.querySelectorAll(".underline")

// // hoverDivs.forEach((div, i)=>{
// //     div.addEventListener("mouseover", ()=>{
// //         underlines[i].style.left = "0"
// //         underlines[i].style.right = "0"
// //         underlines[i].style.transform = "none"
// //     })
// // })

// underlines.forEach(underline => {
//     const siblingLinks = Array.from(underline.parentNode.children).filter(child => child.tagName === 'A' && !child.classList.contains('underline'));
//     console.log(siblingLinks)
//     siblingLinks.forEach((link, i) => {
//         link.addEventListener("mouseover", () => {
//             underlines[i].style.left = "0"
//             underlines[i].style.right = "0"
//             underlines[i].style.transform = "none"
//         })
//     });
// });