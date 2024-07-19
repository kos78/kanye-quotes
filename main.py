from tkinter import *
import requests


def get_quote():
    quote = requests.get(url="https://api.kanye.rest/")
    canvas.itemconfig(quote_text, text=quote.json()["quote"])


window = Tk()
window.title("Kanye says... ")
window.config(padx=30, pady=20)

canvas = Canvas(width=250, height=314)
background_img = PhotoImage(file="background.png")
larger_background_img = background_img.zoom(2,2)
canvas.create_image(250, 150, image=larger_background_img)
quote_text = canvas.create_text(125, 150, text="Kanye Quote Goes HERE", width=240)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
