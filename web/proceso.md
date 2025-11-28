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

#### **df_maxim, df_minim, df_media, df_humed, df_preci, df_presi**
Con estos DataFrames creé los siguientes:
* **[Nombre de DataFrame]_v**: Copia del DataFrame pero solo con la data desde Noviembre a Marzo, que fué el plazo que escogimos para analizar.<br>
![Ejemplo de código](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/ejemplo_codigo.PNG) <br>
(Ejemplo de código para conseguir data de los meses deseados)<br>

#### **[Nombre de DataFrame]_v**
* **df_combinado**: Un DataFrame con toda la data importante de cada DataFrame del rango de meses seleccionado.<br>
  ![Screenshot df_combinado](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/df_completo.PNG)<br>
Otro gráfico que hice fue un histograma de temperaturas para ver cuál temperatura media era más común por mes en dos rangos de años, de 2000 a 2020 y de 1980 a 2000. <br>
![histplot 1](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/hist_temp_mes_nov-mar.png) <br>
O con la misma data también ví la cantidad de veces que se repetía cada temperatura media sin importar el mes.
![histplot 2](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/hist_temp_nov-mar.png) <br>
Y por último, para ver si algunos datos como la temperatura o presión podían estar relacionados, hice un heatmap.
![heatmap](https://github.com/juaco-21/Proyect_IMT2200_Idea/blob/main/web/imgs/imgs_proceso/heatmap.png)
