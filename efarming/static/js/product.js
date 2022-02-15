/*----------------
Count Down Timer
---------------------*/
(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {
        
        /*------------------------------
        filter items on button click
        -------------------------------*/
        
        jQuery('.iq-masonry').isotope({
            itemSelector: '.iq-masonry-item',
            filter: jQuery('.isotope-filters button:first-child').attr('data-filter')
        });

        jQuery('.isotope-filters').on('click', 'button', function () {
            var filterValue = jQuery(this).attr('data-filter');
            jQuery('.iq-masonry').isotope({
                resizable: true,
                filter: filterValue
            });
            jQuery('.isotope-filters button').removeClass('show active');
            jQuery(this).addClass('show active');
        });
        
    });

})(jQuery);
