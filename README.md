Instrucciones para la ejecución de la aplicación codificada en el lenguaje Python: 
1. pip install mysqlclient
2. pip install mysql-connector-python
3. Modify app.py and docker-compose.yml with the corresponding MySQL configurations

    mysql_host = 'localhost'
    mysql_database = 'ChallengeMeLi'
    mysql_user = 'root'
    mysql_pass = '123456'

4. cd src
5. py .\app.py

6. Entregables: 

7. Codigo Fuente:  https://github.com/adimasi-prog/challengeMeli

8. La aplicacion se encuentra Dockerizada y las bases fueron normalizadas

9. Descripción de la aplicación realizada, supuestos, problemas y soluciones con los que se   encontró al realizar la misma.

   9.1  La aplicación tiene por objetivo principal contribuir en el proceso de revalidas anuales con la automatización del envió de mails hacia los managers de las bases más criticas clasificadas como “High”

   9.2 Supuestos: Si alguno de los ítems que componen a la clasificación de las bases (Confidentiality/Integrity/Availability) es “High”, entonces asumimos que la clasificación es “High”. En caso de que ninguno sea catalogado como “High” y al menos uno este catalogado como “Medium”, asumimos que la clasificación es “Medium”. En caso contrario la clasificación se considerará como “Low”.

   9.3 Entre los problemas y soluciones encontradas al realizar la misma puedo enumerar los siguientes considerando mis skills básicos en desarrollo: 
       9.3.1 Conexiones a la base de datos cuya solución fue en base a consulta en la web, así como con colegas
       9.3.2 Manejo de funciones/objetos/clases: Mi background no es de desarrollo con lo cual tuve que recurrir a tutoriales para el correcto entendimiento de la lógica, así como de los comandos que requiere Python para el manejo de estos.
       9.3.3 Recurrí a tutoriales para la búsqueda de comandos del lenguaje Python
       9.3.4 A su vez consulte con colegas para poder validar con ellos si la lógica implementada en la codificación se alineaba a las buenas prácticas de programación y para evitar redundancias en búsquedas y lecturas en bases/archivos
       9.3.5 Para Dockerizar la aplicación, consulte con colegas para entender la lógica y la ejecución de este requerimiento
       9.3.6 Por último, me encontré con errores en la salida de la ejecución de la aplicación por errores en el código lo cual pude solucionarlo revisando material en la web y haciendo consultas a colegas que se dedican al desarrollo
