import importlib.resources
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, load_tool, tool
import datetime
import requests
import pytz
import yaml
from smolagents import FinalAnswerTool
from smolagents import GradioUI

@tool
def book_data(titulo: str) -> str:
    """
    Busca el titulo de un libro y retorna datos relevantes sobre el mismo

    Args:
        titulo: El nombre o titulo del libro a buscar.
    """
    # Api publica de Open Library
    url = "https://openlibrary.org/search.json"
    params = {
        "title": titulo,
        "limit": 1,
        "fields": "title,author_name,first_publish_year,isbn"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Verificar que la API encontro el libro
        if not data.get("docs"):
            return f"No se encontraron resultados para '{titulo}'."

        libro = data["docs"][0]

        titulo_oficial = libro.get("title", "Titulo desconocido")
        autor = ", ".join(libro.get("author_name", ["Autor desconocido"]))
        fecha = str(libro.get("first_publish_year", "Fecha_desconocida"))
        
        lista_isbns = libro.get("isbn", [])

        if lista_isbns:
            isbns_str = ", ".join(lista_isbns[:5])
        else:
            isbns_str = "ISBN desconocido."


        return (f"Titulo: {titulo_oficial}\n"
                f"Autor: {autor}\n"
                f"Fecha de publicacion: {fecha}\n"
                f"ISBN: Hasta los primeros 5 encontrados: {isbns_str}")

    except Exception as e:
        return f"Ocurrio un error en la consulta {str(e)}"

final_answer = FinalAnswerTool()
model = InferenceClientModel(
            max_tokens=2096,
            temperature=0.5,
            model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
            token='token_huggingface',
            custom_role_conversions=None
)

agent = CodeAgent(
         model=model,
         tools=[final_answer, book_data],
         max_steps=6,
         verbosity_level=1,
)

GradioUI(agent).launch()




