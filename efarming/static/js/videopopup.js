/*----------------
Video Popup
---------------------*/
(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {
        if (jQuery('.popup-youtube').length > 0) {
            jQuery('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
                disableOn: 700,
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false
            });
        }
        
    });

})(jQuery);