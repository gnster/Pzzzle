$(document).ready(function() {
  $('.uploader').click(function(){
    //Begin loading of all stuff
    $.get($(this).attr('href'), function(data) {
      $('#uploader').html(data).show();
      
      $('#uploader .submit').click(function() {
        //Disable layer. Maybe send via ajax?
      });
    });
  });
});

function upload_complete(id, url) {
  $(id).attr('src') = url + '?math=' + Math.random();
  $('#uploader').hide();
}
