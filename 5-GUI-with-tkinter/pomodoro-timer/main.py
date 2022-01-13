from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = '✔'
reps = 0
timer = None

# Timer reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_layout, text='00:00')
    label_timer['text'] = 'Timer'
    label_tick['text'] = ''
    global reps
    reps = 0

# Timer mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label_timer.config(text="LONG BREAK", fg=GREEN)
        countdown(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="BREAK", fg=GREEN)
    else:
        label_timer.config(text="WORK", fg=PINK)
        countdown(work_sec)


# Countdown mechanism
def countdown(count):
    count_min = int(math.floor(count/60))
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_layout, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += TICK
        label_tick['text'] = mark

# Interface
window = Tk()
window.title('P0M0D0R0 ')
window.config(padx=100, pady=50, bg=YELLOW)
# Labels
label_timer = Label(text='Timer', font=(FONT_NAME, 35, 'normal'), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)
label_tick = Label(text='', font=(FONT_NAME,15, 'bold'), bg=YELLOW, fg=GREEN, highlightthickness=0)
label_tick.grid(row=4, column=1)
# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_layout = canvas.create_text(100, 130, text='00:00',fill='white', font=(FONT_NAME, 40, 'bold'))
canvas.grid(row=1, column=1)
# Buttons
button_start = Button(text='Start', command=start_timer, font=(FONT_NAME, 15, 'normal'))
button_start.grid(row=3, column=0)
button_reset = Button(text='Reset',command=reset_timer, font=(FONT_NAME, 15, 'normal'), highlightthickness=0)
button_reset.grid(row=3, column=2)

window.mainloop()