const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// auto hiding the messages
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);
