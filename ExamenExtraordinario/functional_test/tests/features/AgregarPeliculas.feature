Feature: Como empleado del videoclub quiero agregar peliculas al inventario
	para tener el inventario actualizado

Scenario: Verificar la lista de peliculas existente.
	Given Ingresar en el navegador la url "http://192.168.1.3:8000/Peliculas/" en la barra de direcciones
	When Introduzca el texto "PEL002" en el campo Clave, el texto "Tansformers" en el campo Titulo, el texto "02:00 hrs" en el campo Duracion, el texto "pelicula sobre una raza de seres mecanicos inteligentes", en el campo Sinopsis, el texto "B" en el campo Clasificacion, seleccionar "Accion" en el campo Genero y oprimo el boton Guardar
	Then Puedo ver en el titulo del navegador la palabra "Peliculas".