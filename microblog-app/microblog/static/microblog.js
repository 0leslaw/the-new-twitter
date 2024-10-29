$(document).ready(function() {
    $('.original').hover(
        function() {
            // var form = $(
            //     // <form action="{{ url_for('main.post_view') }}" method="get">
            //     //     <button type="submit" class="submit-icon">
            //     //         <i class="fas fa-reply"></i>
            //     //     </button></form>
            //         )

            if (!$(this).find("form.reply-form").length){
                var link = $("<a>")
                .attr("href", "#")
                .addClass("reply-link")
                .text("Reply to this post");
                $(this).find(".postOptions").append(link);
                link.click(function() {
                    console.log("clicked");
                    var post = $(this)
                    .closest('.original');
                    post_id = parseInt(
                        post
                        .attr('data-post-id')
                    );
                    form = create_response_form(post_id);
                    post.append(form);
                    $(this).remove();
                });
            }
        },
        function() {
            $(this).find("a.reply-link")
                .remove();
        }
    )
});

var create_response_form = function(post_id) {
    var form = $("<form>")
        .attr("method", "post")
        .attr("action", "/new_post")
        .addClass("reply-form");
    var hidden = $("<input>")
        .attr("type", "hidden")
        .attr("name", "response_to_id")
        .attr("value", post_id);
    var textarea = $("<textarea>")
        .attr("name", "thoughtContent")
        .attr("placeholder", ".   .   .");
    var submit = $("<button>")
        .attr("type", "submit")
        .addClass("submit-icon")
        .append($("<i>").addClass("fas fa-reply"));
    var cancel = $("<button>")
        .attr("type", "button")
        .addClass("cancel-icon")
        .append($("<i>").addClass("fas fa-times"));
    cancel.click(function() {
        $(this).closest("form").remove();
    });
    form.append(hidden)
        .append(textarea)
        .append(submit)
        .append(cancel);
    return form;
}

