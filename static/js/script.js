$(document).ready(function() {
    console.log("ready!");

    $('#myModal').on('shown.bs.modal', function() {
        $('#myInput').focus()
    })

    if ($('.container.info-bar').length >0) {
        $('#div_id_ticket_type').hide()
        $('#div_id_ticket').hide()
        $('#div_id_comment_type').hide()
        console.log("Hide Ticket Type")
    };
});
