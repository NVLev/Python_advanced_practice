import csv
from typing import Optional
import logging
from flask import Flask
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)

logger = logging.getLogger('person_id_checker')


@app.route('/bank?api/<branch>/>int:person?id>')
def bank_api(branch: str, person_id: int):
    branch_card_file_name = f'bank_data/{branch}.csv'

    with open(branch_card_file_name, 'r') as fi:
        csv_reader = csv.DictReader(fi, delimiter=',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
            else:
                return 'Person not found', 404


@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        logger.error(
            f'Tiedosto eei ole löytanyt.  Olen yrittänyt avata  {original.filename}. '
            'Poikkeustieto: {original.strerror}\n'
        )

    elif isinstance(original, OSError):
        logger.error(f'Korttia ei voi käyttää. Poikkeustiedot:{original.strerror}\n')
        with open('invalid_error_log', 'a') as fo:
            fo.write(f'Unable to access a card. Exception info: {original.strerror}\n')
    return 'Internal server error', 500


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    app.run()
