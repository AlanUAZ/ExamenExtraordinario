# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver

@step(u'Given Ingresar en el navegador la url "([^"]*)" en la barra de direcciones')
def given_ingresar_en_el_navegador_la_url_group1_en_la_barra_de_direcciones(step, urlPeliculas):
	world.driver = webdriver.Firefox()
	world.driver.get(urlPeliculas)

@step(u'When Oprimo la tecla Enter')
def when_oprimo_la_tecla_enter(step):
	assert True

@step(u'Then Puedo ver en el titulo del navegador la palabra "([^"]*)".')
def then_puedo_ver_en_el_titulo_del_navegador_la_palabra_group1(step, browserTitle):
    assert browserTitle in world.driver.title