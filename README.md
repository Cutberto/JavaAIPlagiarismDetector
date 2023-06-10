# JavaAIPlagiarismDetector
# Proyecto de Detección de Plagio en Código Java

Este proyecto utiliza un tokenizador programado en Python junto con modelos de procesamiento de lenguaje natural para determinar si existe plagio entre dos códigos de Java. El objetivo principal es brindar una herramienta automatizada que ayude a identificar similitudes o copias entre fragmentos de código.

## Funcionamiento

El proceso de detección de plagio consta de los siguientes pasos:

1. **Tokenización**: Se realiza una tokenización de los códigos fuente de Java utilizando el tokenizador implementado en Python. Este paso convierte el código en una secuencia de tokens (palabras, símbolos, operadores, etc.) que pueden ser procesados por los modelos de procesamiento de lenguaje natural.

2. **Creación de representación vectorial**: Se construye una representación vectorial de los tokens obtenidos. Esto implica transformar los tokens en vectores numéricos para que puedan ser comparados por los modelos.

3. **Comparación de similitud**: Se utiliza un modelo de procesamiento de lenguaje natural para calcular la similitud entre las representaciones vectoriales de los códigos fuente. Esto permite determinar qué tan similares son los códigos analizados.

## Uso

Sigue los pasos a continuación para utilizar este proyecto:

1. Clona o descarga el repositorio en tu máquina local.

2. Abre el notebook del modelo que deseas ejecutar (puedes elegir entre TF-IDF,ROUGE L, MATRICES DE TRANSICION, LSTM Y GPT2)

3. Si deseas ejecutar el prototipo de aplicación web, entra a la carpeta "app" y ejecuta el archivo "app.py" de la carpeta "back". Después de esto entra a la carpeta front y abre "index.html".

