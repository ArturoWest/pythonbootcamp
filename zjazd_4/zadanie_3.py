# program z graficznym interfajsem uzytkownika (GUI) do obliczania kosztow przejazdu na zadanym dystansie na podstawie spalania samochodu oraz ceny paliwa (skorzystaj z modulu tkinter)

import tkinter
def koszt_przejazdu():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    wynik.configure(text=(a*b*c)/100)

root = tkinter.Tk()

a_label = tkinter.Label(master=root, text="Dystans")
a_label.pack()

a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Spalanie")
b_label.pack()

b_entry = tkinter.Entry(master=root)
b_entry.pack()

c_label = tkinter.Label(master=root, text="Cena paliwa")
c_label.pack()

c_entry = tkinter.Entry(master=root)
c_entry.pack()

wynik_label = tkinter.Label(master=root, text="Koszt przejazdu")
wynik_label.pack()
wynik = tkinter.Label(master=root, text="-")
wynik.pack()

policz_button = tkinter.Button(master=root,text="Policz", command=koszt_przejazdu) # do przycisku jest przypisana fukcja sumuj
policz_button.pack()

root.title("Sumator")

root.mainloop()