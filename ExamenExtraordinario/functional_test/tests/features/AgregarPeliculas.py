
Feature: Como empleado del videoclub quiero agregar peliculas al inventario                                                                                                                                                                                                                                                                        # \features\AgregarPeliculas.feature:1
  para tener el inventario actualizado                                                                                                                                                                                                                                                                                                             # \features\AgregarPeliculas.feature:2

  Scenario: Verificar la lista de peliculas existente.                                                                                                                                                                                                                                                                                             # \features\AgregarPeliculas.feature:4
    Given Ingresar en el navegador la url "http://192.168.1.3:8000/Peliculas/" en la barra de direcciones                                                                                                                                                                                                                                          # \features\VisualizarPeliculas.py:6
    Given Ingresar en el navegador la url "http://192.168.1.3:8000/Peliculas/" en la barra de direcciones                                                                                                                                                                                                                                          # \features\VisualizarPeliculas.py:6
    When Introduzca el texto "PEL002" en el campo Clave, el texto "Tansformers" en el campo Titulo, el texto "02:00 hrs" en el campo Duracion, el texto "pelicula sobre una raza de seres mecanicos inteligentes", en el campo Sinopsis, el texto "B" en el campo Clasificacion, seleccionar "Accion" en el campo Genero y oprimo el boton Guardar # \features\AgregarPeliculas.feature:6
    Then Puedo ver en el titulo del navegador la palabra "Peliculas".                                                                                                                                                                                                                                                                              # \features\VisualizarPeliculas.py:15
    Then Puedo ver en el titulo del navegador la palabra "Peliculas".                                                                                                                                                                                                                                                                              # \features\VisualizarPeliculas.py:15

Feature: Como empleado del videoclub quiero visualizar la lista de peliculas                              # \features\VisualizarPeliculas.feature:1
  para conocer en todo momento el inventario existente                                                    # \features\VisualizarPeliculas.feature:2

  Scenario: Verificar la inscripcion la lista de peliculas existente.                                     # \features\VisualizarPeliculas.feature:4
    Given Ingresar en el navegador la url "http://192.168.1.3:8000/Peliculas/" en la barra de direcciones # \features\VisualizarPeliculas.py:6
    Given Ingresar en el navegador la url "http://192.168.1.3:8000/Peliculas/" en la barra de direcciones # \features\VisualizarPeliculas.py:6
    When Oprimo la tecla Enter                                                                            # \features\VisualizarPeliculas.py:11
    When Oprimo la tecla Enter                                                                            # \features\VisualizarPeliculas.py:11
    Then Puedo ver en el titulo del navegador la palabra "Peliculas".                                     # \features\VisualizarPeliculas.py:15
    Then Puedo ver en el titulo del navegador la palabra "Peliculas".                                     # \features\VisualizarPeliculas.py:15

2 features (1 passed)
2 scenarios (1 passed)
6 steps (1 skipped, 1 undefined, 4 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'When Introduzca el texto "([^"]*)" en el campo Clave, el texto "([^"]*)" en el campo Titulo, el texto "([^"]*)" en el campo Duracion, el texto "([^"]*)", en el campo Sinopsis, el texto "([^"]*)" en el campo Clasificacion, seleccionar "([^"]*)" en el campo Genero y oprimo el boton Guardar')
def when_introduzca_el_texto_group1_en_el_campo_clave_el_texto_group2_en_el_campo_titulo_el_texto_group3_en_el_campo_duracion_el_texto_group4_en_el_campo_sinopsis_el_texto_group5_en_el_campo_clasificacion_seleccionar_group6_en_el_campo_genero_y_oprimo_el_boton_guardar(step, group1, group2, group3, group4, group5, group6):
    assert False, 'This step must be implemented'
