import Laboratorio;
import pytest;


parqueo = Laboratorio.Parqueo('San José', 'El parqueo', 2)
       
def test_parqueo1():
  assert isinstance(str(parqueo.datosParqueo()), str) == isinstance('San José, 88556699, Capacidad 2', str)

def test_parqueo4():
  assert parqueo.totalVehiculos() == 2
  
def test_parqueo5():
  assert isinstance(str(parqueo.agregarVehiculo('GHJ888', '11:00')), str) == isinstance('Parqueo lleno', str)
  
def test_parqueo7():
  assert parqueo.totalVehiculos() == 1
  
def test_parqueo9():
  assert parqueo.mostrarVehiculos() = ['DFG888', 'GHJ888']
