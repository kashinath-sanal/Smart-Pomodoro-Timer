def start_timer(app):
    if not app.is_running:
        if app.remaining_seconds == 0:
            app.remaining_seconds = (
                app.work_time.get() * 60 if app.is_work_session
                else app.break_time.get() * 60
            )
        app.is_running = True
        run_timer(app)


def run_timer(app):
    app.update_display()

    if app.is_running:
        if app.remaining_seconds > 0:
            app.remaining_seconds -= 1
            app.root.after(1000, run_timer, app)
        else:
            app.switch_session()


def pause_timer(app):
    app.is_running = False