# Реализуйте flask endpoint, принимающий на вход отсортированный массив
# A и число X, и возвращающий число из массива A, максимально близкое к числу X.

from typing import List

from flask import Flask, request

app = Flask(__name__)


@app.route('/massive/', methods=['GET'])
def massive():
    mass_numbers: sorted(List[int]) = request.args.getlist('number', type=int)
    xnum: int = request.args.get('x', type=int)
    tulos = min(mass_numbers, key=lambda x: abs(x - xnum))
    return f'X lähin luku on {tulos}'

if __name__ == '__main__':
    app.run(debug=True)