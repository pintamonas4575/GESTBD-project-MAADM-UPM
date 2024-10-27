# **DATOS NO ESTRUCTURADOS**

• **Fuente de los Datos:** Rankings periódicos de la F1. [F1 Power Rankings](https://www.formula1.com/en/latest/tags/power-rankings.699Peq5SC9zNGvwCkb1ln6?page=1)

• **Fecha de Recogida:** 27 octubre 2024.

• **Formato de los Datos:** Archivo CSV.

• **Licencia de Uso:**  *Copyright* de **Formula One World Championship Limited**.

• **Descripción de las Variables o Atributos:** Creación de un CSV a partir de datos no estructurados mediante *web scraping*. El archivo está ordenado desde el ranking más reciente (primeras filas) hasta el más antiguo scrapeado (últimas filas). A su vez, cada ranking está ordenado con las posiciones de los pilotos desde el primero hasta el décimo. 

**Archivo *weekly_rankings_info***

- ranking_date -> El día en el que se publicó el ranking. Formato YYYY-MM-DD.
- pilot_name -> Nombre del piloto en el ranking.
- pilot_review -> Descripción del rendimiento del piloto.
- ranking_link -> Enlace a la página web del ranking.