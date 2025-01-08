import os
from flask import Flask, render_template, send_from_directory

# Configurando o diretório dos templates e do app
template_dir = os.path.abspath("./templates")
app = Flask(__name__, template_folder=template_dir)
# router -> eduardotreinamenmtos.com/
# função -> o que você quer exibir naquela página
# template

# Rota para servir a página inicial
@app.route("/")
def hompage():
    return render_template("index.html")

# Rota para subpáginas do site
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/matricula")
def matricula():
    return render_template("matricula.html")

# Rotas para servir arquivos estáticos na pasta "templates"
@app.route("/img/<path:filename>")
def img_static(filename):
    send_from_directory(os.path.join(template_dir, "img"), filename)

@app.route("/css/<path:filename>")
def css_static(filename):
    send_from_directory(os.path.join(template_dir, "css"), filename)

@app.route("/js/<path:filename>")
def js_static(filename):
    send_from_directory(os.path.join(template_dir, "js"), filename)

@app.route("/video/<path:filename>")
def video_static(filename):
    send_from_directory(os.path.join(template_dir, "video"), filename)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

