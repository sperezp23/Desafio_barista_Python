import numpy as np
import pandas as pd

def decodificar_fechas(fecha_binaria):
    # Convertir la fecha en binario a entero decimal
    fecha_entero = int(fecha_binaria, 2)

    # Convertir el entero a bytes
    fecha_bytes = fecha_entero.to_bytes((fecha_entero.bit_length() + 7) // 8, 'big')

    # Decodificar los bytes utilizando UTF-8 para obtener la fecha en formato AAAA/MM/DD
    fecha_decodificada = fecha_bytes.decode('utf-8')

    # Mostrar la fecha decodificada
    return fecha_decodificada

def construir_fecha(dato):
    lista_datos = list(map(decodificar_fechas,dato.split(' ')))
    return f'{lista_datos[0] + lista_datos[1] + lista_datos[2] + lista_datos[3]}/{lista_datos[4] + lista_datos[5]}/{lista_datos[6] + lista_datos[7]}'

nombres = ['cantidad_de_sobres', 'fecha', 'tipo_de_grano']
pedidos_df = pd.read_csv(r'Registros_perdidos\registros_perdidos.txt', names= nombres)

cantidad_de_sobres = pedidos_df.cantidad_de_sobres.apply(lambda dato_hex: int(dato_hex, base = 16))
fechas = [construir_fecha(dato) for dato in pedidos_df.fecha]

pedidos_ordenados_df =  pd.DataFrame({
    'cantidad_de_sobres':cantidad_de_sobres,
    'fechas':fechas,
    'tipo_de_grano':pedidos_df.tipo_de_grano
    })

pedidos_ordenados_df.sort_values(by='cantidad_de_sobres')
pedidos_ordenados_df.fechas = pd.to_datetime(pedidos_ordenados_df.fechas)
pedidos_ordenados_df.to_csv(r'Registros_perdidos\registros_ordenados.txt',index=False)

print(pedidos_ordenados_df)
