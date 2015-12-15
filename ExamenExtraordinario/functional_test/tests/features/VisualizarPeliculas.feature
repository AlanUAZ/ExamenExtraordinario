Feature: Como empleado del videoclub quiero visualizar la lista de peliculas
	para conocer en todo momento el inventario existente

Scenario: Verificar la inscripcion la lista de peliculas existente.
	Given Ingresar en el navegador la url "http://192.168.1.3:8000/Peliculas/" en la barra de direcciones
	When Oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Peliculas".