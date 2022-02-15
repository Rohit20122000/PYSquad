(function (jQuery) {
	"use strict";
	jQuery(document).ready(function () {
		// Multi slider 
		
		// style 2 [ Slider thumb Slide ]
		jQuery('.testimonial-slider.slider-nav').slick({
			slidesToShow: 3,
			slidesToScroll: 1,
			asNavFor: '.slider-for',
			dots: false,
			arrows: false,
			focusOnSelect: true,
			responsive: [
				{
				  breakpoint: 767,
				  settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				  }
				},
			]
		});
		// Style 2 [ Slider normal slide ]
		jQuery('.testimonial-slider.slider-for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: true,
			fade: false,
			dots: false,
			focusOnSelect: true,
			asNavFor: '.slider-nav',
			appendArrows: '.testimonial-arrow'
		});

		// Style 1 & 3 
		jQuery('.testimonial-sliders').each(function () {
			
		jQuery('.testimonial-sliders').slick({
			slidesToShow: jQuery(this).data("items"),
			slidesToScroll: jQuery(this).data("items"),
			infinite: jQuery(this).data('loop'),
			autoplay: jQuery(this).data('autoplay'),
			dots: false,
			arrows: jQuery(this).data("nav"),
			focusOnSelect: true,
			prevArrow: '<div class="iq-swiper-arrow"><div class="swiper-button-prev"><i class="fas fa-caret-left"></i></div></div>',
			nextArrow: '<div class="iq-swiper-arrow"><div class="swiper-button-next"><i class="fas fa-caret-right"></i></div></div>',
			responsive: [
				{
					breakpoint: 480,
					settings: {
					slidesToShow: jQuery(this).data("items-mobile"),
					slidesToScroll: jQuery(this).data("items-mobile"),
				  }
				},
				{
					breakpoint: 786,
					settings: {
					slidesToShow: jQuery(this).data("items-tab"),
					slidesToScroll: jQuery(this).data("items-tab"),
				  }
				},
				{
					breakpoint: 1023,
					settings: {
						slidesToShow: jQuery(this).data("items-laptop"),
						slidesToScroll: jQuery(this).data("items-laptop"),
					}
				},
				{
					breakpoint: 1199,
					settings: {
						slidesToShow: jQuery(this).data("items"),
						slidesToScroll: jQuery(this).data("items"),
					}
				}
			  ]
		});
	});

	});
})(jQuery);