import math
import tkinter as tk

class PonyClicker:
    def __init__(self):
        self.window = tk.Tk()

        self.bits = 0

        self.hooves = 1
        self.hooves_cost = 10

        self.cider = 0
        self.cider_cost = 10
        self.cider_per_second = 0

        self.amulet = 0
        self.amulet_cost = 10
        self.amulet_per_second = 0

        self.create_ui()


    def bits_image_click(self):
        self.bits_label['text'] += self.hooves


    def bits_per_second_from_cider(self):
        self.cider_per_second = 1
        self.bits_label['text'] += self.cider_per_second

        self.window.after(1000, self.bits_per_second_from_cider)


    def bits_per_second_from_amulet(self):
        self.amulet_per_second = 2
        self.bits_label['text'] += self.amulet_per_second

        self.window.after(1000, self.bits_per_second_from_amulet)


    def buy_hooves(self):
        if self.bits_label['text'] >= self.hooves_cost:
            self.bits_label['text'] -= self.hooves_cost
            self.hooves += 1
            self.total_hooves_label['text'] = self.hooves

            self.hooves_cost = math.floor(self.hooves_cost * 1.5)
            self.hooves_cost_label['text'] = math.floor(self.hooves_cost_label['text'] * 1.5)


    def buy_cider(self):
        if self.bits_label['text'] >= self.cider_cost:
            self.bits_label['text'] -= self.cider_cost
            self.cider += 1
            self.total_cider_label['text'] = self.cider
            self.cider_per_second += 1
            self.cider_per_second_label['text'] = self.cider_per_second

            self.cider_cost = math.floor(self.cider_cost * 1.3)
            self.cider_cost_label['text'] = math.floor(self.cider_cost_label['text'] * 1.3)

            self.window.after(1000, self.bits_per_second_from_cider)


    def buy_amulet(self):
        if self.bits_label['text'] >= self.amulet_cost:
            self.bits_label['text'] -= self.amulet_cost
            self.amulet += 1
            self.total_amulet_label['text'] = self.amulet
            self.amulet_per_second += 2
            self.amulet_per_second_label['text'] = self.amulet_per_second

            self.amulet_cost = math.floor(self.amulet_cost * 1.2)
            self.amulet_cost_label['text'] = math.floor(self.amulet_cost_label['text'] * 1.2)

            self.window.after(1000, self.bits_per_second_from_amulet)


    def create_ui(self):    
        self.window.title('Pony Clicker')

        window_icon = tk.PhotoImage(file='mlp_logo.png')
        self.window.iconphoto(True, window_icon)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = 912
        window_height = 684

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.window.resizable(0, 0)

        self.window.rowconfigure([0, 1], weight=1)
        self.window.columnconfigure([0, 1, 2], weight=1)

        #################################################################################################################################
        #                                                 configurações da janela acima                                                 #
        #################################################################################################################################

        self.bits_label = tk.Label(text=self.bits)
        self.bits_label.grid(row=0, column=1)

        bits_text = tk.Label(text='bits')
        bits_text.grid(row=0, column=2)

        #################################################################################################################################
        #                                                total de bits e seu campo acima                                                #
        #################################################################################################################################

        bits_image = tk.PhotoImage(file='poneis.png')
        bits_image = bits_image.subsample(15, 15)

        bits_image_button = tk.Button(image=bits_image, command=self.bits_image_click)
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
        hooves_buy_button = tk.Button(master=items_frame, text='Comprar', bg='yellow', activebackground='yellow', command=self.buy_hooves)
        hooves_buy_button.grid(row=0, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        hooves_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        hooves_cost_text.grid(row=0, column=2)

        # campo do custo do item
        self.hooves_cost_label = tk.Label(master=items_frame, text=self.hooves_cost, bg='pink')
        self.hooves_cost_label.grid(row=0, column=3, padx=5)

        # campo do texto do total comprado do item
        total_hooves_text = tk.Label(master=items_frame, text='Total de Cascos: ', bg='pink')
        total_hooves_text.grid(row=1, column=0, padx=5)

        # campo do total comprado do item
        self.total_hooves_label = tk.Label(master=items_frame, text=self.hooves, bg='pink')
        self.total_hooves_label.grid(row=1, column=1)

        #################################################################################################################################
        #                                               informações do item "Casco" acima                                               #
        #################################################################################################################################

        # campo do nome do item
        cider_text = tk.Label(master=items_frame, text='Sidra', bg='pink')
        cider_text.grid(row=2, column=0)

        # botão de compra do item
        cider_buy_button = tk.Button(master=items_frame, text='Comprar', bg='yellow', activebackground='yellow', command=self.buy_cider)
        cider_buy_button.grid(row=2, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        cider_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        cider_cost_text.grid(row=2, column=2)

        # campo do custo do item
        self.cider_cost_label = tk.Label(master=items_frame, text=self.cider_cost, bg='pink')
        self.cider_cost_label.grid(row=2, column=3, padx=5)

        # campo do texto do total comprado do item
        total_cider_text = tk.Label(master=items_frame, text='Total de Sidra: ', bg='pink')
        total_cider_text.grid(row=3, column=0, padx=5)

        # campo do total comprado do item
        self.total_cider_label = tk.Label(master=items_frame, text=self.cider, bg='pink')
        self.total_cider_label.grid(row=3, column=1)

        # campo do texto de bits por segundo ganhos pelo item
        cider_per_second_text = tk.Label(master=items_frame, text='Bits por segundo: ', bg='pink')
        cider_per_second_text.grid(row=4, column=0, padx=5)

        # campo da quantidade de bits por segundo ganhos pelo item
        self.cider_per_second_label = tk.Label(master=items_frame, text=self.cider_per_second, bg='pink')
        self.cider_per_second_label.grid(row=4, column=1)

        #################################################################################################################################
        #                                               informações do item "Sidra" acima                                               #
        #################################################################################################################################

        # campo do nome do item
        amulet_text = tk.Label(master=items_frame, text='Amuleto', bg='pink')
        amulet_text.grid(row=5, column=0)

        # botão de compra do item
        amulet_buy_button = tk.Button(master=items_frame, text='Comprar', bg='yellow', activebackground='yellow', command=self.buy_amulet)
        amulet_buy_button.grid(row=5, column=1, padx=10, pady=5)

        # campo da palavra "custo"
        amulet_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
        amulet_cost_text.grid(row=5, column=2)

        # campo do custo do item
        self.amulet_cost_label = tk.Label(master=items_frame, text=self.amulet_cost, bg='pink')
        self.amulet_cost_label.grid(row=5, column=3, padx=5)

        # campo do texto do total comprado do item
        total_amulet_text = tk.Label(master=items_frame, text='Total de Amuletos: ', bg='pink')
        total_amulet_text.grid(row=6, column=0, padx=5)

        # campo do total comprado do item
        self.total_amulet_label = tk.Label(master=items_frame, text=self.amulet, bg='pink')
        self.total_amulet_label.grid(row=6, column=1)

        # campo do texto de bits por segundo ganhos pelo item
        amulet_per_second_text = tk.Label(master=items_frame, text='Bits por segundo: ', bg='pink')
        amulet_per_second_text.grid(row=7, column=0, padx=5)

        # campo da quantidade de bits por segundo ganhos pelo item
        self.amulet_per_second_label = tk.Label(master=items_frame, text=self.amulet_per_second, bg='pink')
        self.amulet_per_second_label.grid(row=7, column=1)

        #################################################################################################################################
        #                                              informações do item "Amuleto" acima                                              #
        #################################################################################################################################

        upgrades_frame = tk.Frame(bg='pink', relief=tk.RIDGE, borderwidth=10)
        upgrades_frame.grid(row=0, column=3, sticky='nse', rowspan=2)

        #################################################################################################################################
        #                                                   frame das melhorias acima                                                   #
        #################################################################################################################################

        self.window.mainloop()


pony_clicker = PonyClicker()
