$(document).ready(function(){
 $("#pie").click(function(){
    var item = $('#input').val();
    $('#boxes').append("<p class="box">"+item+"</p>");
 });
});
