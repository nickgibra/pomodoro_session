import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
t = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checkmark
    global reps
    window.after_cancel(t)
    timer["text"] = "Timer"
    timer["fg"] = GREEN
    checkmark = ""
    canvas.itemconfig(timertext, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0 and reps % 8 != 0:
        timer["text"] = "Short Break"
        timer["fg"] = PINK
        countdown(SHORT_BREAK_MIN * 60)
    elif reps % 2 != 0:
        timer["text"] = "Work"
        timer["fg"] = GREEN
        countdown(WORK_MIN * 60)
    else:
        timer["text"] = "Long Break"
        timer["fg"] = RED
        countdown(LONG_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global checkmark
    global t
    countmin = math.floor(count/60)
    countsec = count % 60
    if countsec < 10:
        countsec = f"0{countsec}"
    if countmin < 10:
        countmin = f"0{countmin}"
    canvas.itemconfig(timertext, text=f"{countmin}:{countsec}")
    if count > 0:
        t = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 0:
            checkmark += "✔"
        elif reps % 8 == 0:
            checkmark = ""
        check["text"] = checkmark
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timertext = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
timer = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)
start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)
check = tkinter.Label(font=("Arial", 10, "bold"), bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)
window.mainloop()