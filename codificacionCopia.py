import pandas as pd


def codificacionGlobal(path, k, prefijo):
    try:
        df = pd.read_csv(path+k, sep='|', header=None, dtype=str, encoding='utf-8', lineterminator='\n')
        detectar_saltos_linea_unix(path+k)
        print("Archivo leído correctamente como UTF-8")
    except Exception as e:
        print("Fallo al leer como UTF-8. Intentando conversiones...")
        codificaciones = ['ansi', 'latin-1', 'ascii']
        convertido = False
        for codificacion in codificaciones:
            try:
                with open(path+k, 'r', encoding=codificacion) as archivo_origen:
                    contenido = archivo_origen.read()
                with open(path+k, 'w+', encoding='utf-8') as archivo_destino:
                    archivo_destino.write(contenido)
                print(f"Archivo convertido correctamente de {codificacion} a UTF-8")
                convertido = True
                break
            except Exception as e:
                print(f"Fallo al convertir con codificación {codificacion}: {e}")
        
        if not convertido:
            print("No se pudo convertir el archivo. Verifica manualmente el formato.")
            '''MOVER A CARPETAS'''
            mover = os.getcwd()+'\\' +k 
            print(mover)
            mover_archivos(mover, prefijo,'Error')
            print('movido')



def contenidoError(path, k, prefijo):
    contenidoRaro = ['\t', '\xa0']
    
    try:
        df = pd.read_csv(path + k, sep='|', header=None, encoding='utf-8', dtype=str)
    
        resultado = df.applymap(lambda x: any(caracter in str(x) for caracter in contenidoRaro))
        
        if resultado.any().any():
            print(f"Se encontraron caracteres raros como tabulaciones y nbsp en el archivo {k}.")
            posiciones = resultado.stack()[resultado.stack()].index.tolist()
            print(f"Posiciones con caracteres raros: {posiciones}")
        else:
            print(f"No se encontraron caracteres raros en el archivo {k}.")
    
    except Exception as e:
        print(f"Error al procesar el archivo {k}: {e}")
