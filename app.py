from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.date.today().strftime('%Y-%m-%d')
    return render_template('form.html', today=today)

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos del formulario
    full_name = request.form.get('full_name')
    date_of_birth = request.form.get('date_of_birth')
    available_days = request.form.get('available_days')
    favorite_location = request.form.get('favorite_location')
    taste_preference = request.form.get('taste_preference')
    meet_up = request.form.get('meet_up')

    # Guardar los datos en un archivo o base de datos
    with open('respuestas.txt', 'a') as file:
        file.write(f"Nombre completo: {full_name}\n")
        file.write(f"Fecha de nacimiento: {date_of_birth}\n")
        file.write(f"Días disponibles: {available_days}\n")
        file.write(f"Local favorito: {favorite_location}\n")
        file.write(f"Preferencia de sabor: {taste_preference}\n")
        file.write(f"¿Quiere juntarse?: {meet_up}\n")
        file.write("------------------------\n")

    # Establecer la variable de contexto 'success' en True
    success = True

    return render_template('form.html', success=success)

if __name__ == '__main__':
    app.run()
