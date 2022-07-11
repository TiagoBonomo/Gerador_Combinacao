from flask import Flask, request, jsonify, render_template
from GeraLoto import GeNuLoto

app = Flask(__name__)


@app.route('/home')
def homepage():

    return render_template("homepage.html")


@app.route('/')
def lotofacil():
    resultado = "O site está funcionando ok !!!"

    q_combinacoes = request.args.get('q_combinacoes')
    q_dezenas = request.args.get('q_dezenas')

    loto_request = GeNuLoto(int(q_combinacoes), int(q_dezenas))
    res = loto_request.ge_comb()

    pares = request.args.get('par')
    fibonaci = request.args.get('finonaci')
    primos = request.args.get('primos')

    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
