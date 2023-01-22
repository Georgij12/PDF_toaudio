from tkinter import *
from tkinter import messagebox

import os,PyPDF2
from PyPDF2 import PdfReader
from gtts import gTTS

window= Tk()
window.minsize(height=200,width=500)
window.title("PDF converter to audio")


def insert():
    user_response = user_entry.get()

    pdfReader = PyPDF2.PdfReader(user_response)
    number_of_pages = len(pdfReader.pages)
    full_text = ""

    for page_number in range(0, number_of_pages):
        page = pdfReader.pages[page_number]
        text = page.extract_text()
        full_text += text

    language = "en"

    file_name = os.path.basename(user_response)
    new_file_name = os.path.splitext(file_name)

    test = gTTS(text=full_text, lang=language, slow=False)
    print(new_file_name[0])
    path=os.environ['desktop_destination_path']
    test.save(f"{path}{new_file_name[0]}.mp3")
    window.messagebox.showinfo(title="Sucess", message="uuuuuuuu")



welcome_label= Label(text= "Welcome to the audio converter:", font=("Times New Roman", 20))
welcome_label.grid(columnspan=2, row=0)

canvas= Canvas(height=150, width=150)
logo_img= PhotoImage(file="C:/Users/cen69342/Downloads/audio.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, columnspan=2)


label1= Label(text= "Please insert the path of the pdf file:", font=("Times New Roman", 15))
label1.grid(column=0, row=2)

user_entry= Entry(width=30)
user_entry.grid(column=1, row=2)

button= Button(text="Insert",font=("Times New Roman", 10),command=insert)
button.grid(column=2, row=2)







window.mainloop()