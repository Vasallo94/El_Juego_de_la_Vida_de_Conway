# El Juego de la Vida de Conway
Implementación del Juego de la Vida de Conway en Python utilizando la biblioteca Pygame.

El Juego de la Vida de Conway es un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Se trata de un juego de cero jugadores, lo que significa que su evolución está determinada por el estado inicial y no necesita ninguna interacción adicional. A pesar de su simplicidad, el Juego de la Vida de Conway exhibe una amplia gama de comportamientos complejos.

## Las reglas del Juego de la Vida de Conway son las siguientes:

- Cualquier célula viva con menos de 2 vecinos vivos muere, debido a la soledad.
- Cualquier célula viva con 2 o 3 vecinos vivos sigue viva en la siguiente generación.
- Cualquier célula viva con más de 3 vecinos vivos muere, debido a la sobrepoblación.
- Cualquier célula muerta con exactamente 3 vecinos vivos se convierte en una célula viva, debido a la reproducción.

Estas reglas determinan cómo evolucionan las células en cada generación del juego. A partir del estado inicial, se aplican estas reglas para calcular el estado de las células en la siguiente generación. Este proceso se repite iterativamente para simular la evolución y el comportamiento del sistema.


## Instalación

1. Clona este repositorio:

   ```
   git clone https://github.com/Vasallo94/El_Juego_de_la_Vida_de_Conway
   ```
2. Navega hasta el directorio del proyecto haciendo:
    ```
    cd El_Juego_de_la_Vida_de_Conway
    ```
3. Instala las dependencias utilizando pip:
    ```
    pip install -r requirements.txt
    ```
    
## Uso
1. Ejecuta el script del juego:
    ```
    python game_of_life.py
    ```
2. Pulsa cualquier tecla para pausar el tiempo
3. Dibuja con el click del ratón las células vivas con las que quieres que se inicie tu mundo
4. Pulsa cualquier tecla para pausar o reanudar el juego.
5. Disfruta de la vida y la muerte
6. Cierra la ventana del juego para salir.

## Contribución
Las contribuciones son bienvenidas. Si tienes alguna idea o mejora, por favor crea un issue o envía una pull request.

## Recursos adicionales
[Wikipedia](https://es.wikipedia.org/wiki/Juego_de_la_vida) - Juego de la Vida
[Video interesante](https://www.youtube.com/watch?v=2ssnMkJFqbA) sobre el Juego de la Vida de Conway
