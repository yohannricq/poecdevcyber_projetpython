import json


def load():
    with open('src/config/config.json') as fichier:
        content = json.load(fichier)
        return content['mysql']


if __name__ == '__main__':
    print(load())
