#pip install request to handle api request
#pip install Pillow to handle image

import tkinter as tk

root = tk.Tk()

h=700
w=800
#canvas
canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

#frame
frame=tk.Frame(root, bg='#80c1ff')
frame.place(relx=.1, rely=.1, relwidth=.8, relheight=.8)

# #button
# button=tk.Button(frame, text="hello", bg="gray")
# # button.pack(side='left', fill='x', expand=True)
# # button.grid(row=0, column=0)
# button.place(relx=0, rely=0, relwidth=0.25, relheight=.25)

# label = tk.Label(frame, text="this is a label", bg='yellow')
# # label.pack(side='right')
# # label.grid(row=1, column=1)
# label.place(relx=.3, rely=0, relwidth=.25, relheight=.25)

# entry = tk.Entry(frame, bg='green')
# # entry.pack(side='left')
# # entry.grid(row=2, column=2)
# entry.place(relx=.6, rely=0, relwidth=.25, relheight=.25)
root.mainloop()