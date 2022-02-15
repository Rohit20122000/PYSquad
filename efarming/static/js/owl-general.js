(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {
        jQuery('.owl-carousel').each(function () {
            var jQuerycarousel = jQuery(this);
            jQuerycarousel.owlCarousel({
                items: jQuerycarousel.data("items"),
                loop: jQuerycarousel.data("loop"),
                margin: jQuerycarousel.data("margin"),
                nav: jQuerycarousel.data("nav"),
                dots: jQuerycarousel.data("dots"),
                autoplay: jQuerycarousel.data("autoplay"),
                autoplayTimeout: jQuerycarousel.data("autoplay-timeout"),
                navText: ['<div class="css_prefix-leftarrow"><div class="left-arrow tringle"></div><i class="fas fa-caret-left"></i> </div>', '<div class="css_prefix-rightarrow"><div class="right-arrow tringle"></div><i class="fas fa-caret-right"></i></div>'],
                responsiveClass: true,
                responsive: {
                    // breakpoint from 0 up
                    0: {
                        items: jQuerycarousel.data("items-mobile-sm"),
                        nav: false,
                        dots: true
                    },
                    // breakpoint from 480 up
                    480: {
                        items: jQuerycarousel.data("items-mobile"),
                        nav: false,
                        dots: true
                    },
                    // breakpoint from 786 up
                    786: {
                        items: jQuerycarousel.data("items-tab"),
                        nav: false,
                        dots: true
                    },
                    // breakpoint from 1023 up
                    1023: {
                        items: jQuerycarousel.data("items-laptop"),
                        nav: true,
                        dots: true
                    },
                    1100: {
                        items: jQuerycarousel.data("items-large"),
                    },
                    1299: {
                        items: jQuerycarousel.data("items"),
                    }
                }
            });
        });
		window.dispatchEvent(new Event('resize'));
    });
})(jQuery);