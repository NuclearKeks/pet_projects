from tkinter import Button, Tk, Frame
from tkinter.ttk import Label
from time import sleep

window = Tk()
window.title("Typing practise")

window_width = 1200
window_height = 600
window.geometry(
    f"{window_width}x{window_height}+{int(window.winfo_screenwidth()/2-window_width/2)}+{int(window.winfo_screenheight()/2-window_height/2)-50}")
window.iconbitmap("typing_speed_test\keyboard.ico")

# keyboard
keyboard = Frame(window, bg="#aeafb0")
keyboard.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.3)
letters = ["`1234567890-=", "qwertyuiop[]",
           "asdfghjkl;'", "zxcvbnm,./"]
letters = [list(_) for _ in letters]


def clicked_button(event):
    temporary_label.config(text=f"Pressed {event.char} button")
    print(event)
    for button in buttons:
        if event.keycode == 32:
            space.config(relief="sunken",  bg="#e4e7ed")
            window.update()
            space.config(relief="raised", bg="#bfd9f2")
        if event.char == button.__getitem__("text") and event.keycode != 32:
            button.config(relief="sunken",  bg="#e4e7ed")
            # window.update_idletasks()
            window.update()
            sleep(1)
            button.config(relief="raised", bg="#bfd9f2")


# words
wordspace = Frame(window, bg="#dedab1")
wordspace.place(relwidth=0.7, relheight=0.2, relx=0.05, rely=0.05)

temporary_label = Label(
    wordspace, text="some text", font=("monsterrat 70 underline"), background="#dedab1")
temporary_label.pack()


buttons = []

for i, row in enumerate(letters):
    for j, button in enumerate(row):
        current_button = Button(
            keyboard, bg="#bfd9f2", text=letters[i][j], activebackground="#bfd9f2", relief="raised")
        buttons.append(current_button)
        current_button.bind(f"<Key>", clicked_button)
        current_button.place(relwidth=1/(len(letters[1])+3), relheight=1/(len(letters)+2),
                             relx=1/(len(letters[1])+3)*(j+1+i/5), rely=1/(len(letters)+2)*(i+1))
space = Button(keyboard, bg="#bfd9f2", text="<space>")
space.place(relwidth=2/5, relheight=1/(len(letters)+2),
            relx=1/4, rely=5/6)
# space.bind("<space>", clicked_button)

buttons.append(space)
# print(buttons[1].get)
# for button in buttons:
#     print(button.__getitem__("text"))
window.mainloop()
