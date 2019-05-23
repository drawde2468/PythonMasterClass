try:
    import tkinter
except:
    import Tkinter as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill='red')


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("960x540")

canvas = tkinter.Canvas(mainWindow, width=960 / 2, height=540)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=960 / 2, height=540, background="blue")
canvas2.grid(row=0, column=1)

print(repr(canvas), repr(canvas2))
draw_axes(canvas)
draw_axes(canvas2)

for x in range(-100, 101):
    y = parabola(x)
    plot(canvas, x, -y)

mainWindow.mainloop()
