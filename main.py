import math
import tkinter as tk

window = tk.Tk()

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
    global hooves
    global hooves_cost
    global hooves_cost_label

    if bits_label['text'] >= hooves_cost:
        bits_label['text'] -= hooves_cost
        hooves += 1
        total_hooves_label['text'] = hooves

        hooves_cost = math.floor(hooves_cost * 1.5)
        hooves_cost_label['text'] = math.floor(hooves_cost_label['text'] * 1.5)


def buy_cider(*args):
    global cider
    global cider_cost
    global cider_cost_label
    global cider_per_second
    global cider_per_second_label

    if bits_label['text'] >= cider_cost:
        bits_label['text'] -= cider_cost
        cider += 1
        total_cider_label['text'] = cider
        cider_per_second += 1
        cider_per_second_label['text'] = cider_per_second

        cider_cost = math.floor(cider_cost * 1.3)
        cider_cost_label['text'] = math.floor(cider_cost_label['text'] * 1.3)

        window.after(1000, bits_per_second_from_cider)


def buy_amulet(*args):
    global amulet
    global amulet_cost
    global amulet_cost_label
    global amulet_per_second
    global amulet_per_second_label

    if bits_label['text'] >= amulet_cost:
        bits_label['text'] -= amulet_cost
        amulet += 1
        total_amulet_label['text'] = amulet
        amulet_per_second += 2
        amulet_per_second_label['text'] = amulet_per_second

        amulet_cost = math.floor(amulet_cost * 1.2)
        amulet_cost_label['text'] = math.floor(amulet_cost_label['text'] * 1.2)

        window.after(1000, bits_per_second_from_amulet)


#################################################################################################################################
#                                                         funções acima                                                         #
#################################################################################################################################

bits = 0

bits_label = tk.Label(text=bits)
bits_label.grid(row=0, column=1)

bits_text = tk.Label(text='bits')
bits_text.grid(row=0, column=2)

#################################################################################################################################
#                                                total de bits e seu campo acima                                                #
#################################################################################################################################

bits_image = tk.PhotoImage(file='poneis.png')
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

hooves_cost = 10

# campo da palavra "custo"
hooves_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
hooves_cost_text.grid(row=0, column=2)

# campo do custo do item
hooves_cost_label = tk.Label(master=items_frame, text=hooves_cost, bg='pink')
hooves_cost_label.grid(row=0, column=3, padx=5)

hooves = 1

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

cider_cost = 15

# campo da palavra "custo"
cider_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
cider_cost_text.grid(row=2, column=2)

# campo do custo do item
cider_cost_label = tk.Label(master=items_frame, text=cider_cost, bg='pink')
cider_cost_label.grid(row=2, column=3, padx=5)

cider = 0

# campo do texto do total comprado do item
total_cider_text = tk.Label(master=items_frame, text='Total de Sidra: ', bg='pink')
total_cider_text.grid(row=3, column=0, padx=5)

# campo do total comprado do item
total_cider_label = tk.Label(master=items_frame, text=cider, bg='pink')
total_cider_label.grid(row=3, column=1)

cider_per_second = 0

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

amulet_cost = 15

# campo da palavra "custo"
amulet_cost_text = tk.Label(master=items_frame, text='Custo: ', bg='pink')
amulet_cost_text.grid(row=5, column=2)

# campo do custo do item
amulet_cost_label = tk.Label(master=items_frame, text=amulet_cost, bg='pink')
amulet_cost_label.grid(row=5, column=3, padx=5)

amulet = 0

# campo do texto do total comprado do item
total_amulet_text = tk.Label(master=items_frame, text='Total de Amuletos: ', bg='pink')
total_amulet_text.grid(row=6, column=0, padx=5)

# campo do total comprado do item
total_amulet_label = tk.Label(master=items_frame, text=amulet, bg='pink')
total_amulet_label.grid(row=6, column=1)

amulet_per_second = 0

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
