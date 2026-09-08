def update_display(app):
    mins = app.remaining_seconds // 60
    secs = app.remaining_seconds % 60

    app.timer_label.config(text=f"{mins:02d}:{secs:02d}")

    if app.is_work_session:
        app.mode_label.config(text="WORK SESSION", fg="#d62828")
    else:
        app.mode_label.config(text="BREAK TIME", fg="#2a9d8f")

    task = app.task_name.get().strip()
    app.task_display.config(text=f"Task: {task}" if task else "No task selected")


def reset_timer(app):
    app.is_running = False
    app.is_work_session = True
    app.remaining_seconds = app.work_time.get() * 60
    app.completed_sessions = 0
    app.session_label.config(text="Sessions: 0")
    update_display(app)