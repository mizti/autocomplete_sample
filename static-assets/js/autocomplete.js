//$(document).ready(function(){
$(function(){
  $('#example-search-input').autocomplete({
      //source: data,
      source: function( req, res ) {
          $.ajax({
              type: "GET",
              url: "/autocomplete/" + encodeURIComponent(req.term.replace(/[^a-zA-Z0-9]/g, '').toLowerCase())+ "/",
              dataType: "json",
          }).done(function(data) {
              console.log(encodeURIComponent(req.term.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()));
              var i = 0;
              for (i = 0; i < data.length; i++) {
                  strCombRegex = req.term.replace(/[^a-zA-Z0-9]/ig, '').toLowerCase();
                  regexp = new RegExp(strCombRegex + '(.*?)', 'g'),
                  target = data[i].replace(/[^a-zA-Z0-9]/ig, '').toLowerCase();
                  if(!target.match(regexp)){
                      data.splice(i, 1);
                      i--;
                  }
              }
              res(data);
          }).fail(function(data) {
              //console.log('error!');
              //console.log(data);
          });
      },
      autoFocus: true,
      delay: 50,
      minLength: 1 
  });
});
