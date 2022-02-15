/*----------------
Count Down Timer
---------------------*/
(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {
        if(jQuery('.timer').length > 0)
        {
            jQuery('.timer').countTo();
        }
        
    });

})(jQuery);