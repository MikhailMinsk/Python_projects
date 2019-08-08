from tkinter import *


class Ris(Frame):
    def __init__(self, rod):
        Frame.__init__(self, rod)
        self.rod = rod
        self.nabor()
        self.brush_size = 2
        self.brush_color = "black"

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color,
                              outline=self.brush_color)

    def change_color(self, new_color):
        self.brush_color = new_color

    def change_brush_size(self, new_size):
        self.brush_size = new_size

    def nabor(self):
        self.rod.title("Простенькая программка для рисования")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(7, weight=1)
        self.rowconfigure(3, weight=1)
        self.canv = Canvas(self, bg='white')
        self.canv.grid(row=3, column=0, columnspan=8, padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind('<B1-Motion>', self.draw)

        color_lab = Label(self, text="Цвет: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_kn = Button(self, text="Красный", width=10, bg='red', fg='white', command=lambda: self.change_color('red'))
        red_kn.grid(row=0, column=1)
        gr_kn = Button(self, text="Зеленый", width=10, bg='green', fg='white', command=lambda: self.change_color('green'))
        gr_kn.grid(row=0, column=2)
        bl_kn = Button(self, text="Синий", width=10, bg='blue', fg='white', command=lambda: self.change_color('blue'))
        bl_kn.grid(row=0, column=3)
        blk_kn = Button(self, text="Черный", width=10, bg='black', fg='white', command=lambda: self.change_color('black'))
        blk_kn.grid(row=0, column=4)
        wt_kn = Button(self, text="Белый", width=10, command=lambda: self.change_color('white'))
        wt_kn.grid(row=0, column=5)
        wt_kn = Button(self, text="Желтый", width=10, bg='yellow', command=lambda: self.change_color('yellow'))
        wt_kn.grid(row=0, column=6)

        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)

        one_bt = Button(self, text="Два", bg='light slate blue', fg='white', width=10, command=lambda: self.change_brush_size(2))
        one_bt.grid(row=1, column=1)
        two_bt = Button(self, text="Пять", bg='light slate blue', fg='white', width=10, command=lambda: self.change_brush_size(5))
        two_bt.grid(row=1, column=2)
        three_bt = Button(self, text="Семь", bg='light slate blue', fg='white', width=10, command=lambda: self.change_brush_size(7))
        three_bt.grid(row=1, column=3)
        four_bt = Button(self, text="Десять", bg='light slate blue', fg='white', width=10, command=lambda: self.change_brush_size(10))
        four_bt.grid(row=1, column=4)
        five_bt = Button(self, text="Двенадцать", bg='light slate blue', fg='white', width=10, command=lambda: self.change_brush_size(12))
        five_bt.grid(row=1, column=5)
        five_bt = Button(self, text="Пятнадцать", bg='light slate blue', fg='white', width=10, command=lambda: self.change_brush_size(15))
        five_bt.grid(row=1, column=6)

        clear_btn = Button(self, text='Очистить', bg='SeaGreen1', fg='white', width=10, command=lambda: self.canv.delete('all'))
        clear_btn.grid(row=2, column=1, sticky=W)


def main():
    its = Tk()
    its.geometry("1280x720+300+300")
    app = Ris(its)
    its.mainloop()


if __name__ == '__main__':
    main()
