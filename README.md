# Generador de propósitos para devs 

App sencillísima que te provee un propósito.

Como puedes ver, es un simple programa en Python (main.py) que escoje al azar un elemento de entre una lista de propósitos predefinida.

Cosas a tener en cuenta:
  1. Está hecho para correr en Google Cloud Run, por eso usamos el decorador @functions_framework.http. 
  2. Para ejecutarse en Google Cloud Run requiere los paquetes functions-framework, flask y google-cloud-error-reporting (por eso están en el requirements.txt).
  3. La respuesta es una página html. Se puede responder directamente con un string con todo el html, pero queda muy sucio, así que mejor creamos una plantilla con el html base, y la llenamos con la funcion render_template de flask.
  4. Lee el valor del http header "Accept-language", y si encuentra el texto "es" usa la lista y plantillas en español, sino usa las que están en inglés. 
 
 
