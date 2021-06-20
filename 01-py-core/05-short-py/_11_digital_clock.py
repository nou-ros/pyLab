from tkinter import Tk, Label
import time

app_window = Tk()
app_window.title('Digital Watch')
app_window.geometry('520x180')
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#f3f720"
foreground = "#239f30"
border_width = 40

label = Label(app_window, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_watch():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(200, digital_watch)


# print(time.strftime("%H:%M:%S"))
digital_watch()
app_window.mainloop()
