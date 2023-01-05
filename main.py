import functions_framework
import random, re
from flask import render_template

@functions_framework.http
def get(request):

    template ="base_es.html"

    propositos = [
        "Terminar los cursos a los que me inscribo",
        "Dejar de hacer deploy en viernes",
        "Poner mejores comentarios en mis commits",
        "Tenerle más paciencia al Scrum Master",
        "No olvidar el 'Where' en el 'Delete'",
        "Lograr que mi crush sepa que es mi crush",
        "No involucrarme en discusiones inútiles en Twitter",
        "Trabajar en una Best Place to Code",
        "Reducir el tiempo que paso sentada(o)",
        "Dar una charla en un evento internacional",
        "Contribuir a un proyecto open source",
        "Publicar más en mi blog",
        "Impulsar a más mujeres en tecnología"
    ]

    propositos_en = [
        "Finishing the courses that I enroll in",
        "Stop deploying on Fridays",
        "Putting better messages in my commits",
        "Being more patient with the Scrum Master",
        "Remembering to add a 'Where' in the 'Delete'",
        "My crush knowing how I feel about them",
        "Not getting tangled in useless discussions in Twitter",
        "Working at a company where I feel appreciated",
        "Decreasing the time I spend sitting",
        "Presenting a talk in an international event",
        "Contributing to an open source project",
        "Writing more in my blog",
        "Empower more women in tech"
    ]

    if not re.search("es", request.headers['Accept-Language']):
        propositos = propositos_en
        template = "base_en.html"

    return render_template(template, proposito=random.choice(propositos))

