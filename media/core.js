$(document).ready(function() {
  $('.uploader').click(function(){
    //Begin loading of all stuff
    $.get($(this).attr('href'), function(data) {
      $('#uploader').html(data).show();
      
      $('#uploader .submit').click(function() {
        //Disable layer. Maybe send via ajax?
      });
    });
    return false;
  });
});

function upload_complete(id, url) {
  $(id).attr('src') = url + '?math=' + Math.random();
  $('#uploader').hide();
}

$(window).load(function(){

    buildThumbs($('#imagery-outer'));
    
    function buildThumbs($elem){
        var $wrapper=$elem;
        var $menu=$wrapper.find('#imagery-inner');
        var inactiveMargin=700;
        $wrapper.bind('mousemove1',function(e){
            var wrapperWidth=$wrapper.width();
            var menuWidth=$menu.width()+2*inactiveMargin;
            var left=(e.pageX-$wrapper.offset().left)*(menuWidth-wrapperWidth)/wrapperWidth-inactiveMargin;
            $wrapper.scrollLeft(left);
        });}
    
    $('.cell').click(function(){
        console.log('show');
        $('.cell').removeClass('cell_show');
        $(this).addClass('cell_show');
        return false;
    });
});

function lock(x, y){
    console.log('CLICK');
    $.get('/lock', {x: x, y: y}, function(result){
                if(result == 'success'){
                    $('#control_'+x+'_'+y).html('10 min <img src="/media/i/protected.png">');
                }else{
                    alert(result);
                }                    
            });
    return false;
}
