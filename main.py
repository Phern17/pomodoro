from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(canvas_timer, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps = reps % 8 + 1

    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        check_label.config(text="")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global timer

    countdown_min = math.floor(count / 60)
    if countdown_min < 10:
        countdown_min = f"0{countdown_min}"
    countdown_sec = count % 60
    if countdown_sec < 10:
        countdown_sec = f"0{countdown_sec}"

    canvas.itemconfig(canvas_timer, text=f"{countdown_min}:{countdown_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas_timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, 'bold'), fill="white")
canvas.grid(column=1, row=1)

# calls action() when pressed
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(column=1, row=0)
check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
check_label.grid(column=1, row=3)

window.mainloop()
