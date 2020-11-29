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
can = Canvas(width=640, height=600, bg=BLACK, highlightthickness=0)
timer_img = PhotoImage(file="dino.png")
can.create_image(320, 300, image=timer_img)
can.create_text(550, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
can.pack()










wd.mainloop()

