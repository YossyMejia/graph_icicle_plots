import pandas as pd

# Constantes ----------
# Definicion de la ubicacion del archivo de datos
df = pd.read_csv('D:\\User\\Documentos\\Semestres\\S2-2021\\Visualizacion\\Proyecto 1\\Datos\\Datos.csv')

# Orientaciones del grafico disponibles
orientaciones_disponibles = ["Horizontal", "Vertical"]

# Configuracion de color disponible
colores_disponibles = ["Por categoria", "Por valor comercial"]

# Tamanno de fuentes disponibles
tamannos_fuente = [15, 20, 25, 30, 35, 40]

#Profundidades disponibles para el arbol
profundidades = [2,3,4]