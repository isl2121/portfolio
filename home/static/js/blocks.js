/******************************************************************
	
	
	@ Item          Legendary // One Page Parallax HTML Template 
	@ Author		Avanzare
	@ Website		http://themeforest.net/user/avanzare 
	

 ******************************************************************/
 
 
 /******************************************************************


	------------------------
	-- TABLE OF CONTENTS --
	------------------------
	
	--  1. Work
	--  2. Process
	--  3. Team
	--  4. News
	--  5. Contact
 
 
 ******************************************************************/




/** 1. WORK
*******************************************************************/

$( document ).ready(function() {
     "use strict";



	// WORK GRID ( Cube Plugin )
    $(".work-grid").cubeportfolio({
        filters: "#js-filters-masonry",
        layoutMode: "grid",
        defaultFilter: "*",
        animationType: "quicksand",
        gapHorizontal: 50,
        gapVertical: 50,
		auto: true,
		sortToPreventGaps: true,
		loadMore: "#work-loadmore",
        loadMoreAction: "click",
        gridAdjustment: "responsive",
        mediaQueries: [{
            width: 1500,
            cols: 3
        }, {
            width: 1100,
            cols: 3
        }, {
            width: 800,
            cols: 3
        }, {
            width: 480,
            cols: 2
        }, {
            width: 320,
            cols: 1
        }],
        caption: "revealTop",
        displayType: "default",
        displayTypeSpeed: 70,
        lightboxDelegate: ".cbp-lightbox",
        lightboxGallery: false,
        lightboxTitleSrc: "data-title",
        singlePageDelegate: ".cbp-singlePage",
        singlePageDeeplinking: false,
		singlePageAnimation: "fade",
        singlePageStickyNavigation: false,
        singlePageCallback: function(url, element) {
            var t = this;
            $.ajax({
                    url: url,
                    type: "GET",
                    dataType: "html",
                    timeout: 10000
                })
                .done(function(result) {
                    t.updateSinglePage(result);
                })
                .fail(function() {
                    t.updateSinglePage("AJAX Error! Please refresh the page!");
                });
        },
		
    });



/** 2. PROCESS
*******************************************************************/
	 
	 
	 
	 // PROCESS SLIDER ( Cube Plugin )
	 $(".slider-process").cubeportfolio({
        layoutMode: "slider",
        drag: true,
        auto: false,
        showNavigation: false,
        showPagination: true,
        rewindNav: false,
        scrollByPage: false,
		singlePageDelegate: null,
        gridAdjustment: "responsive",
        mediaQueries: [{
            width: 1500,
            cols: 1
        }],
        gapHorizontal: 0,
        gapVertical: 700,
        caption: "opacity",
        displayType: "fadeIn",
        displayTypeSpeed: 100,
    });
	
	
	function animateProcess() {
		
		var isDown = false;
		
		$(".slider-process .cbp-wrapper").mousedown(function(){
         
			$(".slider-process .cbp-wrapper .process-info-box").removeClass("active");
			isDown = true;
			
		});
		
		$(document).mouseup(function(){
			
			if(isDown){
				
				setTimeout(function(){
					
					$(".slider-process .cbp-wrapper .process-info-box").addClass("active");
					isDown = false;
					
				}, 500);
				
			}
			
		}); 
	
	
	} animateProcess();



/** 3. TEAM
*******************************************************************/ 
	 
	 
	 
	// TEAM SLIDER ( Cube Plugin )
    $(".slider-team").cubeportfolio({
		
        layoutMode: "slider",
        drag: true,
        auto: false,
        autoTimeout: 5000,
        autoPauseOnHover: true,
        showNavigation: false,
        showPagination: true,
        rewindNav: true,
        scrollByPage: true,
        gridAdjustment: "responsive",
        mediaQueries: [{
            width: 800,
            cols: 3
        }, {
            width: 480,
            cols: 2
        }, {
            width: 320,
            cols: 1
        }],
        gapHorizontal: 0,
        gapVertical: 50,
        caption: "revealTop",
        displayType: "fadeIn",
        displayTypeSpeed: 400,
		
		singlePageInlineDelegate: ".cbp-singlePageInline",
        singlePageInlinePosition: "bottom",
		singlePageDelegate: null,
        singlePageInlineInFocus: false,
        singlePageInlineCallback: function(url, element) {
            var t = this;
            $.ajax({
                    url: url,
                    type: "GET",
                    dataType: "html",
                    timeout: 10000
                })
                .done(function(result) {

                    t.updateSinglePageInline(result);

                })
                .fail(function() {
                    t.updateSinglePageInline("AJAX Error! Please refresh the page!");
                });
        },	
		
    });



/** 4. NEWS
*******************************************************************/
	 
	 
	 
	// NEWS SLIDER ( Cube Plugin )
    $(".news-slider").cubeportfolio({
        layoutMode: "slider",
        drag: true,
        auto: false,
        showNavigation: false,
        showPagination: true,
        rewindNav: true,
        scrollByPage: true,
        gridAdjustment: "responsive",
        mediaQueries: [{
            width: 800,
            cols: 2
        }, {
            width: 480,
            cols: 1
        }, {
            width: 320,
            cols: 1
        }],
        gapHorizontal: 0,
        gapVertical: 50,
        caption: "",
        displayType: "fadeIn",
        displayTypeSpeed: 400,
		singlePageDelegate: null,
    });




/** 5. CONTACT
*******************************************************************/
	 
	 
	 
	 //CONTACT FORM
	 $("#contact-form").submit(function(e) {
		 
		e.preventDefault();
	    var postdata = $(this).serialize();
		
	    $.ajax({
	        type: "POST",
	        url: "assets/contact.php",
	        data: postdata,
	        dataType: "json",
	        success: function(json) {
				 
				$("#contact-form .form-group").removeClass("error");
				
				setTimeout(function(){
					
					if (json.nameMessage !== "") {
						
						$("#contact-form-name").parent().addClass("error");
						
					}
					
					if (json.emailMessage !== "") {
						
					   $("#contact-form-email").parent().addClass("error");
					   
					}
					
					if (json.subjectMessage !== "") {
						
					   $("#contact-form-subject").parent().addClass("error");
					   
					}
					
					if (json.messageMessage !== "") {
						
						$("#contact-form-message").parent().addClass("error");
						
					}
					
				}, 50);
					
				if (json.nameMessage === "" && json.emailMessage === "" && json.subjectMessage === "" && json.messageMessage === "") {
					
					$("#contact-form").addClass("success");
					$("#contact-form button span").removeClass("ti-arrow-right").addClass("ti-check");
					
					$("#contact-form input").attr("placeholder", "");
					$("#contact-form-message").attr("placeholder", json.succesMessage);
					
					$("#contact-form input,#contact-form button").val("").prop("disabled", true);
				}
	        }
			
	    });
		
	});

	// CONTACT BUTTON HOVER ADD/REMOVE CLASS
	$("#contact form button").hover(
	  
	  function() {
		  
		$("#contact form .form-group.button-container").addClass("move");
		
	  }, function() { 
	  
		$("#contact form  .form-group.button-container").removeClass("move");
		
	  }
	  
	);
	
	// FORM GROUP ADD CLASS WHEN INPUT IS FOCUSED
	$("#contact form input").focusin(function() {
		
		$(this).parent(".form-group").addClass("switch-color");
		
	});
	
	// FORM GROUP REMOVE CLASS WHEN INPUT IS NOT FOCUSED
	$("#contact form input").focusout(function() {
		
		$(this).parent(".form-group").removeClass("switch-color");
		
	});
	
	// CHANGING HEIGHT OF ELEMENT ON WINDOW RESIZE 
	$(window).on("resize", function(){
		
		$("#contact .map-wrapper").css("height",$("#contact .map-wrapper").width()*0.8);
		
	});
	
	// CHANGING HEIGHT OF ELEMENT WHEN TAB ( BOOTSTRAP) IS SHOWN 
	$('a[data-toggle="tab"]').on("shown.bs.tab", function () {
		
		$("#contact .map-wrapper").css("height",$("#contact .map-wrapper").width()*0.8);
		
	});

	
	// OPEN/CLOSE POPUP DESCRIPTION ON BUTTON CLICK
	$("body").on("click",".tab-content .map-wrapper .button-description", function(){
		
		if ($(".tab-content .map-wrapper .button-description").hasClass("active")) {
			
			$(".tab-content .map-wrapper .container-info").removeClass("active");
			$(".tab-content .map-wrapper .button-description").removeClass("active");
		  
		} else {
			
			$(".tab-content .map-wrapper .button-description").addClass("active");
		    $(".tab-content .map-wrapper .container-info").addClass("active");
			
		}
		
	});
	
	// CLOSE POPUP DESCRIPTION WHEN OTHER CONTENT IS CLICK
	$("body").on("mousedown","#map", function(){
		
		if ($(".tab-content .map-wrapper .button-description").hasClass("active")) {
			
			setTimeout(function() {	
			
				$(".tab-content .map-wrapper .container-info").removeClass("active");
				$(".tab-content .map-wrapper .button-description").removeClass("active");
				
			}, 100);
			 
		}
		
	});

	
		
});