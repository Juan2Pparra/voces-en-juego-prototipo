from datetime import datetime


def exportar_resultado(historia, blueprint, control, generado, validacion) -> str:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
    titulo = historia.get("titulo", "Historia")

    lineas = [
        "=" * 60,
        "VOCES EN JUEGO – RESULTADO DE GENERACIÓN NARRATIVA",
        f"Fecha: {ahora}",
        "=" * 60,
        "",
        f"HISTORIA: {titulo}",
        f"Ubicación: {historia.get('ubicacion', 'N/A')}",
        f"Emoción principal: {historia.get('emocion_principal', {}).get('emocion', '')}",
        f"Temas: {', '.join(historia.get('temas', []))}",
        "",
        "─── MÓDULO 1.3 – BLUEPRINT NARRATIVO ───",
        f"Tipo de escena: {blueprint['tipo_escena']}",
        f"Tono: {blueprint['tono']}",
        f"Objetivo: {blueprint['objetivo_narrativo']}",
        "",
        "─── MÓDULO 1.4 – CONTROL ÉTICO ───",
        "Reglas éticas aplicadas:",
        *[f"  • {r}" for r in control["reglas_eticas"]],
        "",
        "─── MÓDULO 1.5 – CONTENIDO GENERADO ───",
        "ESCENA:",
        generado["escena"],
        "",
        "DIÁLOGO NPC:",
        generado["dialogo_npc"],
        "",
        "DECISIONES:",
        generado["decisiones"],
        "",
        "─── MÓDULO 1.6 – VALIDACIÓN ───",
        f"Estado: {validacion['estado']}",
        f"Puntuación: {validacion['puntuacion']}/100",
        "",
        "Observaciones:",
        *[f"  {o}" for o in validacion["observaciones"]],
    ]

    if validacion["alertas"]:
        lineas += ["", "Alertas:", *[f"  {a}" for a in validacion["alertas"]]]

    lineas += ["", "=" * 60]
    return "\n".join(lineas)