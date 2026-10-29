from collections import namedtuple
from math import sqrt

EstacionSevici = namedtuple("EstacionSevici", 
    "nombre, direccion, latitud, longitud, capacidad, puestos_libres, bicicletas_disponibles")

def selecciona_color(estacion:EstacionSevici) -> str:
    """
    Devuelve el color en que debe pintarse cada estación según su disponibilidad.

    Parámetros:
    estacion: EstacionSevici

    Devuelve:
    str: "green", "orange", "red" o "gray"
    """
    # TODO: Ejercicio 1
    if estacion.capacidad == 0:
        return "gray"
    disponibilidad = (estacion.bicicletas_disponibles/estacion.capacidad)
    if disponibilidad >= 2/3:

        return "green"
    elif disponibilidad >= 1/3:
        return "orange"
    elif disponibilidad >0:
        return "red"
    else:
        return "gray"

def calcula_estadisticas(estaciones: list[EstacionSevici]) -> tuple[int, int, float, int]:
    """
    Calcula estadísticas de las estaciones.
    Parametros:
    estaciones: lista de EstacionSevici
    Devuelve:
    tupla con (total de bicicletas libres, total de capacidad, porcentaje de ocupación, total de estaciones)
    """
    # TODO: Ejercicio 2
    bicis_total = 0
    capacidad_total = 0
    estacion = 0
    for i in estaciones:
        bicis_total+=i.bicicletas_disponibles
        capacidad_total+=i.capacidad
        estacion += 1

    prc_ocupacion = 100-(bicis_total/capacidad_total)*100
    return (bicis_total, capacidad_total, prc_ocupacion, estacion)

def busca_estaciones_direccion(estaciones: list[EstacionSevici], direccion_parcial: str) -> list[EstacionSevici]:
    """
    Busca las estaciones que contengan en su dirección (subcadena, sin distinguir mayúsculas/minúsculas) la dirección parcial dada.    

    Parametros:
    estaciones: lista de EstacionSevici
    direccion_parcial: subcadena a buscar en la dirección de las estaciones

    Devuelve:
    lista de EstacionSevici que cumplen el criterio
    """
    # TODO: Ejercicio 30
    lista_res=[]
    for i in estaciones:
        if direccion_parcial.lower() in i.direccion.lower():
            lista_res.append(i)

    return lista_res

def busca_estaciones_con_disponibilidad(estaciones:list[EstacionSevici], min_disponibilidad: float = 0.5) -> list[EstacionSevici]:
    """
    Devuelve una lista de EstacionSevici con al menos el porcentaje mínimo de bicicletas disponible
    indicado.

    Parametros:
    estaciones: lista de EstacionSevici
    min_disponibilidad: porcentaje mínimo de bicicletas disponibles (0.0 a 1.0)
    
    Devuelve:
    lista de EstacionSevici
    """
    # TODO: Ejercicio 4
    lista=[]
    for i in estaciones:
        if i.capacidad != 0:
            disponibilidad = (i.bicicletas_disponibles/i.capacidad)

            if disponibilidad >= min_disponibilidad:
            
                lista.append(i)
    return lista

def calcula_distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """
    Calcula la distancia euclídea entre dos puntos (latitud, longitud).

    Parámetros:
    p1: tupla (latitud, longitud) del primer punto
    p2: tupla (latitud, longitud) del segundo punto

    Devuelve:
    float: distancia euclídea entre los dos puntos
    """
    # TODO: Ejercicio 5
    distancia = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distancia

def busca_estacion_mas_cercana(estaciones:list[EstacionSevici], punto:tuple[float, float]) -> EstacionSevici | None:
    """
    Devuelve la estación más cercana al punto dado (latitud, longitud) que tenga al menos una bicicleta disponible.
    
    Parametros:
    estaciones: lista de EstacionSevici
    punto: tupla (latitud, longitud)

    Devuelve:
    EstacionSevici más cercana con al menos una bicicleta disponible, o None si no hay ninguna.
    """ 
    # TODO: Ejercicio 5
    res = None

    for i in estaciones:
        if res == None:
            res = i
        else:
            if calcula_distancia((i.latitud, i.longitud),punto) < calcula_distancia((res.latitud,res.longitud),punto) :
                res = i
            
    return res

def calcula_ruta(estaciones:list[EstacionSevici], origen:tuple[float, float], destino:tuple[float, float]) -> tuple[EstacionSevici | None, EstacionSevici | None]   :
    """
    Devuelve las estaciones más cercanas al punto de origen y destino dados, que tengan al menos una bicicleta disponible.

    Parametros: 
    estaciones: lista de EstacionSevici
    origen: tupla (latitud, longitud) del punto de origen
    destino: tupla (latitud, longitud) del punto de destino

    Devuelve:
    tupla con (estacion_origen, estacion_destino)
    """
    # TODO: Ejercicio 5
    res_origen = busca_estacion_mas_cercana(estaciones, origen)
    res_destino = busca_estacion_mas_cercana(estaciones, destino)
    return res_origen,res_destino

