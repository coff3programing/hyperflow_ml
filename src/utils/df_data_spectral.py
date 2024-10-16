""" Data """
import chardet


def extract_x_y(file_path):
    """Extraer datos de un archivo y devolver listas de X e Y."""

    # Función para procesar líneas del archivo
    def procesar_linea(line):
        try:
            wvl = float(line.strip().split('\t')[0])  # Extrae Wvl
            reflect = float(line.strip().split('\t')[1])  # Extrae Reflect
            return wvl, reflect
        except (ValueError, IndexError):
            return None, None

    # Inicializar listas para Wvl y Reflect
    x = []
    y = []

    try:
        # Detectar la codificación del archivo
        with open(file_path, 'rb') as file:  # Abre el archivo en modo binario
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']

        # Leer el archivo usando la codificación detectada
        with open(file_path, 'r', encoding=encoding) as file:
            for line in file:
                if "\t" in line:
                    wvl, reflect = procesar_linea(line)
                    if wvl is not None:  # Filtrar valores válidos
                        x.append(wvl)
                    if reflect is not None:  # Filtrar valores válidos
                        y.append(reflect)
        if not x or not y:
            raise ValueError(f"No valid data found in the file {file_path}")
    except UnicodeDecodeError:
        raise ValueError(
          {
              "message": f'Error decoding the file {file_path}.',
              "error": 'It may not be a valid text file.'
          }
        )
    except Exception as e:
        raise ValueError(
          f'An error occurred while processing the file {file_path}: {str(e)}'
        )

    return x, y
