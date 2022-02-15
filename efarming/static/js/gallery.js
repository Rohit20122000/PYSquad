(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {
        jQuery('.css_prefix-gallery .owl-carousel').each(function () {
            var jQuerycarousel = jQuery(this);
            jQuerycarousel.owlCarousel({
                items: 3, 
                loop: jQuerycarousel.data("loop"),
                margin: jQuerycarousel.data("margin"),
                nav: jQuerycarousel.data("nav"),
                dots: jQuerycarousel.data("dots"),
                autoplayTimeout: jQuerycarousel.data("autoplay-timeout"),
                autoplay: false,
                center: true,
                navText: ['<div class="css_prefix-leftarrow"><div class="left-arrow tringle"></div><i class="fas fa-chevron-left"></i> </div>', '<div class="css_prefix-rightarrow"><div class="right-arrow tringle"></div><i class="fas fa-chevron-right"></i></div>'],
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                        nav: false,
                        dots: true
                    },                        
                    675: {
                        items: 2,
                        nav: false,
                        dots: true
                    },
                    1025: {
                        items: 3
                    },
                    1441: {
                        items: 3
                    },
                }
            });
        });
        window.dispatchEvent(new Event('resize'));

        /*------------------------
        Masonry
        --------------------------*/

        if (jQuery('.iqonic-masonry-grid').length > 0) {

            jQuery('.iqonic-masonry-grid').each(function () {
                jQuery(".iqonic-masonry-block").imagesLoaded(function () {
                    jQuery(".iqonic-masonry-grid").masonry({
                        columnWidth: ".grid-sizer",
                        itemSelector: ".iqonic-masonry-item",
                    });
                });

            });
        }
    });
})(jQuery);