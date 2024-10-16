""" Extract Information """
from functools import partial
from datetime import datetime
import polars as pl
import chardet


def format_date(date_str):
    """ Convierte la fecha al formato YYYY-MM-DD desde MM-DD-YYYY """
    try:
        # Cambiar a YYYY-MM-DD para que coincida con DRF
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return date_str


def extract_values(line, keyword):
    """ Extract Values """
    if keyword in line:
        try:
            values = line.split(":")[1].strip().split(',')
            return [
                v.strip().replace('"', '') for v in values
            ] if len(values) == 2 else [
                values[0].strip().replace('"', ''), None
            ]
        except (IndexError, ValueError):
            return [None, None]
    return [None, None]


def extract_time(line):
    """ Extract Time """
    if "Time:" in line:
        try:
            values = line.split("Time:")[1].strip().split(',')
            return values[0].strip().replace('"', ''), (
                values[1].strip().replace(
                  '"', '') if len(values) > 1 else None)
        except Exception:
            return None, None
    return None, None


def extract_averages(line):
    """ Extract Averages """
    return extract_values(line, "Averages")


def extract_by_keyword(keyword, lines):
    """ Extract By Keyword """
    extractor = partial(extract_values, keyword=keyword)
    return next(filter(
        lambda result: result != [None, None], map(extractor, lines)
    ), [None, None])


def process_file(file_path):
    """ Process File """
    try:
        # Detectar la codificación del archivo
        with open(file_path, 'rb') as file:  # Abre el archivo en modo binario
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']

        # Leer el archivo usando la codificación detectada
        with open(file_path, 'r', encoding=encoding) as file:
            lines = [line.strip() for line in file.readlines()]
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

    initial_time, end_time = None, None
    averages_initial, averages_final = None, None

    for line in lines:
        if not (initial_time and end_time):
            initial_time, end_time = extract_time(line)
        if not (averages_initial and averages_final):
            averages_initial, averages_final = extract_averages(line)
        if initial_time and end_time and averages_initial and averages_final:
            break

    extraction_map = {
        "InitialDate": "Date",
        "EndDate": "Date",
        "InitialTemp": "Temperature (C)",
        "EndTemp": "Temperature (C)",
        "InitialVoltage": "Battery Voltage",
        "EndVoltage": "Battery Voltage"
    }

    dates, temps, voltages = {}, {}, {}
    for key, keyword in extraction_map.items():
        initial, final = extract_by_keyword(keyword, lines)
        if "Date" in key:
            # Normalizamos las fechas utilizando format_date()
            dates[key] = format_date(initial) if initial else None
            dates[key + "_final"] = format_date(final) if final else None
        elif "Temp" in key:
            temps[key] = initial if "Initial" in key else final
        elif "Voltage" in key:
            voltages[key] = initial if "Initial" in key else final

    data = {
        "InitialDate": dates.get("InitialDate"),
        "EndDate": dates.get("EndDate"),
        "InitialTime": initial_time,
        "EndTime": end_time,
        "InitialTemperature": temps.get("InitialTemp"),
        "EndTemperature": temps.get("EndTemp"),
        "InitialVoltage": voltages.get("InitialVoltage"),
        "EndVoltage": voltages.get("EndVoltage"),
        "InitialAverages": averages_initial,
        "EndAverages": averages_final
    }

    columns_order = [
        "InitialDate",
        "EndDate",
        "InitialTime",
        "EndTime",
        "InitialTemperature",
        "EndTemperature",
        "InitialVoltage",
        "EndVoltage",
        "InitialAverages",
        "EndAverages"
    ]
    return pl.DataFrame([data])[columns_order]
