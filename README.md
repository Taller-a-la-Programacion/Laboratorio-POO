
## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Pueden hacer uso **Try/Except, isinstance, type**
- Pueden hacer el uso de las funciones previamente definidas en clase


## Clase Vehículo (Programación Orientada a Objetos)

- Escriba en python los métodos necesarios para recrear un **Vehiculo**. 
- Los atributos de la  clase **Vehiculo** son: 
  - Placa : String
  - Hora de entrada : String debe registrar la hora y minuto de entrada, ej: 15:30

- Debe crearse el **constructor** en donde se inicializan sus atributos
- Debe tener una funcion llamado **mostrar()** que mostrará un string con el valor concatenado de "Placa: ABC-123 hora de ingreso: 15:30"

```python
>>> veh1 = Vehiculo('ABC-123', '10:23')

>>> veh1.mostrar()
'Placa: ABC-123 hora de ingreso: 10:23'

```


## Clase Parqueo (Programación Orientada a Objetos e Iteración)

- Escriba en python los métodos necesarios para recrear un **Parqueo**. 
- Los atributos de la  clase **Parqueo** son:
  - Dirección : debe ser string
  - Nombre : debe ser string
  - Campos  : debe ser entero, es la cantidad de campos que posse el parqueo
  - Lista de Vehículos : Arreglo donde se guardará los objetos de los vehículos que se parquean

Los métodos a crear son:

- **Constructor**: debe guardar la dirección, teléfono y total de campos que tendrá el parqueo
- **datosParqueo**: imprime en pantalla los datos del parqueo
- **agregarVehículo**: debe guardar: placa, horaEntrada
- **quitarVehículo**: solo necesita una placa y quitarlo de la lista
- **totalVehiculos**: debe devolver el total de vehículos en el parqueo
- **mostrarVehiculos**: devolver una lista de las placas de los vehículos en el parqueo

```python
>>> parqueo = Parqueo('San José', 'El parqueo', 2)

>>> parqueo.datosParqueo()
'San José, El parqueo con capacidad 2'

>>>parqueo.agregarVehiculo('ABC132', '12:00')

>>>parqueo.agregarVehiculo('DFG888', '11:00')

>>>parqueo.totalVehiculos()
2

>>>parqueo.agregarVehiculo('GHJ888', '11:00')
'Parqueo lleno'

>>>parqueo.quitarVehiculo('ABC132')

>>>parqueo.totalVehiculos()
1

>>>parqueo.agregarVehiculo('GHJ888', '11:00')

>>>parqueo.mostrarVehiculos()
['DFG888', 'GHJ888']

```

