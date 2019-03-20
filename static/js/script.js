$(document).ready(function() {
    console.log("ready!");

    $('#myModal').on('shown.bs.modal', function() {
        $('#myInput').focus()
    })

    /*
    $('.stripe-button-el').hide()

    $('#id_ticket_type').click(function() {
        if ($(this).val() === "Feature") {
            $(this).siblings('.btn-default').hide()
            $(this).siblings('.stripe-button-el').show()
            console.log("Stripe button display")
        }
        else if ($(this).val() === "Bug") {
            $(this).siblings('.btn-default').show()
            $(this).siblings('.stripe-button-el').hide()
            console.log("Stripe button removed")
        };
    });
    */

});
