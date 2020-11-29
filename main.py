from tkinter import *
import math

# consts
RED = "#f05454"  # long break
GREEN = "#81b214"  # working
PURPLE = "#892cdc"  # short break
BLACK = "#191919"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
root_timer = None


# timer reset
def reset_timer():
    wd.after_cancel(root_timer)
    canvas.itemconfig(timer, text="00:00")
    heading.config(text="DinoPomo", fg=GREEN)
    tick_label.config(text="")


# timer start
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # red
        count_down(long_break_sec)
        heading.config(text="Break", fg=RED)

    if reps % 2 == 0:
        # purple
        count_down(short_break_sec)
        heading.config(text="Break", fg=PURPLE)

    else:
        count_down(work_sec)
        heading.config(text="Work", fg=GREEN)


# countdown
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    if count > 0:
        global root_timer
        root_timer = wd.after(1000, count_down, count - 1)
    else:
        start_timer()
        ticks = ""
        session = math.floor(reps / 2)
        for _ in range(session):
            ticks += "✔"
        tick_label.config(text=ticks)


# GUI setup
wd = Tk()
wd.title("DinoPomo")
wd.config(padx=100, pady=50, bg=BLACK)

canvas = Canvas(width=640, height=600, bg=BLACK, highlightthickness=0)
timer_img = PhotoImage(file="dino.png")
canvas.create_image(320, 300, image=timer_img)
timer = canvas.create_text(550, 200, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))

canvas.grid(column=1, row=1)
heading = Label(text="DinoPomo", fg=GREEN, bg=BLACK, font=(FONT_NAME, 30, "bold"))
heading.grid(column=1, row=0)

start_button = Button(text="START", bg=GREEN, fg=BLACK, activebackground=RED, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="RESET", bg=GREEN, fg=BLACK, activebackground=RED, command=reset_timer)
reset_button.grid(column=2, row=3)

tick_label = Label(text="", bg=BLACK, fg=GREEN, font=(FONT_NAME, 30, "bold"))
tick_label.grid(column=1, row=3)

wd.mainloop()
