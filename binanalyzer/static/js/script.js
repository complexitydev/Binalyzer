$(function () {
    $("#dropbox").on('click', function (e) {
        e.preventDefault();
        $("#upload_button").trigger('click');
    });
    $("#upload_button").change(function (e) {
        $("#upload_form").submit();
    });
});