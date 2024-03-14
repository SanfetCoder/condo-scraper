// element
const condoLists = document.getElementById("condoList");
const form = document.getElementById("form");
const inputLocation = document.getElementById("inputLocation");
const searchButton = document.getElementById('searchButton')
// handle event
searchButton.addEventListener("click", function(event){
    event.preventDefault();
    if (!inputLocation.value) return alert("กรุณาใส่ตำแหน่งที่ตั้ง")
    window.location.href = `?province=${encodeURIComponent(inputLocation.value)}`
})