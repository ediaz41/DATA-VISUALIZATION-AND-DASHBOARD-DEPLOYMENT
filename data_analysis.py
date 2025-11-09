import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

# ==========================
#  Carga del archivo CSV
# ==========================
print("📂 Por favor, selecciona el archivo 'university_student_data.csv' desde tu computadora...")
uploaded = files.upload()  # 👈 Esto abre el cuadro para subir archivos

# Una vez cargado, el archivo estará disponible en el entorno de Colab
df = pd.read_csv("university_student_data.csv")

# ==========================
#  Configuración visual
# ==========================
sns.set(style="whitegrid", palette="deep")

# ==========================
#  Vista previa
# ==========================
print("Dimensiones del dataset:", df.shape)
display(df.head())

# ==========================
#  Análisis Exploratorio Inicial
# ==========================
print("\n--- Información general ---")
print(df.info())

print("\n--- Valores faltantes ---")
print(df.isnull().sum())

print("\n--- Estadísticas descriptivas ---")
display(df.describe(include='all'))

# ==========================
#  Descripción de las columnas
# ==========================
"""
Significado de las columnas en el contexto del estudio:

• Year: Año académico correspondiente a la observación.
• Term: Semestre o término académico (Spring = Primavera, Fall = Otoño).
• Applications: Número total de solicitudes recibidas por la universidad.
• Admitted: Cantidad de estudiantes admitidos.
• Enrolled: Cantidad de estudiantes matriculados.
• Retention Rate (%): Porcentaje de estudiantes que continuaron sus estudios al siguiente año (indicador clave de retención).
• Student Satisfaction (%): Porcentaje promedio de satisfacción estudiantil medido mediante encuestas institucionales.
• Engineering Enrolled / Business Enrolled / Arts Enrolled / Science Enrolled:
  Número de estudiantes matriculados por cada facultad o departamento académico.
"""

# ==========================
#  Visualizaciones Solicitadas
# ==========================
# Tendencias de la tasa de retención a lo largo del tiempo
plt.figure(figsize=(8,5))
sns.lineplot(data=df, x="Year", y="Retention Rate (%)", marker="o", color="blue")
plt.title("Tendencia de la Tasa de Retención a lo Largo del Tiempo", fontsize=13)
plt.xlabel("Año")
plt.ylabel("Tasa de Retención (%)")
plt.show()

# Puntuaciones de satisfacción de los estudiantes por año
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Year", y="Student Satisfaction (%)", color="orange")
plt.title("Puntuación Promedio de Satisfacción por Año", fontsize=13)
plt.xlabel("Año")
plt.ylabel("Satisfacción (%)")
plt.show()

# Comparación entre los semestres Spring y Fall
plt.figure(figsize=(6,5))
sns.barplot(data=df, x="Term", y="Student Satisfaction (%)", palette="Set2")
plt.title("Comparación de Satisfacción por Semestre (Spring vs Fall)", fontsize=13)
plt.xlabel("Semestre")
plt.ylabel("Satisfacción (%)")
plt.show()

# Ejemplo adicional: Distribución por facultades
facultades = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
mean_fac = df[facultades].mean()
plt.figure(figsize=(6,6))
plt.pie(mean_fac, labels=facultades, autopct="%1.1f%%", startangle=90)
plt.title("Distribución Promedio de Estudiantes por Facultad")
plt.show()

print("✅ Visualizaciones generadas correctamente.")
