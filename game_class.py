import math
import tkinter as tk

from tkinter import messagebox

from game_data import GameData


class PonyClicker:
    def __init__(self):
        self.window = tk.Tk()

        data = GameData.load()

        self.bits = data['bits']

        self.hooves = data['hooves']
        self.hooves_cost = data['hooves_cost']

        self.cider = data['cider']
        self.cider_cost = data['cider_cost']
        self.cider_per_second = data['cider_per_second']

        self.amulet = data['amulet']
        self.amulet_cost = data['amulet_cost']
        self.amulet_per_second = data['amulet_per_second']

    def _set_up_resolution(self, window):
        # pega a resolução do monitor
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # resolução que a janela vai ficar
        window_width = 912
        window_height = 684

        # conta malusquia pra deixar a janela centralizada na tela
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # monta a geometria centralizando a janela na tela
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def _set_up_icon(self, window):
        window_icon = tk.PhotoImage(file='assets\\images\\mlp_logo.png')
        window.iconphoto(True, window_icon)

    def _set_up_window(self):
        window = self.window

        window.title('Pony Clicker')

        self._set_up_resolution(window)
        self._set_up_icon(window)

        window.resizable(False, False)

        window.rowconfigure([0, 1], weight=1)
        window.columnconfigure([0, 1, 2], weight=1)

    def _set_up_menus(self):
        window = self.window

        # desliga a opção de destacar o menu em uma nova janela
        window.option_add('*tearOff', False)

        menu_bar = tk.Menu(window)
        window['menu'] = menu_bar

        options_menu = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=options_menu, label='Opções')
        options_menu.add_command(label='Salvar', command=self._save_game)
        options_menu.add_command(label='Resetar progresso', command=self._reset_game)

        menu_bar.add_command(label='Sair', command=self._quit_game)

    def _save_game(self):
        # cria uma cópia do __dict__ pra remover a chave "window" e salvar os dados
        data = self.__dict__.copy()
        data.pop('window')

        GameData.save(data)

    def _reset_game(self):
        confirmation = messagebox.askyesno(
            message='Tem certeza que deseja recomeçar do zero?\n' \
            'TODO o progresso será perdido.',
            title='Recomeçar jogo'
        )

        if confirmation:
            initial_values = GameData.initial_values()

            GameData.save(initial_values)

            self.window.destroy()
            restart = PonyClicker()
            restart.create_ui()

    def _quit_game(self):
        confirmation = messagebox.askyesno(
            message='Tem certeza que deseja sair?\n' \
            'Todo o progresso não salvo será perdido.',
            title='Sair do jogo')

        if confirmation: self.window.destroy()

    def create_ui(self):
        self._set_up_window()
        self._set_up_menus()

        def _bits_image_click(*args):
            bits_label['text'] += self.hooves
            self.bits += self.hooves

        def _buy_hooves(*args):
            if bits_label['text'] >= self.hooves_cost:
                bits_label['text'] -= self.hooves_cost
                self.bits -= self.hooves_cost

                self.hooves += 1
                total_hooves_label['text'] = self.hooves

                self.hooves_cost = math.floor(self.hooves_cost * 1.5)
                hooves_cost_label['text'] = self.hooves_cost

        def _bits_per_second_from_cider(*args):
            cider_per_second = 1

            bits_label['text'] += cider_per_second
            self.bits += cider_per_second

            self.window.after(1000, _bits_per_second_from_cider)

        def _buy_cider(*args):
            if bits_label['text'] >= self.cider_cost:
                bits_label['text'] -= self.cider_cost
                self.bits -= self.cider_cost

                self.cider += 1
                total_cider_label['text'] = self.cider

                self.cider_per_second += 1
                cider_per_second_label['text'] = self.cider_per_second

                self.cider_cost = math.floor(self.cider_cost * 1.2)
                cider_cost_label['text'] = self.cider_cost

                self.window.after(1000, _bits_per_second_from_cider)

        def _bits_per_second_from_amulet(*args):
            amulet_per_second = 2

            bits_label['text'] += amulet_per_second
            self.bits += amulet_per_second

            self.window.after(1000, _bits_per_second_from_amulet)

        def _buy_amulet(*args):
            if bits_label['text'] >= self.amulet_cost:
                bits_label['text'] -= self.amulet_cost
                self.bits -= self.amulet_cost

                self.amulet += 1
                total_amulet_label['text'] = self.amulet

                self.amulet_per_second += 2
                amulet_per_second_label['text'] = self.amulet_per_second

                self.amulet_cost = math.floor(self.amulet_cost * 1.3)
                amulet_cost_label['text'] = self.amulet_cost

                self.window.after(1000, _bits_per_second_from_amulet)

        #################################################################################################################################
        #                                                         funções acima                                                         #
        #################################################################################################################################

        bits_label = tk.Label(text=self.bits)
        bits_label.grid(row=0, column=1)

        bits_text = tk.Label(text='bits')
        bits_text.grid(row=0, column=2)

        #################################################################################################################################
        #                                                total de bits e seu campo acima                                                #
        #################################################################################################################################

        bits_image = tk.PhotoImage(file='assets\\images\\ponies.png')
        bits_image = bits_image.subsample(15, 15)

        bits_image_button = tk.Button(image=bits_image, command=_bits_image_click)
        bits_image_button.grid(row=1, column=1, columnspan=2)

        #################################################################################################################################
        #                                                     botão de pôneis acima                                                     #
        #################################################################################################################################

        items_frame = tk.Frame(bg='pink', relief=tk.RIDGE, borderwidth=10)
        items_frame.grid(row=0, column=0, sticky='nsw', rowspan=2)

        #################################################################################################################################
        #                                                     frame dos itens acima                                                     #
        #################################################################################################################################

        # campo do nome do item
        hooves_text = tk.Label(master=items_frame, text='Casco', bg='pink')
        hooves_text.grid(row=0, column=0)

        # botão de compra do item
        hooves_buy_button = tk.Button(master=items_frame,
                                      text='Comprar',
                                      bg='yellow',
                                      activebackground='yellow',
                                      command=_buy_hooves)

        hooves_buy_button.grid(row=0, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        hooves_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        hooves_cost_text.grid(row=0, column=2)

        # campo do custo do item
        hooves_cost_label = tk.Label(master=items_frame, text=self.hooves_cost, bg='pink')
        hooves_cost_label.grid(row=0, column=3, padx=5)

        # campo do texto do total comprado do item
        total_hooves_text = tk.Label(master=items_frame, text='Total de Cascos: ', bg='pink')
        total_hooves_text.grid(row=1, column=0, padx=5)

        # campo do total comprado do item
        total_hooves_label = tk.Label(master=items_frame, text=self.hooves, bg='pink')
        total_hooves_label.grid(row=1, column=1)

        #################################################################################################################################
        #                                               informações do item "Casco" acima                                               #
        #################################################################################################################################

        # campo do nome do item
        cider_text = tk.Label(master=items_frame, text='Sidra', bg='pink')
        cider_text.grid(row=2, column=0)

        # botão de compra do item
        cider_buy_button = tk.Button(master=items_frame,
                                     text='Comprar',
                                     bg='yellow',
                                     activebackground='yellow',
                                     command=_buy_cider)

        cider_buy_button.grid(row=2, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        cider_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        cider_cost_text.grid(row=2, column=2)

        # campo do custo do item
        cider_cost_label = tk.Label(master=items_frame, text=self.cider_cost, bg='pink')
        cider_cost_label.grid(row=2, column=3, padx=5)

        # campo do texto do total comprado do item
        total_cider_text = tk.Label(master=items_frame, text='Total de Sidra: ', bg='pink')
        total_cider_text.grid(row=3, column=0, padx=5)

        # campo do total comprado do item
        total_cider_label = tk.Label(master=items_frame, text=self.cider, bg='pink')
        total_cider_label.grid(row=3, column=1)

        # campo do texto de bits por segundo ganhos pelo item
        cider_per_second_text = tk.Label(master=items_frame, text='Bits por segundo: ', bg='pink')
        cider_per_second_text.grid(row=4, column=0, padx=5)

        # campo da quantidade de bits por segundo ganhos pelo item
        cider_per_second_label = tk.Label(master=items_frame, text=self.cider_per_second, bg='pink')
        cider_per_second_label.grid(row=4, column=1)

        #################################################################################################################################
        #                                               informações do item "Sidra" acima                                               #
        #################################################################################################################################

        # campo do nome do item
        amulet_text = tk.Label(master=items_frame, text='Amuleto', bg='pink')
        amulet_text.grid(row=5, column=0)

        # botão de compra do item
        amulet_buy_button = tk.Button(master=items_frame,
                                      text='Comprar',
                                      bg='yellow',
                                      activebackground='yellow',
                                      command=_buy_amulet)

        amulet_buy_button.grid(row=5, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        amulet_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        amulet_cost_text.grid(row=5, column=2)

        # campo do custo do item
        amulet_cost_label = tk.Label(master=items_frame, text=self.amulet_cost, bg='pink')
        amulet_cost_label.grid(row=5, column=3, padx=5)

        # campo do texto do total comprado do item
        total_amulet_text = tk.Label(master=items_frame, text='Total de Amuletos: ', bg='pink')
        total_amulet_text.grid(row=6, column=0, padx=5)

        # campo do total comprado do item
        total_amulet_label = tk.Label(master=items_frame, text=self.amulet, bg='pink')
        total_amulet_label.grid(row=6, column=1)

        # campo do texto de bits por segundo ganhos pelo item
        amulet_per_second_text = tk.Label(master=items_frame, text='Bits por segundo: ', bg='pink')
        amulet_per_second_text.grid(row=7, column=0, padx=5)

        # campo da quantidade de bits por segundo ganhos pelo item
        amulet_per_second_label = tk.Label(master=items_frame, text=self.amulet_per_second, bg='pink')
        amulet_per_second_label.grid(row=7, column=1)

        #################################################################################################################################
        #                                              informações do item "Amuleto" acima                                              #
        #################################################################################################################################

        upgrades_frame = tk.Frame(bg='pink', relief=tk.RIDGE, borderwidth=10)
        upgrades_frame.grid(row=0, column=3, sticky='nse', rowspan=2)

        #################################################################################################################################
        #                                                   frame das melhorias acima                                                   #
        #################################################################################################################################

        # vários for pra continuar contando os bits por segundo depois de reabrir o jogo
        for _ in range(self.cider):
            _bits_per_second_from_cider()

        for _ in range(self.amulet):
            _bits_per_second_from_amulet()

        self.window.mainloop()
