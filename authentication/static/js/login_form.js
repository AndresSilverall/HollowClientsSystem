// Aplicando AJAX al formulario de login para evitar que se refresque la pagina.
$(document).on("submit", "#login-form", function(e) {
    e.preventDefault();
    console.log("se clickeo")
    $.ajax({
        type: 'POST',
        dataType:'html',
        url:  '/login/',
        data: {
            username: $("input[name='username']").val(),
            password: $("input[name='password']").val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response) {
        // Eliminar los datos de entrada de los inputs cuando se hace submit. 
        $("input[name='username']").val("")
        $("input[name='password']").val("")
        alert("Sesion!")
        $("#message-content").html(response)

      },
      error: function (xhr, status, error) {
        console.log("error de respuesta", error)
      }

      });

  });


  const preventRefreshLoginForm = () => {
    return null;
  }