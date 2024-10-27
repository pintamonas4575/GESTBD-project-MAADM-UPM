# **DATOS ESTRUCTURADOS**

• **Fuente de los Datos:** Dataset de Kaggle. [Formula 1 World Championship (1950 - 2024)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?select=constructors.csv)

• **Fecha de Recogida:** 19 Octubre 2024

• **Formato de los Datos:** Archivos CSV

• **Licencia de Uso:** [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

• **Descripción de las Variables o Atributos:** 

**TABLA DRIVERS**
- driverId -> Identificador de los pilotos (Clave primaria)
- driverRef -> Nombre de referencia del piloto
- number -> Número del piloto, en caso de no tener número permanente (pilotos previos a 2014) tendrá un valor de \N
- code -> Abreviatura del piloto
- forname -> Nombre del piloto
- surname -> Primer apellido del piloto
- dob -> Fecha de nacimiento del piloto
- nationality -> Nacionalidad del piloto
- url -> Enlace a la página de Wikipedia del piloto

**TABLA RESULTS**
- resultId -> Identificador del resultado (Clave primaria)
- raceId -> Identificador de la carrera (Clave foranea)
- driverId -> Identificador del piloto (Clave foranea)
- constructorId -> Identificador del constructor (Clave foranea)
- number -> Número que usaba el piloto en esa carrera
- grid -> Posición de salida
- position -> Posición final, en caso de retirada, descalificación o similar tendrá un valor de \N
- positionText -> Posición final en formato string, en caso de retirada, descalificación o similar tendrá un caracter indicativo
- points -> Puntos obtenidos por el piloto
- laps -> Número de vueltas completadas
- time -> Para el primer clasificado el tiempo total de finalización, para los pilotos no doblados el delta de tiempo con el primer clasificado, en el resto de casos \N
- miliseconds -> Para los resultados con valor diferente de \N en tiempo, el tiempo de carrera convertido a milisegundos
- fastestLap -> Número de vuelta donde el piloto realizó su vuelta más rápida
- rank -> En una clasificación de vueltas rápidas de una carrera, la posición de la vuelta rápida de ese piloto
- fastestLapTime -> El tiempo de la vuelta más rápida del piloto
- fastestLapSpeed -> Velocidad máxima de la vuelta rápida en millas por hora
- statusId -> Identificador del estado (Clave foránea)
