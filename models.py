from abc import ABC, abstractmethod


class Producto(ABC):
    id_prod = 0
    @abstractmethod
    def __init__(self, codigo, descripcion, estado, iva):
        self.__id = Producto.id_prod
        Producto.id_prod += 1
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__estado = estado
        # estado puede ser comprable, vendible, activo, publicado
        self.__iva = iva 


    @property
    def get_id(self):
        return self.__id

    @property
    def get_codigo(self):
        return self.__codigo

    @property
    def get_descripcion(self):
        return self.__descripcion

    @property
    def get_estado(self):
        return self.__estado

    @property
    def get_iva(self):
        return self.__iva

class Articulo(Producto):
    def __init__(self, codigo, descripcion, estado, iva, stock_min, perecedero, serie, lote, precio_venta):
        super().__init__(codigo, descripcion, estado, iva)
        self.__stock_min = stock_min
        self.__perecedero = perecedero
        self.__serie = serie
        self.__lote = lote
        self.__precio_venta = precio_venta

    @property
    def get_stock_min(self):
        return self.__stock_min
    
    @property
    def get_perecedero(self):
        return self.__perecedero
    
    @property
    def get_serie(self):
        return self.__serie
    
    @property
    def get_lote(self):
        return self.__lote
    
    @property
    def get_precio_venta(self):
        return self.__precio_venta
    
    @property
    def set_codigo(self, valor):
        self.__codigo = valor

    @property
    def set_descripcion(self, valor):
        self.__descripcion = valor

    @property
    def set_stock_min(self, valor):
        self.__stock_min = valor

    def __str__(self):
        return f"Codigo: {self.get_codigo}, descripcion: {self.get_descripcion}"


class Servicio(Producto):
    def __init__(self, codigo, descripcion, comprable, iva, tipo_servicio):
        super().__init__(codigo, descripcion, comprable, iva)
        self.__tipo_servicio = tipo_servicio

    @property
    def get_tipo_servicio(self):
        return self.__tipo_servicio

    def __str__(self):
        return f"Codigo: {self.get_codigo}, descripcion: {self.get_descripcion}"



class Estado():
    def __init__(self, estado):
        pass

class Ubicacion():
    id_ubi = 0
    def __init__(self, codigo, descripcion, recepcion : bool):
        self.__id = Ubicacion.id_ubi
        Ubicacion.id_ubi += 1
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__recepcion = recepcion

    @property
    def get_id(self):
        return self.__id

    @property
    def get_codigo(self):
        return self.__codigo

    @property
    def get_descripcion(self):
        return self.__descripcion
    
    @property
    def get_recepcion(self):
        return self.__recepcion
    
    @property
    def set_codigo(self, valor):
        self.__codigo = valor

    @property
    def set_descripcion(self, valor):
        self.__descripcion = valor

    @property
    def set_recepcion(self, valor):
        self.__recepcion = valor

    def __str__(self):
        return f"Codigo: {self.get_codigo} - descripcion: {self.get_descripcion} "

class Transaccion():
    id_trans = 0
    def __init__(self, articulo, cantidad, ubi_origen, ubi_destino):
        self.__id_trans = Transaccion.id_trans
        Transaccion.id_trans += 1
        self.__articulo = articulo
        self.__cantidad = cantidad
        self.__ubi_origen = ubi_origen
        self.__ubi_destino = ubi_destino

    @property
    def get_id_trans(self):
        return self.__id_trans

    @property
    def get_articulo(self):
        return self.__articulo

    @property
    def get_cantidad(self):
        return self.__cantidad

    @property
    def get_ubicacion_origen(self):
        return self.__ubi_origen

    @property
    def get_ubicacion_destino(self):
        return self.__ubi_destino
    
    def __str__(self):
        return f"{self.get_ubicacion_origen} --> {self.get_ubicacion_destino} : {self.get_articulo.codigo} '{self.get_cantidad}'"
    

class Solicitud_pedido():
    id_pedido = 0
    def __init__(self, objeto_articulo, cantidad):
        self.__id_pedido = Solicitud_pedido.id_pedido
        Solicitud_pedido.id_pedido += 1
        self.__objeto_articulo = objeto_articulo
        self.__cantidad = cantidad

    @property
    def get_id_pedido(self):
        return self.__id_pedido

    @property
    def get_objeto_articulo(self):
        return self.__objeto_articulo

    @property
    def get_cantidad(self):
        return self.__cantidad

    @property
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("La cantidad debe ser mayor o igual a cero.")

    def __str__(self):
        return f"{self.get_objeto_articulo.codigo} : {self.get_cantidad}"










