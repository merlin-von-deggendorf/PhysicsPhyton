import math
import threading
import time
import tkinter as tk


class TkinterApp:
    def __init__(self, master, graphics, sim_speed=1, sleep_time=0.05):
        self.master = master
        self.sim_speed = sim_speed
        self.sleep_time = sleep_time
        self.is_loop = True
        master.title("Tkinter Application with Canvas and Controls")
        # Configure the main window to start maximized
        master.state('zoomed')
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        # Create a frame for the canvas
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a fixed-size canvas
        self.width = 1000
        self.height = 800
        self.canvas = tk.Canvas(self.canvas_frame, width=self.width, height=self.height, bg='white')
        self.canvas.pack(padx=10, pady=10)

        # Create a frame for the buttons and input fields
        self.control_frame = tk.Frame(master)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Add buttons
        self.button1 = tk.Button(self.control_frame, text="reset", command=self.reset_time)
        self.button1.pack(pady=5)

        # Add input fields
        self.input_field1 = tk.Entry(self.control_frame)
        self.input_field1.pack(pady=5)
        self.input_field1_button = tk.Button(self.control_frame, text="OK")
        self.input_field1_button.pack()

        self.input_field2 = tk.Entry(self.control_frame)
        self.input_field2.pack(pady=5)
        self.graphics = graphics
        self.start_time = None
        self.my_thread = threading.Thread(target=self.paint_loop)
        self.my_thread.start()

    def on_close(self):
        self.is_loop = False

    def real_close(self):
        print("Window closed!")  # Replace with your desired functionality

        self.master.quit()
        self.master.destroy()

    def reset_time(self):
        self.start_time = time.time()
        self.total_time = 0
        self.last_time = self.start_time
        pass

    def paint_loop(self):
        self.graphics.initialize_graphics(self, self.canvas)
        self.start_time = time.time()
        self.total_time = 0
        self.last_time = self.start_time
        while self.is_loop:
            stamp = time.time()
            self.total_time = stamp - self.start_time
            delta_time = stamp - self.last_time
            self.last_time = stamp
            self.graphics.paint_function(self, self.canvas, delta_time * self.sim_speed,
                                         self.total_time * self.sim_speed)
            time.sleep(self.sleep_time)

        self.master.after(0, self.real_close)


class Graphics:
    def __init__(self):
        self.circle = None

    def paint_function(self, context, canvas, sleep_time, total_time):
        pass

    def initialize_graphics(self, context, canvas):
        self.circle = canvas.create_oval(0, 0, 30, 30)

        pass
