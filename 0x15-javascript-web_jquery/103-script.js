$(document).ready(() => {
  function fetchTranslation () {
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
  }
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
  $('INPUT#btn_translate').on('click', fetchTranslation);
});
