$(document).ready(function(){
    $("#columnthree").attr("style", "width: 290px; height: 523px;");
    $(".galleryimage").click(function(){
        var image = $(this).attr("style");
        var link = $(this).attr("alt");
        $(".mainimg").attr("style", image);
        $(".mainimglink").attr("href", "/catalogue/" + link);
    });
    $(".tagged_animal_link").mouseover(function(){
        var slug = $(this).attr("id");
        $('.' + slug).attr("class", slug + " selected");
    });
    $(".tagged_animal_link").mouseout(function(){
        var slug = $(this).attr("id");
        $('.' + slug).attr("class", slug);
    }); 
    $("#storycontent a").mouseover(function(){
        var slug = $(this).attr("class");
        $("#" + slug + "image").css("opacity", "1");
    });
    $("#storycontent a").mouseout(function(){
        var slug = $(this).attr("class");
        $("#" + slug + "image").css("opacity", "");
    });
    var contheight = $("#imagecontainer").height();
    var propheight = 455.0;
    var ratio = propheight/contheight;
    var imgheight = $(".tagged_animal_image").height() * ratio;
    var newpads = 10.0 * ratio;
    $(".tagged_animal_image").css({
        'height': imgheight,
        'margin-bottom': newpads
    });
    $("#imagecontainer").css({
        'height': propheight,
        'padding': newpads
    });
    $("#dictname").click(function(){
		$("#listcontainer").css("-moz-transform", "translate(0, 0)");
	});
	$("#dictspecies").click(function(){
      		$("#listcontainer").css("-moz-transform", "translate(-608px, 0)");
	});
  	$("#dictcountry").click(function(){
      		$("#listcontainer").css("-moz-transform", "translate(-1216px, 0)");
   	});
   	$("#dictage").click(function(){
      		$("#listcontainer").css("-moz-transform", "translate(-1824px, 0)");
   	});
   	$("#dictgender").click(function(){
      		$("#listcontainer").css("-moz-transform", "translate(-2432px, 0)");
   	});
	$("#nav1").click(function(){
		$("#carouselcontainer").css("-moz-transform", "translate(0, 0)");
	});
	$("#nav2").click(function(){
      		$("#carouselcontainer").css("-moz-transform", "translate(-265px, 0)");
	});
  	$("#nav3").click(function(){
      		$("#carouselcontainer").css("-moz-transform", "translate(-530px, 0)");
   	});
   	$("#nav4").click(function(){
      		$("#carouselcontainer").css("-moz-transform", "translate(-795px, 0)");
   	});
   	$("#nav5").click(function(){
      		$("#carouselcontainer").css("-moz-transform", "translate(-1060px, 0)");
   	});    
   	$("#nav11").click(function(){
      		$("#personalitycontainer").css("-moz-transform", "translate(0, 0)");
   	});
   	$("#nav22").click(function(){
      		$("#personalitycontainer").css("-moz-transform", "translate(-608px, 0)");
   	});
	$(function()
	{
		$('.namesort, .gendersort, .agesort, .countrysort, .speciesort, .facts11, .facts22, .facts1, .facts2, .facts3, .facts4, #columnthree, #hmlcont').jScrollPane({enableKeyboardNavigation: false, gutter: 10});
	});
    $(function()
	{
		$('#storycontainer').jScrollPane({enableKeyboardNavigation: false, verticalGutter: 10});
	});
});

