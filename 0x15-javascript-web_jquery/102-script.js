$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const languageCode = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'GET',
      data: { lang: languageCode },
      success: function (data) {
        $('DIV#hello').text(data.hello);
      },
      error: function (err) {
        console.log(err);
      }
    });
  });
});
