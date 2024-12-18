import os 
from flask import Flask, render_template, send_from_directory

# Configurando o diretório dos templates e do app
templates_dir = os.path.abspath("./templates")

app = Flask(__name__, template_folder = templates_dir)

# router -> eduardotreinamentos.com/
# função -> o que você quer exibir naquela página
# template

# Rota para servir a página inicial
@app.route("/")
def homepage():
    return render_template("index.html")

# Rota para subpáginas do site
@app.route("/contatos")
def sobre(): 
    return render_template("sobre.html")

@app.route("/matricula")
def matricula():
    return render_template("matricula.html")

# Rotas para servir arquivos estáticos na pasta "templates"
@app.router("/img/<path:filename>")
def img_static(filename):
    send_from_directory(os.path.join(templates_dir, "img"), filename)

@app.router("/css/<path:filename>")
def css_static(filename):
    send_from_directory(os.path.join(templates_dir, "css"), filename)

@app.router("/js/<path:filename>")
def js_static(filename):
    send_from_directory(os.path.join(templates_dir, "js"), filename)

@app.router("/video/<path:filename>")
def video_static(filename):
    send_from_directory(os.path.join(templates_dir, "video"), filename)

# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

