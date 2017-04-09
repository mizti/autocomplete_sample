//$(document).ready(function(){
$(function(){
  $('#example-search-input').autocomplete({
      //source: data,
      source: function( req, res ) {
          $.ajax({
              type: "GET",
              url: "/autocomplete/" + encodeURIComponent(req.term.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()),
              dataType: "json",
          }).always(function(data) {
              console.log(data);
              res(data);
              console.log('always!');
          }).fail(function(data) {
              console.log('error!');
              console.log(data);
          });
      },
      autoFocus: true,
      delay: 50,
      minLength: 1 
  });
});
