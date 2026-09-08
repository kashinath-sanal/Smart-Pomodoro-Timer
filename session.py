from tkinter import messagebox

def switch_session(app):
    app.is_running = False

    if app.is_work_session:
        app.completed_sessions += 1
        app.session_label.config(text=f"Sessions: {app.completed_sessions}")

        messagebox.showinfo("Break Time", "Work session completed! Take a break.")

        app.is_work_session = False
        app.remaining_seconds = app.break_time.get() * 60

    else:
        messagebox.showinfo("Work Time", "Break over! Back to work.")

        app.is_work_session = True
        app.remaining_seconds = app.work_time.get() * 60

    app.start_timer()