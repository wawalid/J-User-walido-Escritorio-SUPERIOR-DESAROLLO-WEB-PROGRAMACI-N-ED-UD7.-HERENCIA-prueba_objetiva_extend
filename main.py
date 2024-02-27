from models import (Articulo, Ubicacion, Transaccion)


maestro_articulos = []

articulo_1 = Articulo("A.al.1", "bolsa de patatas", "comprable", 21, 10, True, 3428756, 1, 1)
articulo_2 = Articulo("A.al.2", "caja de cereales", "comprable", 15, 20, True, 3428757, 1.5, 2)
articulo_3 = Articulo("A.al.3", "botella de agua", "comprable", 2, 50, True, 3428758, 0.5, 0.5)
articulo_4 = Articulo("A.al.4", "paquete de galletas", "comprable", 5, 15, False, 3428759, 0.8, 0.8)
articulo_5 = Articulo("A.al.5", "frutas variadas", "comprable", 12, 30, True, 3428760, 2, 2)

maestro_articulos.extend([articulo_1, articulo_2, articulo_3, articulo_4, articulo_5])


maestro_ubicaciones = []

madrid = Ubicacion("001","Madrid", True)
elche = Ubicacion("002", "Elche", False)
barcelona = Ubicacion("003", "Barcelona", False)

maestro_ubicaciones.extend([madrid, elche, barcelona])


transaccion_1 = Transaccion(articulo_1, 20, madrid, barcelona)
transaccion_2 = Transaccion(articulo_2, 15, elche, barcelona)
transaccion_3 = Transaccion(articulo_3, 50, madrid, elche)
transaccion_4 = Transaccion(articulo_4, 10, barcelona, madrid)

transaccion_5 = Transaccion(articulo_1, 10, elche, madrid)
transaccion_6 = Transaccion(articulo_2, 5, madrid, barcelona)
transaccion_7 = Transaccion(articulo_3, 20, elche, madrid)
transaccion_8 = Transaccion(articulo_4, 5, madrid, elche)
transaccion_9 = Transaccion(articulo_5, 8, barcelona, elche)
transaccion_10 = Transaccion(articulo_2, 10, elche, barcelona)
