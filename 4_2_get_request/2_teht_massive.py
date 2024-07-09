from typing import List
from functools import reduce

from flask import Flask, request

app = Flask(__name__)

@app.route('/massive/', methods=['GET'])
def massive():
    mass_numbers: List[int] = request.args.getlist('number', type=int)
    summ = sum(mass_numbers)
    multiple = reduce((lambda x, y: x * y), mass_numbers)
    return f'Lukujen summa on {summ} \n Lukujen kertolasku on {multiple}'


if __name__ == '__main__':
    app.run(debug=True)
