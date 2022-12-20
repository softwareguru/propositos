import functions_framework
import random

@functions_framework.http
def get(request):

    propositos = [
        "Terminar los cursos a los que me inscribo",
        "Aprender bien un lenguaje antes de comenzar con otro",
        "Dejar de hacer deploy en viernes",
        "Poner mejores comentarios en mis commits",
        "Tenerle más paciencia al Scrum Master",
        "No olvidar el 'Where' en el 'Delete'",
        "Lograr que mi crush sepa que es mi crush",
        "No involucrarme en discusiones inútiles en Twitter",
        "Trabajar en una Best Place to Code",
        "Ir a un evento Tech en otro país",
        "Reducir el tiempo que paso sentado",
        "Mejorar el setup en mi escritorio",
    ]

    return f"Mi propósito es: <br><h2>{random.choice(propositos)}.</h2><br><br><a href='/'>Intentar otra vez</a>."

