function hexToBase64(str) {
    return btoa(String.fromCharCode.apply(null, str.replace(/\r|\n/g, "").replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ")));
}
$(function () {
    $(document).on("click", "#goodluck", function(){
        $.post("/",
        {
            cleartext: $('#cleartext').val(),
        },
        function(data,status){
            var img = document.createElement('img');
            img.src = 'data:image/jpeg;base64,' + data;
            img.setAttribute('class', 'center-block')
            $('#diplay_area').html(img)
            //alert("Data: " + data + "\nStatus: " + status);
            $('#request_button').html('<button id="revive" class="btn btn-success">Revive!</button>')
        }
        );
    });
    $(document).on("click", "#revive", function(){
        location.reload();
    });
    $(document).keydown(function(e) {
        if ((e.ctrlKey && e.shiftKey) || (e.metaKey && e.shiftKey)) {
            switch(e.which) {
                case 86: // V
                $('#clueModal').modal('toggle');
                break;

                default: return;
            }
            e.preventDefault(); // prevent the default action
        }
    });
    $("#reg_button").click(function() {
        $('#register').modal('toggle');
    });
    $("#signin_button").click(function() {
        $('#signin').modal('toggle');
    });
});
