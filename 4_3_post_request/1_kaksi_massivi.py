from typing import List
import itertools
from flask import Flask, request

app = Flask(__name__)


@app.route('/massive', methods=['POST'])
def massive():
    mass_numbers1: List[int] = request.form.getlist('number', type=int)
    mass_numbers2: List[int] = request.form.getlist('number2', type=int)
    if len(mass_numbers1) != len(mass_numbers2):
        return f'Listat pitää olla yhtä pitkiä!'
    else:
        permut = itertools.permutations(mass_numbers1, len(mass_numbers2))
        print(permut)
        unique_combinations = []
        for comb in permut:
            zipped = zip(comb, mass_numbers2)
            unique_combinations.append(list(zipped))
    return f'Lukujen permutations ovat {unique_combinations}'


if __name__ == '__main__':
    app.run(debug=True)