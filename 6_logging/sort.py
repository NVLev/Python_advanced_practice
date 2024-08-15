import heapq
import json
import logging
from typing import List

from flask import Flask, request

app = Flask(__name__)

logger = logging.getLogger("sort")


def bubble_sort(array: List[int]) -> List[int]:
    n = len(array)
    logger.info('Aloitan bubble_sort')
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    logger.info('Lopetin bubble_sort')
    return array


def tim_sort(array: List[int]) -> List[int]:
    logger.info('Aloitan tim_sort')
    array.sort()
    logger.info('Lopetin tim_sort ')
    return array


def heap_sort(array: List[int]) -> List[int]:
    data = []
    logger.info('Aloitan Heap_sort')
    for val in array:
        heapq.heappush(data, val)
    logger.info('Lopetim')
    return [heapq.heappop(data) for _ in range(len(data))]


algorithms = {
    "bubble": bubble_sort,
    "tim": tim_sort,
    "heap": heap_sort,
}


@app.route("/<algorithm_name>/", methods=["POST"])
def sort_endpoint(algorithm_name: str):
    if algorithm_name not in algorithms:
        return f"Bad algorithm name, acceptable values are {algorithms.keys()}", 400

    form_data = request.get_data(as_text=True)

    array = json.loads(form_data)

    result = algorithms[algorithm_name](array)

    return json.dumps(result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    logger.info("Started sort server")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
