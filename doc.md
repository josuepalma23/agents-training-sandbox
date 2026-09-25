# Documentación inicial: Agente básico de recolección de información para citas en formato APA 7.

Inicialmente, la idea era desarrollar un agente con una lógica implementada que ayude a recolectar información pública sobre libros, atributos básicos como ISBN, título, año de publicación, etc. El presente código subido a la fecha 25/09/2026 solo tiene implementa una herramienta, lo que quiere decir que hacen falta las implementaciones de formateo, otras ideas, etc.

A continuación, se explica la lógica de esta herramienta:

Deberá notarse que parte de la presente herramienta está desarrollada **a partir de una plantilla.**

Se declara @tool como estándar en Python.

Para el parámetro, devolverá un valor str, siendo este un json extenso incluyendo la información proporcionada por la API. Así mismo, se llama a la misma con su respectivo URL, pasándole como parámetros los atributos necesarios de cada libro antes mencionados.

Dentro del bloque try-catch, se incluyen las declaraciones de las respuestas formateadas a json, se hace una validación simple sobre la existencia del libro dentro de la API. Seguido de eso, simplemente se utilizan métodos básicos para unir este json con la información recolectada.

Nota: Para el atributo ISBN, recolectamos hasta 5 disponibles dentro de la web.

Finalmente, se utiliza el token clásico de HuggingFace (oculto) para utilizar un número determinado de tokens, temperatura, etc. (Se cambiará a Ollama en un futuro).

### Pasos al futuro: Raghilda y flujo de trabajo para formateo.

- Para el futuro, el agente prescindirá de un token clásico de HuggingFace, ejecutando un modelo ligero utilizando Ollama.

- Eliminaré la necesidad de utilizar GradioUI, tengo la idea de implementar un tracer con el server phoenix, de manera que se almacenen los datos y se evidencie el proceso que sufrirá el agente al aprender esta nueva habilidad.
