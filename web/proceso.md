---
nav_order: 3
---

# ⚙️ Proceso de recoleccion y desarollo de datos

## **Procesamiento**
Dado a que la información que buscaba ya estaba recolectada y limpiada, creé los siguientes DataFrames de Pandas a partir de archivos CSV:<br>
* **df_maxim**: Hecho con CSV de temperatura máxima por mes.
* **df_minim**: Hecho con CSV de temperatura mínima por mes.
* **df_media**: Hecho con CSV de temperatura media por mes.
* **df_humed**: Hecho con CSV de la data de humedad mensual.
* **df_preci**: Hecho con CSV de la data de precipitación mensual.
* **df_presi**: Hecho con CSV de la data de presión atmosférica.
![Head y tail de un DataFrame](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/ejemplo_df.PNG) <br>
(Ejemplo de head y tail de df_maxim)


## !! (cambiar) **Preparación**
![Ejemplo de código](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/ejemplo_codigo.PNG) <br>
Después, fuí haciendo copias de los DataFrames que usaría pero solo dejando la información en el rango de tiempo que me importaba (En este caso, el periodo desde Noviembre hasta Marzo), 
y con estos nuevos DataFrames les añadí columnas como la media de la temperatura en esos periodos o también la temperatura mínima o máxima que había en cada año dentro del periodo, 
o en otro caso haciendo copias del DataFrame pero solo con datos en ciertos años. 

## !! (cambiar) **Visualización**
Tras preparar los datos necesarios, empezé con el análisis de estos, haciendo gráficos de puntos, de barras, y también histogramas, por ejemplo este gráfico que muestra la temperatura media, máxima, y mínima por año en el periodo de meses que definimos. <br>
![regplot](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/temp_a%C3%B1os_nov-mar.png) <br><br>
Otro gráfico que hice fue un histograma de temperaturas para ver cuál temperatura media era más común por mes en dos rangos de años, de 2000 a 2020 y de 1980 a 2000. <br>
![histplot 1](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/hist_temp_mes_nov-mar.png) <br>
O con la misma data también ví la cantidad de veces que se repetía cada temperatura media sin importar el mes.
![histplot 2](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/hist_temp_nov-mar.png) <br>
Y por último, para ver si algunos datos como la temperatura o presión podían estar relacionados, hice un heatmap.
![heatmap](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/heatmap.png)
