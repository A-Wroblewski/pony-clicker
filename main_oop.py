import math
import tkinter as tk
from tkinter import messagebox

class PonyClicker:
    def __init__(self):
        self.window = tk.Tk()
        self.bits = 0

        self.hooves = 1
        self.hooves_cost = 10

        self.cider = 0
        self.cider_cost = 15
        self.cider_per_second = 0

        self.amulet = 0
        self.amulet_cost = 15
        self.amulet_per_second = 0


    def quit_game(self):
        confirmation = messagebox.askyesno(
            message='Tem certeza que deseja sair?\nTodo o progresso não salvo será perdido.',
            title='Sair do jogo')

        if confirmation: self.window.destroy()


    def create_ui(self):
        window = self.window
        bits = self.bits
        hooves = self.hooves
        hooves_cost = self.hooves_cost
        cider = self.cider
        cider_cost = self.cider_cost
        cider_per_second = self.cider_per_second
        amulet = self.amulet
        amulet_cost = self.amulet_cost
        amulet_per_second = self.amulet_per_second

        #################################################################################################################################
        #                                                  pegando todos os self acima                                                  #
        #################################################################################################################################

        window.title('Pony Clicker')

        window_icon = tk.PhotoImage(file='mlp_logo.png')
        window.iconphoto(True, window_icon)

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = 912
        window_height = 684

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        window.resizable(0, 0)

        window.rowconfigure([0, 1], weight=1)
        window.columnconfigure([0, 1, 2], weight=1)

        #################################################################################################################################
        #                                                 configurações da janela acima                                                 #
        #################################################################################################################################

        window.option_add('*tearOff', False)  # desliga a opção de destacar o menu em uma nova janela

        menu_bar = tk.Menu(window)
        window['menu'] = menu_bar

        options_menu = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=options_menu, label='Opções')
        options_menu.add_command(label='Salvar', command=...)

        menu_bar.add_command(label='Sair', command=self.quit_game)

        #################################################################################################################################
        #                                                 configurações dos menus acima                                                 #
        #################################################################################################################################

        def bits_image_click(*args):
            bits_label['text'] += hooves


        def bits_per_second_from_cider(*args):
            cider_per_second = 1
            bits_label['text'] += cider_per_second

            window.after(1000, bits_per_second_from_cider)


        def bits_per_second_from_amulet(*args):
            amulet_per_second = 2
            bits_label['text'] += amulet_per_second

            window.after(1000, bits_per_second_from_amulet)


        def buy_hooves(*args):
            nonlocal hooves, hooves_cost

            if bits_label['text'] >= hooves_cost:
                bits_label['text'] -= hooves_cost
                hooves += 1
                total_hooves_label['text'] = hooves

                hooves_cost = math.floor(hooves_cost * 1.5)
                hooves_cost_label['text'] = hooves_cost


        def buy_cider(*args):
            nonlocal cider, cider_cost, cider_per_second

            if bits_label['text'] >= cider_cost:
                bits_label['text'] -= cider_cost
                cider += 1
                total_cider_label['text'] = cider
                cider_per_second += 1
                cider_per_second_label['text'] = cider_per_second

                cider_cost = math.floor(cider_cost * 1.3)
                cider_cost_label['text'] = cider_cost

                window.after(1000, bits_per_second_from_cider)


        def buy_amulet(*args):
            nonlocal amulet, amulet_cost, amulet_per_second

            if bits_label['text'] >= amulet_cost:
                bits_label['text'] -= amulet_cost
                amulet += 1
                total_amulet_label['text'] = amulet
                amulet_per_second += 2
                amulet_per_second_label['text'] = amulet_per_second

                amulet_cost = math.floor(amulet_cost * 1.2)
                amulet_cost_label['text'] = amulet_cost

                window.after(1000, bits_per_second_from_amulet)

        #################################################################################################################################
        #                                                         funções acima                                                         #
        #################################################################################################################################

        bits_label = tk.Label(text=bits)
        bits_label.grid(row=0, column=1)

        bits_text = tk.Label(text='bits')
        bits_text.grid(row=0, column=2)

        #################################################################################################################################
        #                                                total de bits e seu campo acima                                                #
        #################################################################################################################################

        bits_image = tk.PhotoImage(file='ponies.png')
        bits_image = bits_image.subsample(15, 15)

        bits_image_button = tk.Button(image=bits_image, command=bits_image_click)
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
        hooves_buy_button = tk.Button(master=items_frame, text='Comprar', bg='yellow', activebackground='yellow', command=buy_hooves)
        hooves_buy_button.grid(row=0, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        hooves_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        hooves_cost_text.grid(row=0, column=2)

        # campo do custo do item
        hooves_cost_label = tk.Label(master=items_frame, text=hooves_cost, bg='pink')
        hooves_cost_label.grid(row=0, column=3, padx=5)

        # campo do texto do total comprado do item
        total_hooves_text = tk.Label(master=items_frame, text='Total de Cascos: ', bg='pink')
        total_hooves_text.grid(row=1, column=0, padx=5)

        # campo do total comprado do item
        total_hooves_label = tk.Label(master=items_frame, text=hooves, bg='pink')
        total_hooves_label.grid(row=1, column=1)

        #################################################################################################################################
        #                                               informações do item "Casco" acima                                               #
        #################################################################################################################################

        # campo do nome do item
        cider_text = tk.Label(master=items_frame, text='Sidra', bg='pink')
        cider_text.grid(row=2, column=0)

        # botão de compra do item
        cider_buy_button = tk.Button(master=items_frame, text='Comprar', bg='yellow', activebackground='yellow', command=buy_cider)
        cider_buy_button.grid(row=2, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        cider_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        cider_cost_text.grid(row=2, column=2)

        # campo do custo do item
        cider_cost_label = tk.Label(master=items_frame, text=cider_cost, bg='pink')
        cider_cost_label.grid(row=2, column=3, padx=5)

        # campo do texto do total comprado do item
        total_cider_text = tk.Label(master=items_frame, text='Total de Sidra: ', bg='pink')
        total_cider_text.grid(row=3, column=0, padx=5)

        # campo do total comprado do item
        total_cider_label = tk.Label(master=items_frame, text=cider, bg='pink')
        total_cider_label.grid(row=3, column=1)

        # campo do texto de bits por segundo ganhos pelo item
        cider_per_second_text = tk.Label(master=items_frame, text='Bits por segundo: ', bg='pink')
        cider_per_second_text.grid(row=4, column=0, padx=5)

        # campo da quantidade de bits por segundo ganhos pelo item
        cider_per_second_label = tk.Label(master=items_frame, text=cider_per_second, bg='pink')
        cider_per_second_label.grid(row=4, column=1)

        #################################################################################################################################
        #                                               informações do item "Sidra" acima                                               #
        #################################################################################################################################

        # campo do nome do item
        amulet_text = tk.Label(master=items_frame, text='Amuleto', bg='pink')
        amulet_text.grid(row=5, column=0)

        # botão de compra do item
        amulet_buy_button = tk.Button(master=items_frame, text='Comprar', bg='yellow', activebackground='yellow', command=buy_amulet)
        amulet_buy_button.grid(row=5, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        amulet_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        amulet_cost_text.grid(row=5, column=2)

        # campo do custo do item
        amulet_cost_label = tk.Label(master=items_frame, text=amulet_cost, bg='pink')
        amulet_cost_label.grid(row=5, column=3, padx=5)

        # campo do texto do total comprado do item
        total_amulet_text = tk.Label(master=items_frame, text='Total de Amuletos: ', bg='pink')
        total_amulet_text.grid(row=6, column=0, padx=5)

        # campo do total comprado do item
        total_amulet_label = tk.Label(master=items_frame, text=amulet, bg='pink')
        total_amulet_label.grid(row=6, column=1)

        # campo do texto de bits por segundo ganhos pelo item
        amulet_per_second_text = tk.Label(master=items_frame, text='Bits por segundo: ', bg='pink')
        amulet_per_second_text.grid(row=7, column=0, padx=5)

        # campo da quantidade de bits por segundo ganhos pelo item
        amulet_per_second_label = tk.Label(master=items_frame, text=amulet_per_second, bg='pink')
        amulet_per_second_label.grid(row=7, column=1)

        #################################################################################################################################
        #                                              informações do item "Amuleto" acima                                              #
        #################################################################################################################################

        upgrades_frame = tk.Frame(bg='pink', relief=tk.RIDGE, borderwidth=10)
        upgrades_frame.grid(row=0, column=3, sticky='nse', rowspan=2)

        #################################################################################################################################
        #                                                   frame das melhorias acima                                                   #
        #################################################################################################################################

        window.mainloop()


pony_clicker = PonyClicker()
pony_clicker.create_ui()
