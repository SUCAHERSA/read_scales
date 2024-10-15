import serial
import time
import configparser
import serial.tools.list_ports


# Configuración del puerto COM
def read_port(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)

    # Asegurarse de que la sección y la opción existen
    try:
        #'Printer' in config and 'name' in config['Printer']
        port = config['Bascula']['port']
        baudrate = config['Bascula']['baudrate']
        return port, baudrate
    except:
        print("Error", ValueError("La sección 'Printer' o la opción 'name' no se encuentran en el archivo de configuración."))


def check_com_port_status(port_name):
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if port.device == port_name:
            return True
    return False


def read_scales():
    port_name, baudrate = read_port()
    datos = b'P'

    if check_com_port_status(port_name):
        try:
            ser = serial.Serial(port_name, baudrate, timeout=1)
        except Exception as e:
            print(f"Error al enviar datos: {e}")
            return e
    
        try:
            ser.write(datos)
        except Exception as e:
            return e
        
        try:
            while True:
        
                # Leer datos del puerto
                data = ser.readline()
                if data:
                    peso = data.decode('utf-8').strip()
                    return peso
                else: 
                    return "No se recibio lectura de bascula"
                    

        except Exception as e:
            return e
        
        finally:
            ser.close()
            
    else:
        return f'Puerto {port_name} no conectado'


#print (read_scales())