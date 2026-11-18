import pandas as pd
import matplotlib.pyplot as plt

# Samuel Martinez NC 0096
# 1. Crear diccionario con datos de equipamiento deportivo
equipamiento_deportivo = {
    'id_equipo': [201, 202, 203, 204, 205, 206],
    'nombre': ['Mancuernas 10kg', 'Colchoneta Yoga', 'Cuerda para saltar', 'Balon Medicinal 5kg', 'Banda elastica', 'Kettlebell 12kg'],
    'categoria': ['Pesas', 'Accesorios', 'Cardio', 'Pesas', 'Accesorios', 'Pesas'],
    'cantidad_total': [40, 30, 50, 20, 40, 25],
    'cantidad_disponible': [35, 28, 45, 18, 38, 22],
    'precio_unitario': [500, 300, 150, 600, 100, 700],
    'fecha_compra': ['2022-01-01', '2023-05-10', '2021-08-15', '2022-11-20', '2023-02-05', '2022-06-30'],
    'estado': ['Bueno', 'Excelente', 'Regular', 'Bueno', 'Excelente', 'Bueno'],
    'ubicacion': ['Sala Pesas', 'Sala Yoga', 'Recepcion', 'Sala Pesas', 'Sala Yoga', 'Sala Pesas'],
    'vida_util_estimada_meses': [60, 24, 12, 36, 18, 48]
}

print("Análisis Exploratorio de Datos")
print("EDA, Exploratory Data Analysis por Samuel Martinez NC 0096")
print(" 5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(equipamiento_deportivo)
print("\n--- TABLA ORIGINAL DE EQUIPAMIENTO DEPORTIVO ---")
print(df)

# 3. Exportar los datos a CSV
print("+-+-+- 7. Convertir el DataFrame en archivo CSV -+-+-+")
df.to_csv(
    'equipamiento_deportivo_0096.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("+-+- 8. Leer los datos desde el archivo CSV +-+-")

# 4. Leer el archivo CSV
df = pd.read_csv('equipamiento_deportivo_0096.csv')
print("equipamiento_deportivo_0096.csv")
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("+-+- 9. Análisis Exploratorio de Datos (EDA) +-+-")

# 5. Primeros y últimos registros
print("+-+-+- \n1. PRIMEROS REGISTROS (Head): +-+-+-")
print(df.head(3))  # Muestra los primeros 3
print("+-+-+- \n2. ÚLTIMOS REGISTROS (Tail): +-+-+-")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+- 6. Dimensiones y estructura +-+-+-")
print(df)  # mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("+-+- \n7. ESTADÍSTICAS DESCRIPTIVAS: +-+-")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Categorías únicas:", df['categoria'].unique())

# 8. Análisis específico
print(df)
print("---------------------------------------------------------")
print("\n11. EQUIPOS POR CATEGORÍA:")
print(df['categoria'].value_counts())

print("\n12. PROMEDIO DE PRECIO UNITARIO: $", df['precio_unitario'].mean())
print("13. PRECIO UNITARIO MÁXIMO: $", df['precio_unitario'].max())
print("14. PRECIO UNITARIO MÍNIMO: $", df['precio_unitario'].min())

# 9. Ordenamiento, filtrado y agrupación
print("# 9. Ordenamiento, filtrado y agrupación")
print("+-+-\n15. EQUIPOS ORDENADOS POR PRECIO UNITARIO (Mayor a menor):+-+-")
print(df.sort_values(by='precio_unitario', ascending=False))

print("\n16. EQUIPOS CON PRECIO UNITARIO MAYOR A $300:")
filtro = df[df['precio_unitario'] > 300]
print(filtro)

print("\n17. RESUMEN POR CATEGORÍA:")
resumen = df.groupby('categoria').agg(
    tipos_equipo=('id_equipo', 'count'),
    precio_promedio=('precio_unitario', 'mean'),
    precio_maximo=('precio_unitario', 'max')
)
print(resumen)

# 18. Gráfica de barras: Tipos de equipo por categoría
print("18. Gráfica de barras: Tipos de equipo por categoría")
conteo = df['categoria'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Equipos por categoría Samy 0096')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de tipos de equipo')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Precio unitario por equipo
plt.figure(figsize=(9, 5))
plt.bar(df['nombre'], df['precio_unitario'], color='lightgreen')
plt.title('Precio unitario por equipo EDA Por Samuel 0096')
plt.xlabel('Equipo')
plt.ylabel('Precio unitario en pesos')
plt.xticks(rotation=25)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de cantidad total
plt.figure(figsize=(8, 5))
plt.hist(df['cantidad_total'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de cantidad total de equipos EDA Samy 0096')
plt.xlabel('Cantidad total')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Vida útil vs Precio unitario
plt.figure(figsize=(8, 5))
plt.scatter(df['vida_util_estimada_meses'], df['precio_unitario'], color='red', s=100)
plt.title('Relación entre vida útil (meses) y precio unitario EDA por Samy 0096')
plt.xlabel('Vida útil estimada (meses)')
plt.ylabel('Precio unitario')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de precios unitarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['precio_unitario'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de precios unitarios (Boxplot) EDA por Samy 0096')
plt.ylabel('Precio unitario')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA por Samy 0096')
plt.tight_layout()
plt.show()