# Week 3 · Asistente de Café Aurora con LangChain

Asistente para el personal de Café Aurora: conversa recordando lo que le dices, y convierte
una reseña en datos validados más una respuesta sugerida. LM Studio local u OpenAI.

## Instalación

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # Windows: copy .env.example .env
```

## Configuración

- **LM Studio (gratis):** deja `USE_LOCAL_LLM=true`, carga `llama-3.2-3b-instruct` y enciende el servidor.
- **OpenAI (con la key del curso):** pon `USE_LOCAL_LLM=false` y la key que te dio tu instructor en `OPENAI_API_KEY`.

## Uso

```bash
python week3_assistant.py          # chat con memoria ("salir" para terminar)
python week3_assistant.py reply    # reseña a ReviewData + respuesta sugerida
python test_assistant.py           # pruebas sin servidor
```

## Decisiones

- `ChatOpenAI` configurado desde `.env`: un solo archivo para local y nube.
- Prompts en `prompts.py`, como `ChatPromptTemplate`; el modelo lee instrucciones en inglés.
- Modo reply: una cadena LCEL de dos pasos, extracción con `with_structured_output` (temperatura 0) y respuesta (temperatura 0.3).
- Memoria: historial explícito con `MessagesPlaceholder`, recortado a los últimos 10 mensajes con `trim_messages`. Sin APIs deprecadas.
- Errores capturados por clase del SDK; `ValidationError` si el JSON no cumple `ReviewData`, `LengthFinishReasonError` si se cortó y `OpenAIRefusalError` si el modelo se negó.