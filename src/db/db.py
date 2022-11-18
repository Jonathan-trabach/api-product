import json

def load():
    with open('produtos.json') as json_product:
        return json.load(json_product)

def save(request):
    with open("produtos.json") as json_product:
        data = json.load(json_product)
        data_products = data["produtos"]
        print(request)
        data_products.append(request)

    with open("produtos.json", 'w') as json_product:
        json.dump(data, json_product, indent=4, separators=(",", ": "))

def save_object_listener(request):
    with open("../../produtos_listener.json") as json_product:
        data = json.load(json_product)
        data_products = data["produtos"]
        data_products.append(request)

    with open("../../produtos_listener.json", 'w') as json_product:
        json.dump(data, json_product, indent=4, separators=(",", ": "))