from flask import Flask, render_template

app = Flask(__name__)

# router -> eduardotreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "Esse é o meu primeiro site - Luize Weschenfelder Araujo"

@app.route("/contatos")
def contatos(): 
    return "<p>contatos do site: </p>Email:eduardo.nh1969@gmail.com <br>Fone: (51) 999456213"

# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

