import zipfile 
import shutil 

carpeta_origen = "C:\\Users\\EDMG0\\Downloads\\Proyecto dia 9\\Proyecto+Dia+9.zip"

archivo_destino = "C:\\Users\\EDMG0\\Downloads\\Proyecto dia 9"

shutil.unpack_archive(carpeta_origen, "archivo.zip","zip")
