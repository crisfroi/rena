import configparser
import os

class readConf(object):
    def __init__(self):
        # Obtiene el directorio donde se encuentra este script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construye la ruta al archivo set.conf de forma segura
        # asumiendo que set.conf está en el mismo directorio que readConf.py.
        self.config_path = os.path.join(base_dir, 'set.conf')

    def GetwebsocketParam(self):
        config = configparser.ConfigParser()
        config.read(self.config_path, encoding="utf-8")
        val = config.get('websocket', 'port')
        return val

    def GetDBParam(self):
        config = configparser.ConfigParser()
        config.read(self.config_path, encoding="utf-8")
        url = config.get('db', 'url')
        return url

    def GetUploadParam(self):
        # Esta ruta también debe ser compatible con cualquier sistema operativo
        # Si la carpeta 'pictures' está en la raíz del proyecto, debes ajustar la ruta.
        # Por ejemplo, si está en la raíz, la ruta podría ser os.path.join(base_dir, '..', 'pictures').
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads', 'pictures')

# El bloque de prueba local se deja para depuración si lo necesitas
if __name__ == "__main__":
    read = readConf()
    print(read.GetwebsocketParam())
    print(read.GetDBParam())
