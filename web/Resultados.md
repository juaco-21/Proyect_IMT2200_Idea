---
nav_order: 4
---
# ✅ Análisis y resultados

## ❗ Informacion Crucial del Contexto Para Esta Parte

Nuestras motivaciones son las de entender y anticipar un fenomeno climatico importante en Chile o principalmente Santiago de Chile, la capital del pais.

Las preguntas claves que ayudan a dar con el analisis son:

1) ¿Han aumentado o se han extendido las Olas de Calor en Santiago históricamente? 

2) ¿Podemos predecir la ocurrencia de una Ola de Calor con base en otros factores climáticos?

Para poder responder la segunda pregunta, transformamos este objetivo y su respuesta en un problema de Clasifocacion Binaria o una pregunta que se puede responder con un si i un no. Lo cual la simplifica bastante, ya que diremos si un mes tuvo olas de calor como un Si o un No.

## 🔥 ¿Como Modelamos una Ola de Calor para este problema?

1) Lo definimos como un evento extremo, ya que esta depende de las temperaturas altas.  Para que un mes fuera clasificado como una Ola de Calor, establecimos una regla de clasificacion: La tamperatura maxima mensual debia superar el Percentil 90 o ser parte del 10% de las temperaturas mas altas entre los meses de la distribucion historica. 

- En otras palabras, solo el 10% de los meses mas calurosos en la historia de Santiago seran etiquetados como eventos extremos (Olas de Calor). Esta regla asegura que el modelo prediga solo el calor anomalo(temperaturas que son significativamente más altas de lo normal para un lugar y época específicos).

2) Variables Predictivas: Para las variables de prediccion excluimos la temperatura maxima (Ya que la utilizamos para definir que es una ola de calor) y nos centramos en cuatro factores metereologicos clave, elegimos los siguientes:

- Presión Atmosférica: Directamente asociada a la nubosidad y la estabilidad del aire.

- Radiación UVB Máxima: Precursor directo del calentamiento diario.

- Humedad Media: El aire seco permite que la temperatura suba más fácilmente.

- Precipitación: La ausencia de lluvia (sequía) es un factor conocido en la intensificación del calor extremo.


<div style="text-align: center;">

  <img src="{{ site.baseurl }}/assets/images/Matriz de Confusion kNN.png" 
       style="
           max-width: 90%; 
           height: auto; 
           display: block; 
           margin: 0 auto;
       ">

</div>

## 📝 Evaluacion y Significado de los Resultados

Comparamos dos modelos predictivos: la Regresion Logistica (un modelo lineal y simple) y la Clasificacion k-Nearest Neighbors (kNN) (un modelo no lineal, basado en patrones de distancia).

### 🤝 Confiabilidad de los Modelos

Ya que las Olas de Calor son un evento poco frecuente, metricas como la Precisión (que tan confiable es) y el Recall (nuestra capacidad de detección acertada). Vamos a dar los siguientes ejemplos de que representan para una mayor comprension:

- Precisión significa en el contexto de nuestros datos, cuantas olas de calor predijimos de forma acertada entre 10 meses. Por ejemplo si la presision fuera del 84%, entonces de cada 10 alarmas de Olas de Calor que se emiten, nuestro modelo predijo 8 correctamente.

- Recall significa la deteccion de Olas de Calor que realmente ocurren, la cantidad de ellas que nosotros detectamos. Por ejemplo si el recall fuera del 66% de todas las olas de calor que realmente ocurrieron, solo detectamos 6.5 de cada 10 Olas de Calor. Que nos dice el margen de error de forma mas clara.

Tambien es importante destacar que los modelos que utilizamos fueron muy similares. Lo cual implica que la relacion entre la presión, la humedad y otras variables es bastante clara. De hecho es tan clara que se puede describir con una relacion lineal simple (la Regresion Logistica), lo que los india que no se necesitan algoritmos complejos para dar con esta prediccion.

## 🖼️ El Mapeo de Errores: Matriz de Confusion

- La Matriz de Confusion es el mapa que nos dice donde acierta y donde falla el modelo.

<div style="text-align: center;">

  <img src="{{ site.baseurl }}/assets/images/Matriz de Correlacion de Variables Cilmatologicas.png" 
       style="
           max-width: 90%; 
           height: auto; 
           display: block; 
           margin: 0 auto;
       ">
</div>


Se puede decir que, nuestro modelo es muy confiable cuando predice, aunque pierda algunos eventos extremos, por lo general cuando acierta es bastante probable que sea verdad.

### ✅ Conclusion de la pregunta

El modelamiento que realizamos demostro que las variables climaticas (Presion Atmosferica, Humedad Media, Precipitacion y Radiacion UV Maxima) son predictivas para la ocurrecia de una Ola de Calor con una confianza de 84% por la metrica de Presicion. Ademas el uso del modelo de kNN valida por asi decirlo, la hipotesis inicial que teniamos, la cual esra que las condiciones atmosfericas que preceden a una Ola de Calor siguen los patrones distintivos los cuales deberian de replicarse apartir de los datos historicos. 


## 😣 Preocupaciones y Extensiones Futuras

__Problematicas Globales__: Nuestros hallazgos reafirman que los factores atmosfericas asociados el cambio climatico, tales como el aumento de la radiacion UV y la baja de humedad. Estos son factores que aportan (Como se ve en la matriz de correlacion) a la concurrencia de Olas de Calor. La capacidad de poder predecir estos eventos (Las Olas de Calor) es algo esencial o importante para la gestion y prevencion de riesgo asociados a estos eventos, como los incendios forestales y posibles golpes de calor en la poblacion.


### ✨ Analisis a Fururo y Mejoras 

1) Se podria mejorar el umbral de eleccion de olas de calor, evaluandolo por dia y no por meses. Dando con una prediccion mas presica y practica. 

2) Inclusion de tiempos o evaluaciones mas espacificas o local, tal como analizar si las variables de mediados de marzo y/o otoño, evaluendo las muestras de estos periodos para ver si tienen patrones de temperatura irregulares o afectados por la extencion del verano. Lo cual responderia a la pregunta de a extencion de estaciones que destacan por temperaturas mas altas/calidas.

3) Tambien el impacto de los datos geograficos, puede alterar de sobre manera los resultados y incluso ser mas presisos o fieles a la realidad. Tambien podemos ver la distribucion o variabilidad entre zonas globales o locales. 


