import math
import time
import threading
import tkinter as tk

g = 9.81


class Pendel:
    def __init__(self, pendel_name="noname", start_alpha=math.radians(0), length=100, masse=3):
        self.alpha = start_alpha
        self.time_since_start = 0
        self.masse = masse
        self.length = length
        self.sleep_time = 0.02
        self.post_init()
        self.my_thread = None
        self.pendel_name = pendel_name
        self.pendel_running = True
        self.root = tk.Tk()  # Tkinter root window
        self.root.title("Pendel Control")

        # Canvas for the pendulum
        self.canvas = tk.Canvas(self.root, width=1400, height=700)
        self.canvas.pack()
        self.pendulum_dot = self.canvas.create_oval(190, 190, 210, 210, fill="black")
        self.pendulum_line = self.canvas.create_line(600, 300, 200, 200, fill="black")

        # Button to stop the pendel
        stop_button = tk.Button(self.root, text="Stop Process", command=self.stop)
        stop_button.pack(pady=20)

        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.prestop)

        # Start the pendel thread
        self.thread_pendel()

        # Start the Tkinter event loop
        self.root.mainloop()

    def post_init(self):
        pass

    def pendel(self):
        self.do_sleep()
        while self.pendel_running:
            self.move_pendel()
            x = 600 + self.length * math.sin(self.alpha)
            y = 300 + self.length * math.cos(self.alpha)
            self.canvas.coords(self.pendulum_dot, x - 10, y - 10, x + 10, y + 10)
            self.canvas.coords(self.pendulum_line, 600, 300, x, y)
            self.do_sleep()

    def do_sleep(self):
        self.time_since_start += self.sleep_time
        time.sleep(self.sleep_time)

    def move_pendel(self):
        self.alpha += self.sleep_time
        pass

    def thread_pendel(self):
        self.my_thread = threading.Thread(target=self.pendel)
        self.my_thread.start()

    def prestop(self):
        self.root.after(0, self.stop)

    def stop(self):
        self.pendel_running = False
        self.root.destroy()  # Close the Tkinter window


class FederMasse:
    def __init__(self, pendel_name="noname", start_alpha=math.radians(0), length=100, masse=3):
        self.alpha = start_alpha
        self.time_since_start = 0
        self.masse = masse
        self.length = length
        self.sleep_time = 0.02
        self.post_init()
        self.my_thread = None
        self.pendel_name = pendel_name
        self.pendel_running = True
        self.root = tk.Tk()  # Tkinter root window
        self.root.title("Pendel Control")

        # Canvas for the pendulum
        self.canvas = tk.Canvas(self.root, width=1400, height=700)
        self.canvas.pack()
        self.pendulum_dot = self.canvas.create_oval(190, 190, 210, 210, fill="black")
        self.pendulum_line = self.canvas.create_line(600, 300, 200, 200, fill="black")

        # Button to stop the pendel
        stop_button = tk.Button(self.root, text="Stop Process", command=self.stop)
        stop_button.pack(pady=20)

        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.prestop)

        # Start the pendel thread
        self.thread_pendel()

        # Start the Tkinter event loop
        self.root.mainloop()

    def post_init(self):
        pass

    def pendel(self):
        self.do_sleep()
        while self.pendel_running:
            self.move_pendel()
            x = 600 + self.length * math.sin(self.alpha)
            y = 300 + self.length * math.cos(self.alpha)
            self.canvas.coords(self.pendulum_dot, x - 10, y - 10, x + 10, y + 10)
            self.canvas.coords(self.pendulum_line, 600, 300, x, y)
            self.do_sleep()

    def do_sleep(self):
        self.time_since_start += self.sleep_time
        time.sleep(self.sleep_time)

    def move_pendel(self):
        self.alpha += self.sleep_time
        pass

    def thread_pendel(self):
        self.my_thread = threading.Thread(target=self.pendel)
        self.my_thread.start()

    def prestop(self):
        self.root.after(0, self.stop)

    def stop(self):
        self.pendel_running = False
        self.root.destroy()  # Close the Tkinter window


class MathematischesPendel(Pendel):

    def post_init(self):
        self.start_alpha = self.alpha
        print(math.degrees(self.start_alpha))
        self.v_w_e = (g / self.length*100) ** 0.5
        self.A = self.start_alpha / math.sin(self.start_alpha)

    def move_pendel(self):
        self.alpha = self.A * math.sin(self.v_w_e * self.time_since_start + self.start_alpha)


# Create and run the Pendel instance
p = MathematischesPendel(length=300, start_alpha=math.radians(1), masse=20)
