(function (jQuery) {
    "use strict";
    jQuery(document).ready(function () {

        callCircleChart();

    });

})(jQuery);

function callCircleChart(){

    if (jQuery('.circleChart').length > 0) {

        jQuery('.circleChart').each(function () {
            jQuery(this).circleChart({
                size: jQuery(this).data('size'),
                color: jQuery(this).data('color'),
                backgroundColor: jQuery(this).data('background'),
                speed: jQuery(this).data('speed'),
                startAngle: jQuery(this).data('angle'),
                value: jQuery(this).data('value'),
                widthRatio: jQuery(this).data('ratio'),
                lineCap: jQuery(this).data('linecap'),
                counterclockwise: jQuery(this).data('direction'),
                text: 0,

                onDraw: function (el, circle) {
                    circle.text(Math.round(circle.value) + "%");
                }
            });
        });

    }

}
