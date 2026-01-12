// HTML Elements
const LED_arr = []
for (let i=0;i<64;i++) {
    LED_arr.push(false)
}

const LED_container = document.querySelector(".LED_container")
for (let r=0;r<8;r++) {
    const row = document.createElement("div")
    row.classList.add("LED_row")
    for (let c=0;c<8;c++) {
        const LED = document.createElement("button")
        LED.classList.add("LED")
        LED.addEventListener("click", (e) => {
            LED.classList.toggle('LED_toggled')
            LED_arr[LED.id] = !LED_arr[LED.id]
            postLEDArr()
        })
        LED.id = r*8 + c
        row.appendChild(LED) 
    }
    LED_container.appendChild(row)
}

// Methods
function postLEDArr() {
    fetch('/', {
        headers: {
        "Content-Type": "application/json"
        },
        method:"POST",
        body:JSON.stringify(LED_arr)
    })
}

postLEDArr()