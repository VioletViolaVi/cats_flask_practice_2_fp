cats = [
    {"id": 1, "name": "Muffy", "age": 9},
    {"id": 2, "name": "Brian", "age": 8},
    {"id": 3, "name": "Arthur", "age": 10},
    {"id": 4, "name": "Buster", "age": 7}
]


def index(req):
    return [c for c in cats], 200


def create(req):
    new_cat = req.get_json()
    new_cat["id"] = sorted([c["id"] for c in cats])[-1] + 1
    cats.append(new_cat)
    return new_cat, 201
