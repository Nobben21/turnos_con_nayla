from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Frases por franja horaria
frases_por_franja = {
    "12:00-13:30": [
        "😴 Turno reservado. Nayla probablemente llegue 40 minutos tarde.",
        "⏳ Gracias por reservar. Ella te avisará... si se acuerda.",
        "😂 Mediodía es sagrado: si llega tarde, será por un buen motivo (¿almuerzo?).",
        "📵 No garantizamos asistencia. Pero tu esfuerzo cuenta.",
        "🍎 En la franja mediodía, Nayla puede estar mirando memes."
    ],
    "22:00-00:00": [
        "🌙 Turno nocturno reservado, pero espera sentado por las dudas",
        "😴 A esta hora, Nayla podría estar dormida o trabajando.",
        "👻 Turno válido solo si Nayla no esta ocupada.",
    ],
    "01:00-02:00": [
        "🌌 Madrugada mágica: turnos con poca certeza y muchas risas.",
        "🦉 Turno nocturno, solo para los valientes con paciencia.",
        "😴 Aquí la puntualidad es un mito, pero la diversión es real."
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        hora = request.form['hora']

        frases = frases_por_franja.get(hora, ["Turno reservado. ¡Pero quién sabe cuándo llega Nayla!"])
        frase_elegida = random.choice(frases)

        franja_texto = {
            "12:00-13:30": "Mediodía (12:00 - 13:30) - única posibilidad de contacto",
            "22:00-00:00": "Noche (22:00 - 00:00)",
            "01:00-02:00": "Madrugada (01:00 - 02:00)"
        }.get(hora, "Franja desconocida")

        mensaje = f"Turno reservado para {nombre} en la franja {franja_texto}. {frase_elegida}"

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
