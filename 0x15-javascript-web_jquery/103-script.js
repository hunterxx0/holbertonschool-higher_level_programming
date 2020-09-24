$(document).ready(function () {
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
      return false;
    }
  });
  $('#btn_translate').click(function () {
    $.get(('https://fourtonfish.com/hellosalut/?lang=' +
         $('#language_code').val()), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
