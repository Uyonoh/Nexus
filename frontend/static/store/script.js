$(document).ready(function() {
    $('.rgb-text').each(function() {
        var element = $(this);
        var text = element.text();
        element.empty();
        for (var i = 0; i < text.length; i++) {
            var char = text[i];
            var span = $('<span>').text(char).css({
                'color': 'white',
                'text-shadow': '-1px 0 red, 0 1px green, 1px 0 blue'
            });
            element.append(span);
        }
    });
});
