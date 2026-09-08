import tkinter as tk

from ui import build_ui
from timer import start_timer, pause_timer
from session import switch_session
from display import update_display, reset_timer


class SmartPomodoroTimer:
    def __init__(self, root):
        self.root = root

        # Shared variables
        self.work_time = tk.IntVar(value=25)
        self.break_time = tk.IntVar(value=5)
        self.task_name = tk.StringVar()

        self.is_running = False
        self.is_work_session = True
        self.remaining_seconds = 0
        self.completed_sessions = 0

        # Build UI
        build_ui(self)

        # Initialize
        self.reset_timer()

    def start_timer(self):
        start_timer(self)

    def pause_timer(self):
        pause_timer(self)

    def switch_session(self):
        switch_session(self)

    def update_display(self):
        update_display(self)

    def reset_timer(self):
        reset_timer(self)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartPomodoroTimer(root)
    root.mainloop()