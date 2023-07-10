document.getElementById('en').addEventListener('click', function (event) {
    document.getElementsByName('next')[0].value = '/en' + window.location.pathname.substring(3);
});
document.getElementById('bg').addEventListener('click', function (event) {
    document.getElementsByName('next')[0].value = '/bg' + window.location.pathname.substring(3);
});
