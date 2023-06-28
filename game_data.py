import json


class GameData:
    # quantidade de itens e preços iniciais do jogo
    @staticmethod
    def initial_values():
        return {
            'bits': 0,
            'hooves': 1,
            'hooves_cost': 10,
            'cider': 0,
            'cider_cost': 15,
            'cider_per_second': 0,
            'amulet': 0,
            'amulet_cost': 15,
            'amulet_per_second': 0,
        }

    # carrega os dados salvos
    @staticmethod
    def load():
        with open('game_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    # sobrescreve os dados tanto pra salvar o jogo quanto pra resetar
    @staticmethod
    def save(data):
        with open('game_data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
