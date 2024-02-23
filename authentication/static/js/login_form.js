(function() {

  // Aplicando AJAX al formulario de login para evitar que se refresque la pagina.
$(document).on("submit", "#login-form", function(e) {
  e.preventDefault();
  console.log("se clickeo")
  $.ajax({
      type: 'POST',
      url:  '/login/',
      data: {
          username: $('#username').val(),
          password: $('#password').val(),
          csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
      },
      success: function(data) {
        // Eliminar los datos de entrada de los inputs cuando se hace submit. 
        $("input[name='username']").val("")
        $("input[name='password']").val("")
        
      }

  });
});

})();
