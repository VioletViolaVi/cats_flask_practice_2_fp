from werkzeug import exceptions

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


def show(req, uid):
    return find_by_id(uid), 200


def update(req, uid):
    cat = find_by_id(uid)
    data = req.get_json()
    for key, val in data.items():
        cat[key] = val
    return cat, 200


def destroy(req, uid):
    cat = find_by_id(uid)
    cats.remove(cat)
    return cat, 204


def find_by_id(uid):
    try:
        matching_cats = []
        for c in cats:
            if c["id"] == uid:
                matching_cats.append(c)
        return matching_cats[0]
        # return next(c for c in cats if c["id"] == uid)
    except:
        raise exceptions.NotFound(f"We don't have a cat with that {uid} id!")
