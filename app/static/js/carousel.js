(function($) {
    $(function() {
        $('.jcarousel').jcarousel();

        $('.jcarousel-control-prev')
            .on('active.jcarouselcontrol', 'keydown', function() {
                $(this).removeClass('inactive');
            })
            .on('inactive.jcarouselcontrol', 'keydown', function() {
                $(this).addClass('inactive');
            })
            .jcarouselControl({
                target: '-=1'
            });

        $('.jcarousel-control-next')
            .on('active.jcarouselcontrol', function() {
                $(this).removeClass('inactive');
            })
            .on('inactive.jcarouselcontrol', function() {
                $(this).addClass('inactive');
            })
            .jcarouselControl({
                target: '+=1'
            });

        $(document)
            .on('keydown', function(event) {
                if (event.which == 37) {
                    $('.jcarousel').jcarousel('scroll', '-=1');
                }
                else if (event.which == 39) {
                    $('.jcarousel').jcarousel('scroll', '+=1');
                }
            });

        $('.jcarousel-pagination')
            .on('active.jcarouselpagination', 'a', function() {
                $(this).addClass('active');
            })
            .on('inactive.jcarouselpagination', 'a', function() {
                $(this).removeClass('active');
            })
            .jcarouselPagination();

    });
})(jQuery);
