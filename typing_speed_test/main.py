import tkinter
from turtle import bgcolor


window = tkinter.Tk()
window.title("Typing practise")
keyboard = tkinter.Frame(window, bg="#aeafb0")
keyboard.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.3)

window_width = 1200
window_height = 600
window.geometry(
    f"{window_width}x{window_height}+{int(window.winfo_screenwidth()/2-window_width/2)}+{int(window.winfo_screenheight()/2-window_height/2)-50}")
window.iconbitmap("typing_speed_test\keyboard.ico")

letters = ["`1234567890-=", "qwertyuiop[]",
           "asdfghjkl;'", "zxcvbnm,./"]
letters = [list(_) for _ in letters]

buttons = []

for i, row in enumerate(letters):
    for j, button in enumerate(row):
        current_button = tkinter.Button(
            keyboard, bg="#bfd9f2", text=letters[i][j])
        buttons.append(current_button)
        current_button.place(relwidth=1/(len(letters[1])+3), relheight=1/(len(letters)+2),
                             relx=1/(len(letters[1])+3)*(j+1+i/5), rely=1/(len(letters)+2)*(i+1))

window.mainloop()
