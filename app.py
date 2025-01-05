from flask import Flask, render_template_string

app = Flask(__name__)

# HTML proporcionado
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problemas Ambientales Críticos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        header {
            text-align: center;
            padding: 20px;
            background: #4CAF50;
            color: white;
        }
        section {
            background: white;
            margin: 20px auto;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            max-width: 800px;
        }
        h1, h2 {
            color: #333;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Problemas Ambientales Críticos y Soluciones</h1>
    </header>
    <section>
        <h2>1. Cambio climático</h2>
        <ul>
            <li><strong>Causas:</strong> Emisión de gases de efecto invernadero, deforestación, agricultura intensiva.</li>
            <li><strong>Soluciones:</strong>
                <ul>
                    <li>Transición a energías renovables.</li>
                    <li>Reducción de emisiones de CO₂.</li>
                    <li>Promoción del transporte sostenible.</li>
                    <li>Restauración de ecosistemas.</li>
                </ul>
            </li>
        </ul>
        <h2>2. Pérdida de biodiversidad</h2>
        <ul>
            <li><strong>Causas:</strong> Deforestación, urbanización, contaminación.</li>
            <li><strong>Soluciones:</strong>
                <ul>
                    <li>Creación y protección de áreas naturales.</li>
                    <li>Regulación del comercio ilegal de especies.</li>
                    <li>Prácticas agrícolas sostenibles.</li>
                </ul>
            </li>
        </ul>
    </section>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
