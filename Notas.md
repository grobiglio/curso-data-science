# Notas del curso de Ciencia de Datos

Los que se muestran en la siguiente figura son los pasos típicos que todo científico de datos hace en su proyecto de Inteligencia Artificacial.

![Pasos](./figuras/data-scince-steps.png)

Lo primero que debemos hacer es definir el problema y asegurarnos que que estamos haciendo las preguntas correctas.

Cuestiones a tener en cuenta acerca de los datos:
* Fuente de datos
* Descripción del conjunto de datos
* Cantidad de datos
* Número de aspectos (_features_) medidos (columnas del _dataframe_)
* Nombre de los aspectos (_features_)
* Descripción de cada aspecto

![Consideraciones](./figuras/consideraciones-sobre-datos.png)

Features: Columnas del dataset. Estos son los atributos del conjunto de datos.
Instance: Filas del dataset.

:warning: No es lo mismo _atributo_ en Machine Learning que en programación. :warning:

:warning: No es lo mismo _instance_ en Machine Learning que en programación. En programación, una instancia es un objeto. :warning:

En la visualización de datos nos interesan dos cosas:
* Distribución. Normalmente se aprecia con histogramas.
* Valores atípicos (outliers)

## ¿Cómo aprenden las computadoras?

Predice los coeficientes de la ecuación que definimos como hipótesis, luego estima el error de predicción. Tener en cuenta que si nuestra hipótesis es errónea el problema no es de la computadora.

![ML-Steps](./figuras/machine-learning-steps.png)

Otros términos con los que se suele hacer referencia a la función de costo o Cost Function: Loss Function, Error Function, Objective Function.

En Machine Learning, la Función de Costo que se utiliza es el Error Medio Cuadrático (MSE - Mean Squared Error). Esta es una variante del residuo de la suma de los cuadrados, que provee una idea de la cantidad de muestras que mi hipótesis no es capaz de representar.

![MSE](./figuras/MSE.png)

Las variables ficticias (dummy variables) captan información binaria en los datasets.