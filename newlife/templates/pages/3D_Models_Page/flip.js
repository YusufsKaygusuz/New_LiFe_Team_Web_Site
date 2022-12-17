document.querySelectorAll('.flip-card-click .flip-card-inner').forEach(function (item) {
    item.addEventListener('keypress', function (evt) { if (evt.keyCode == 13 || evt.keyCode == 32) { item.click(); } });
});

document.querySelectorAll('.flip-card-click').forEach(function (item) {
    item.addEventListener('click', function () { this.classList.toggle('flipped'); });
});