from tkinter import *
import requests
def get_quote():
    quote = requests.get(url="https://api.kanye.rest/")
    canvas.itemconfig(quote_text, text=quote.json()["quote"])


window = Tk()
window.title("Kanye says... ")
window.config(padx=70, pady=70)

canvas = Canvas(width=500, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
