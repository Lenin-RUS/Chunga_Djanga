// ajax
$(document).on('click', '#ajax-button', function(event) {
console.log ('step 1');
        $.ajax({
        url: '/users/update-token-ajax/',
        success :function(data) {
        console.log(data);
        $('#token').html(data.key);
        }

})
})