"""
debug_demo.py: ver cada paso de la cadena con su entrada y su salida.
"""

# set_debug enciende la traza de LangChain; StrOutputParser cierra la cadena con texto
from langchain_core.globals import set_debug
from langchain_core.output_parsers import StrOutputParser

# Lo tuyo: la configuración, el modelo y el prompt del chat
from aurora_llm import create_llm, load_config
from prompts import CHAT_PROMPT

set_debug(True)  # desde aquí, cada pieza imprime lo que recibe y lo que devuelve
chain = CHAT_PROMPT | create_llm(load_config()) | StrOutputParser()  # la misma cadena del chat
chain.invoke({"history": [], "question": "¿Qué es un cortado?"})  # history vacío: el prompt lo pide