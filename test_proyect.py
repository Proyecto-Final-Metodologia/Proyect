from proyectosim import variables, mostrar_LCD, tiempo
import pytest
import datetime
    
def test_mostrar_LCD():
    lista = mostrar_LCD.get_datos_actualizados()
    assert lista != None
    
def test_tiempo():
    assert tiempo(1) <= 205
    
def test_variables():
    fecha = variables.get_fechaActual()
    assert fecha == datetime.datetime.now()
    
def test_variables2():
    temperatura = variables.get_tem()
    assert not temperatura == 0