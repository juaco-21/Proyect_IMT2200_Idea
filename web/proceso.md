---
nav_order: 3
---

# ⚙️ Proceso de recoleccion y desarollo de datos
### 🛠️ **Herramientas utilizadas**: Python a través de Jupyter Notebooks y algunas de las librerías, principalmente Pandas, Seaborn, Matplotlib, y Sklearn.

## ⛏️ **Recolección**
### 🏞️ **MeteoChile**:
De aquí recolectamos varia información, pero la que nos interesa para esto son:
<br>**1)** Máxima y mínima temperatura media por mes en cada año.
<br>**2)** Temperatura media por mes en cada año.
<br>**3)** Humedad, presión atmosférica media, y precipitación por mes.<br><br>
Esta data fue recopilada en diferentes archivos CSV, como:
* "maximo_temperaturas_maximas_santiago.csv": Temperatura máxima por mes.
* "media_temperaturas_minimas_santiago.csv": Temperatura mínima por mes.
* "media_temperaturas_maximas_santiago.csv": Temperatura media por mes.
* "humedad_mensual_santiago.csv": Humedad media por mes.
* "precipitaciones_mensuales_santiago.csv": Precipitación por mes.
* "presion_mensual_santiago.csv": Presión atmosférica media por mes.<br><br>

Son del formato ["Año",  "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

## 🪢 **Procesamiento**
Creamos los siguientes DataFrames de Pandas a partir de los archivos CSV mencionados anteriormente:<br>
* **df_maxim**: Hecho con CSV de temperatura máxima por mes.
* **df_minim**: Hecho con CSV de temperatura mínima por mes.
* **df_media**: Hecho con CSV de temperatura media por mes.
* **df_humed**: Hecho con CSV de la data de humedad mensual.
* **df_preci**: Hecho con CSV de la data de precipitación mensual.
* **df_presi**: Hecho con CSV de la data de presión atmosférica.

<div style="text-align: center;">

  <img src="{{ site.baseurl }}/web/imgs/imgs_proceso/ejemplo_df.PNG" 
       style="
           max-width: 90%; 
           height: auto; 
           display: block; 
           margin: 0 auto;
       ">
</div>

#### 📋 **df_maxim, df_minim, df_media, df_humed, df_preci, df_presi**
Con estos DataFrames creé los siguientes:
* **df_[Nombre de DataFrame]_v**: Copia del DataFrame pero solo con la data desde Noviembre a Marzo, que fué el plazo que escogimos para analizar. También tiene una columna añadida que junta toda la data de las otras columnas.<br>
Quedan del formato ["Año", "Noviembre", "Diciembre", "Enero", "Febrero", "Marzo", Media o max/min de los valores de la fila.]

<div style="text-align: center;">

  <img src="{{ site.baseurl }}/web/imgs/imgs_proceso/ejemplo_codigo.PNG" 
       style="
           max-width: 90%; 
           height: auto; 
           display: block; 
           margin: 0 auto;
       ">
</div>

**df_short_[Nombre de DataFrame]_v** : Una versión acortada de df_[Nombre de DataFrame]_v, solo con ["Año", Media o max/min de los valores de la fila.]<br>

<div style="text-align: center;">

  <img src="{{ site.baseurl }}/web/imgs/imgs_proceso/media_v y short_media_v.PNG" 
       style="
           max-width: 90%; 
           height: auto; 
           display: block; 
           margin: 0 auto;
       ">
</div>

#### 📋 **df_short_[Nombre de DataFrame]_short_v**
**df_combinado**: Un DataFrame con toda la data importante de cada DataFrame del rango de meses seleccionado.<br>
Queda del formato ["Año", "Media_humedad", "Media_precipitación", "Media_presión", "Media_temperatura", "Max_temperatura", "Min_temperatura"]<br>

<div style="text-align: center;">

  <img src="{{ site.baseurl }}/web/imgs/imgs_proceso/df_completo.PNG" 
       style="
           max-width: 90%; 
           height: auto; 
           display: block; 
           margin: 0 auto;
       ">
</div>

