from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
reps = 0
timer_counting = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global timer_counting
    reps = 0
    checks = ""
    window.after_cancel(timer_counting)
    canvas.itemconfig(timer_count, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text=checks)


# ---------------------------- Top window ------------------------------- #
def pop_up():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps == 0:
        continue_timer()


def continue_timer():
    global reps
    reps += 1
    # print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

    elif reps == 8:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
        pop_up()

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
        pop_up()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_min)) == 1:
        count_min = f"0{count_min}"
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_counting
        timer_counting = window.after(1000, count_down, round(count - 1))
    else:
        continue_timer()
        global reps
        checks = ""
        work_sessions = math.floor(reps / 2)
        print(work_sessions)
        for _ in range(work_sessions):
            checks += "✔"
        check_mark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer.grid(column=1, row=0)

start_button = Button(width=5, text="Start", command=start_timer)
start_button.grid(column=0, row=2)

rest_button = Button(width=5, text="Reset", command=reset_timer)
rest_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
