(function (jQuery) {
    "use strict";
    
    jQuery(document).ready(function () {
        if (jQuery('.css_prefix-loadmore').length >= 1) {
            let css_prefixMasonryEle = jQuery('.css_prefix-loadmore-block');
            if (css_prefixMasonryEle.length > 0) {
                css_prefixMasonryEle.isotope({
                    itemSelector: '.css_prefix-loadmore-item',
                    percentPosition: true,
                    HorizontalMode: true,
                    resizable: true,
                    layoutMode: 'masonry',
                    masonry: {
                        gutterWidth: 0
                    },
                });
            }

            jQuery(document).find('.css_prefix-loadmore-block').each(function () {
                let counter = jQuery(this).closest('.css_prefix-with-loadmore').data('loadmore-item');
                isotopeLoadMore(jQuery(this), counter); //execute function onload
            });
        }

        jQuery(document).on("click", ".load-more-pf", function (e) {
            e.preventDefault();
            let counter = parseInt(jQuery(this).closest('.css_prefix-with-loadmore').data('loadmore-item')) + parseInt(jQuery(this).closest('.css_prefix-with-loadmore').data('loadmore-count'));
            jQuery(this).closest('.css_prefix-with-loadmore').data('loadmore-count', counter);
            isotopeLoadMore(jQuery(this), counter); //execute function onload
        });
    });

    function isotopeLoadMore(element, toShow) {
        let $container = element.closest('.css_prefix-with-loadmore').find('.css_prefix-loadmore-block');
        let ele = $container.find('.css_prefix-loadmore-item').addClass('loadmore-hidden-items');
        ele.parent().find(".loadmore-hidden-items").removeClass("loadmore-hidden-items");
        let iso = $container.data('isotope');
        let hiddenElems = iso.filteredItems.slice(toShow, iso.filteredItems.length).map(function (item) {
            return item.element;
        });
        jQuery(hiddenElems).addClass('loadmore-hidden-items');

        //when no more to load, hide show more button
        if (jQuery(hiddenElems).length === 0) {
            element.closest('.css_prefix-with-loadmore').find(".load-more-pf").hide();
        } else {
            element.closest('.css_prefix-with-loadmore').find(".load-more-pf").show();
        }
        $container.isotope('layout');
    }
    
})(jQuery);