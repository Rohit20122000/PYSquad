/*------------------------
Accordion
--------------------------*/
(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {
       
        jQuery('.css_prefix-accordion .css_prefix-accordion-block .css_prefix-accordion-details').hide();
        jQuery('.css_prefix-accordion .css_prefix-accordion-block:first').addClass('css_prefix-active').children().slideDown('slow');
        jQuery('.css_prefix-accordion .css_prefix-accordion-title').on("click", function () {
            let ele = jQuery(this).parent().hasClass('css_prefix-active');
            jQuery('.css_prefix-accordion .css_prefix-accordion-block').removeClass('css_prefix-active').children('div.css_prefix-accordion-details').slideUp('slow');
            if (ele) {
                jQuery(this).parent().removeClass('css_prefix-active');
            }else{
                jQuery(this).parent().addClass('css_prefix-active').children('div.css_prefix-accordion-details').slideDown('slow');
            }
        }); 
    });
})(jQuery);


