$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, films) {
        $('UL#list_movies').append(`<li>${films.title}</li>`);
      });
    }
  });
});
