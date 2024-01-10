const $results = $('UL#list_movies');
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: (data) => {
    $.each(data.results, function (i, data) {
      $results.append(`<li>${data.title}</li>`);
    });
  }
});
