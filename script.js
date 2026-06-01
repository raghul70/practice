let picker = document.getElementById("colorPicker");

picker.addEventListener("input", function () {
    document.body.style.backgroundColor = picker.value;
});