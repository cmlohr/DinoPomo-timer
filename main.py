from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
GREEN = "#9bdeac"
BLACK = "#191919"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20



# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# GUI setup
wd = Tk()
wd.title("DinoPomo")
wd.config(padx=100, pady=50, bg=BLACK)
canvas = Canvas(width=640, height=600, bg=BLACK, highlightthickness=0)
timer_img = PhotoImage(file="dino.png")
canvas.create_image(320, 300, image=timer_img)
canvas.create_text(550, 200, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


heading = Label(text="DinoPomo", fg=GREEN, bg=BLACK, font=(FONT_NAME, 30, "bold"))
heading.grid(column=1, row=0)

start_button = Button(text="START", bg=GREEN, fg=BLACK)
start_button.grid(column=0, row=3)

reset_button = Button(text="RESET", bg=GREEN, fg=BLACK)
reset_button.grid(column=2, row=3)

check = Label(text="✔", bg=BLACK, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check.grid(column=1, row=3)



wd.mainloop()

