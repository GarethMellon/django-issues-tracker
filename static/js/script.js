$(document).ready(function() {
    console.log("ready!");

    $('.stripe-button-el').hide()

    $('#myModal').on('shown.bs.modal', function() {
        $('#myInput').focus()
    })

    $('#id_ticket_type').click(function() {
        if ($(this).val() === "Feature") {
            $(this).siblings('.btn-default').hide()
            $(this).siblings('.stripe-button-el').show()
        }
        else if ($(this).val() === "Bug") {
            $(this).siblings('.btn-default').show()
            $(this).siblings('.stripe-button-el').hide()
        }
        else {
            $(this).siblings('.btn-default').show()
            $(this).siblings('.stripe-button-el').hide()
        };
    })
});
