const $results = $('UL#list_movies');
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, data) {
    $results.append(`<li>${data.title}</li>`);
  });
});
