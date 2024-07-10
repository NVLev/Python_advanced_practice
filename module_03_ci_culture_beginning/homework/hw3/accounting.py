from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    vuosi = str(date)[:4]
    kuukausi = str(date)[4:6]
    storage.setdefault(vuosi, {}).setdefault(kuukausi, 0)
    storage[vuosi][kuukausi] += number
    return f'{number} on kirjattu ohjelmaan.  Hyvää päivänjatkoa.'  # Расходы внесены в программу.  Хорошего дня


@app.route("/calculate/<int:vuosi>")
def calculate_year(vuosi: int):
    vuosi = str(vuosi)
    if vuosi in storage:
        menot = sum(storage[vuosi].values())
        return f'Tämän vuoden kokonaismenot ovat {menot}'  # Суммарные расходы этого года
    else:
        return 'Tänä vuonna ei ole vielä ollut menoja'    # В этом году еще не было расходов


@app.route("/calculate/<int:vuosi>/<int:kuukausi>")
def calculate_month(vuosi: int, kuukausi: int):
    vuosi = str(vuosi)
    if kuukausi < 10:
        kuukausi = '0' + str(kuukausi)
    else:
        kuukausi = str(kuukausi)
    if vuosi in storage:
        if kuukausi in storage[vuosi]:
            menot = storage.get(vuosi, {}).get(kuukausi)
            return f'Tämän kuukauden kokonaismenot ovat {menot}'  # Суммарные расходы этого года
    else:
        return 'Tässä kuukaudessa ei ole vielä ollut menoja'  # В этом месяце еще не было расходов




if __name__ == "__main__":
    app.run(debug=True)
