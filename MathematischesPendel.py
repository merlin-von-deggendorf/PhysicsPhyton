import math
import threading
import time
import tkinter as tk
import Simulation


class MathematischesPendel:
    def __init__(self, r, max_alpha):
        max_alpha=math.radians(max_alpha)
        self.r = r
        self.max_alpha = max_alpha
        self.v_w_e = (9.81 / r) ** 0.5
        self.center_x = 500
        self.center_y = 50
        self.masse_radius = 30
        self.masse_y = self.center_y + self.r
        self.masse_x = self.center_x

    def paint_function(self, context, canvas, sleep_time, total_time):
        alpha = self.max_alpha * math.sin(self.v_w_e * total_time)

        translated_x = math.sin(alpha) * self.r
        translated_y = math.cos(alpha) * self.r
        self.masse_x = self.center_x + translated_x
        self.masse_y = self.center_y + translated_y
        canvas.coords(self.aufheange_punkt,
                      self.center_x, self.center_y,
                      self.masse_x, self.masse_y)
        canvas.coords(self.masse,
                      self.masse_x - self.masse_radius,
                      self.masse_y - self.masse_radius,
                      self.masse_x + self.masse_radius,
                      self.masse_y + self.masse_radius)

    def initialize_graphics(self, context, canvas):
        self.aufheange_punkt = \
            canvas.create_line(self.center_x, self.center_y,
                               self.masse_x, self.masse_y, width=5,
                               fill="red")
        self.masse = \
            canvas.create_oval(self.masse_x - self.masse_radius,
                               self.masse_y - self.masse_radius,
                               self.masse_x + self.masse_radius
                               , self.masse_y + self.masse_radius,
                               fill="Green")


g = MathematischesPendel(600, 30)

root = tk.Tk()
app = Simulation.TkinterApp(root, g, sim_speed=10, sleep_time=0.05)

# Start the Tkinter event loop
root.mainloop()
