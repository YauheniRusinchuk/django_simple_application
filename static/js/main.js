$(function(){

  $(".comment_form").on('submit', (e) => {
    e.preventDefault();
    create_comment();
  })
});


function create_comment() {
  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: {
      comment: $('.text_comment').val(),
      csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
    },
    success : function(data) {
      let newItem = document.createElement('p')
      newItem.className = 'comment_view';
      newItem.innerHTML = data.message;
      $('.comments').append(newItem);
      let inputText = $('.text_comment').val("")
    }
  })
}
