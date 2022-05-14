$(document).ready(function () {
    $('.js-predict-btn').on('click', function () {
        let $button = $('.js-predict-btn');
        $button.prop('disabled', true);

        let $form = $('.js-predict');
        let data = new FormData($form.get(0));

        let $preloader = $('.js-predict__preloader');
        $preloader.removeClass('m-display__none');

        $.ajax({
            url: $form.attr('action'),
            type: $form.attr('method'),
            data: data,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            success: function (response) {
                $('.js-predicted').removeClass('m-display__none')
                $('.js-predicted__audio').removeClass('m-display__none');
                $('.js-predicted__audio audio').attr('src', response.path_to_audio)
                $('.js-predicted__genre').text(response.predicted_genre);
            },
            complete: function () {
                $button.prop('disabled', false);
                $preloader.addClass('m-display__none');
            }
        });
    });

    $('.js-train-btn').on('click', function () {
        $button = $(this);
        $button.prop('disabled', true);

        let $form = $('.js-train');
        let data = $form.serialize();

        let $success = $('.js-train__success');
        $success.addClass('m-display__none');
        $success.text('');

        let $preloader = $('.js-train__preloader');
        $preloader.removeClass('m-display__none');

        $.ajax({
            url: $form.attr('action'),
            type: $form.attr('method'),
            data: data,
            dataType: 'json',
            success: function (response) {
                $success.text(response.message);
            },
            complete: function () {
                $preloader.addClass('m-display__none');
                $success.removeClass('m-display__none');
                $button.prop('disabled', false);
            }
        });
    });
});
