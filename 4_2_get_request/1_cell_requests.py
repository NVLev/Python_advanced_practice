"""ЗАдача - отправить на сервер get-запрос и получить данные о клиентах
сотовых вышек, отобранный по определенным параметрам"""
from typing import List, Optional
from datetime import date
from flask import Flask, request

app = Flask(__name__)


@app.route('/search/', methods=['GET'])  # даем понять серверу, что мы имеем дело с GET
def search():
    cell_tower_ids: List[int] = request.args.getlist('cell_tower_id', type=int)

    if not cell_tower_ids:
        return f'You must specify at least one cell_tower_id', 400

    for i in cell_tower_ids:
        if i <= 0:
            return f'Your speified a wrong number', 400

    phone_prefixes: List[str] = request.args.getlist('phone_prefix')
    for phone_prefix in phone_prefixes:
        if phone_prefix != r'^\d{1,10}[\*\]':
            return (f'The phone prefix should contain only digits (not more than 10) '
                    f'and * after them', 400)

    protocols: List[str] = request.args.getlist('protocol')
    protocols_list = ['2G', '3G', '4G']
    for protocol in protocols_list:
        if protocol not in protocols_list:
            return f'Protocol should be 2G, 3G or 4G', 400

    signal_level: Optional[float] = request.args.get(
        'signal_level', type=float, default=None
    )
    # date.today().strftime('%Y%m%d') YYYYmmdd
    current_date: date = date.today()
    date_from: Optional[date] = request.args.get('time_stamp')

    date_to: Optional[date] = request.args.get('time_stamp')
    if date_from > current_date or date_to > current_date:
        return "Wrong date!", 400
    if date_to > date_from:
        return "Wrong date_to!", 400

    return (
        f'Search for {cell_tower_ids} cell towers.  Search criteria: '
        f'phone_prefixes={phone_prefixes}, '
        f'protocols={protocols}, '
        f'signal_level={signal_level}'
    )


if __name__ == '__main__':
    app.run(debug=True)
