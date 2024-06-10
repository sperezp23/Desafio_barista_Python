import numpy as np

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(np.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def cargar_y_limpiar_datos(ruta_datos = 'codigos_secretos.txt'):
    codigos = np.genfromtxt(ruta_datos, delimiter=',')
    codigos_limpios = codigos[~np.isnan(codigos)]
    return codigos_limpios

def buscar_primos(codigos_limpios):
    return codigos_limpios[list(map(es_primo, codigos_limpios))]

if __name__ == '__main__':
    codigos_limpios = cargar_y_limpiar_datos()
    granos_dorados = buscar_primos(codigos_limpios)
    print(np.sort(granos_dorados))
