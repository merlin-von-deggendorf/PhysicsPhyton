import math
import threading
import time
import tkinter as tk
import Simulation


class FederMasseSystemGedeampft:
    def __init__(self, D, m, A, C):
        self.bottom = 600
        self.center = 400
        self.C = C
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
        self.roh = C / (2 * m)
        print(self.roh)
        self.v_w_e = ((D / m) - self.roh * self.roh) ** 0.5
        print(self.v_w_e)

    def paint_function(self, context, canvas, sleep_time, total_time):
        self.masse_center = self.center + self.A * ((math.e) ** (-total_time * self.C / (2 * self.m))) * math.sin(
            self.v_w_e * total_time)
        canvas.coords(self.masse, self.masse_center - self.masse_width / 2, self.bottom - self.masse_height,
                      self.masse_center + self.masse_width / 2, self.bottom)

    def initialize_graphics(self, context, canvas):
        # self.circle = canvas.create_oval(0, 0, 30, 30)
        self.bottom_line = canvas.create_rectangle(0, self.bottom, self.width, self.bottom + 40, fill="blue")
        self.center_line = canvas.create_rectangle(self.center - 1, 0, self.center + 1, self.bottom + 40, fill="red")
        self.masse = canvas.create_rectangle(self.center - self.masse_width / 2, self.bottom - self.masse_height,
                                             self.center + self.masse_width / 2, self.bottom,
                                             fill="green")
