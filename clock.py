import tkinter as tk
import time
import datetime
import pytz

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("200x100")
        
        self.time_label = tk.Label(self, text="", font=("Helvetica", 24))
        self.time_label.pack(expand=True)
        
        self.update_time()

    def update_time(self):
        current_time = datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.after(1000, self.update_time)

if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()
