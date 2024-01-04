import math
import threading
import time
import tkinter as tk
import Simulation


class FederMasseSystem2:
    def __init__(self, D, m, A):
        self.bottom = 600
        self.center = 400
        self.masse_width = 50
        self.masse_height = 50
        self.width = self.center * 2
        self.bottom_line = None
        self.center_line = None
        self.masse = None
        self.masse_center = self.center
        self.D = D
        self.m = m
        self.A = A
        self.v_w_e = (D / m) ** 0.5

    def paint_function(self, context, canvas, sleep_time, total_time):
        self.masse_center = self.center + self.A * math.sin(self.v_w_e * total_time)
        canvas.coords(self.masse, self.masse_center - self.masse_width / 2, self.bottom - self.masse_height,
                      self.masse_center + self.masse_width / 2, self.bottom)

    def initialize_graphics(self, context, canvas):
        # self.circle = canvas.create_oval(0, 0, 30, 30)
        self.bottom_line = canvas.create_rectangle(0, self.bottom, self.width, self.bottom + 40, fill="blue")
        self.center_line = canvas.create_rectangle(self.center - 1, 0, self.center + 1, self.bottom + 40, fill="red")
        self.masse = canvas.create_rectangle(self.center - self.masse_width / 2, self.bottom - self.masse_height,
                                             self.center + self.masse_width / 2, self.bottom,
                                             fill="green")


g = FederMasseSystem2(1, 1, 100)

root = tk.Tk()
app = Simulation.TkinterApp(root, g, sim_speed=1, sleep_time=0.05)

# Start the Tkinter event loop
root.mainloop()
