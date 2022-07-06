from flask import Flask, request
from GeraLoto import GeNuLoto

app = Flask(__name__)


@app.route('/lotofacil')
def lotofacil():
    resultado = "O site está funcionando ok !!!"

    q_combinacoes = request.args.get('q_combinacoes')
    q_dezenas = request.args.get('q_dezenas')

    loto_request = GeNuLoto(int(q_combinacoes), int(q_dezenas))
    res = loto_request.ge_comb()

    pares = request.args.get('par')
    fibonaci = request.args.get('finonaci')
    primos = request.args.get('primos')

    return res


if __name__ == "__main__":
    app.run(debug=True)
