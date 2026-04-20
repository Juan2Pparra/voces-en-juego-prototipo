import json
import streamlit as st


@st.cache_data
def cargar_historias():
    with open("voces_en_juego/historias.json", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def cargar_textos():
    try:
        with open("voces_en_juego/textos.json", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return {item["_id"]: item for item in data if "_id" in item}
        return data
    except Exception:
        return {}


@st.cache_data
def cargar_fuentes():
    try:
        with open("voces_en_juego/fuentes.json", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return {item["_id"]: item for item in data if "_id" in item}
        return data
    except Exception:
        return {}