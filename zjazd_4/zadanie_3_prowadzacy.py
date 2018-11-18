import tkinter
root = tkinter.Tk()

def policz_koszt_przejazdu():
    dystans = int(dystans_entry.get())
    spalanie = float(spalanie_entry.get())
    cena = float(cena_entry())

    koszt = (dystans / 100) * spalanie * cena
    wynik.configure(text=f'{koszt} PLN')

dystans_label = tkinter.Label(master=root, text="Dystans")
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Spalanie")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

cena_label = tkinter.Label(master=root, text="Cena")
cena_label.grid(row=2, column=0)
cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=2, column=1)

wynik_label = tkinter.Label(master=root, text = "Wynik")
wynik_label.grid(row=3, column=0)
wynik = tkinter.Label(master=root, text = " - ")
wynik.grid(row=3, column=1)

policz_button = tkinter.Button(master=root, text="Przelicz", command=policz_koszt_przejazdu)
policz_button.grid(row=4, column = 1)

root.title("Kalkulator spalania")
root.mainloop()