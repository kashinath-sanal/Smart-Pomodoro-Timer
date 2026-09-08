import tkinter as tk

def build_ui(app):
    app.root.title("Smart Pomodoro Timer")
    app.root.geometry("450x550")
    app.root.resizable(False, False)
    app.root.configure(bg="#f4f6f8")

    # Title
    tk.Label(app.root, text="🍅 Smart Pomodoro Timer",
             font=("Arial", 20, "bold"),
             bg="#f4f6f8", fg="#d62828").pack(pady=15)

    # Settings Frame
    settings = tk.Frame(app.root, bg="white", bd=2, relief="groove")
    settings.pack(padx=20, pady=10, fill="x")

    tk.Label(settings, text="Work Time (min):", bg="white").grid(row=0, column=0, padx=10, pady=8)
    tk.Entry(settings, textvariable=app.work_time, width=8).grid(row=0, column=1)

    tk.Label(settings, text="Break Time (min):", bg="white").grid(row=1, column=0, padx=10, pady=8)
    tk.Entry(settings, textvariable=app.break_time, width=8).grid(row=1, column=1)

    # Task Input
    task_frame = tk.Frame(app.root, bg="white", bd=2, relief="groove")
    task_frame.pack(padx=20, pady=10, fill="x")

    tk.Label(task_frame, text="Task Name:", bg="white").pack(anchor="w", padx=10)
    tk.Entry(task_frame, textvariable=app.task_name).pack(fill="x", padx=10, pady=10)

    # Mode Label
    app.mode_label = tk.Label(app.root, text="WORK SESSION",
                              bg="#f4f6f8", fg="#d62828")
    app.mode_label.pack()

    # Timer Label
    app.timer_label = tk.Label(app.root, text="25:00",
                               font=("Arial", 42), bg="#f4f6f8")
    app.timer_label.pack(pady=10)

    # Task Display
    app.task_display = tk.Label(app.root, text="No task selected",
                                bg="#f4f6f8")
    app.task_display.pack()

    # Buttons
    btn_frame = tk.Frame(app.root, bg="#f4f6f8")
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="Start", command=app.start_timer).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Pause", command=app.pause_timer).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Reset", command=app.reset_timer).grid(row=0, column=2, padx=5)

    # Session Counter
    app.session_label = tk.Label(app.root, text="Sessions: 0", bg="#f4f6f8")
    app.session_label.pack()