import math
import threading
import time
import tkinter as tk
import Simulation
import random


class MassenStoesse:

    def __init__(self):
        self.spheres = []
        self.ticker = 0
        self.physics_frequency = 10
        pass

    def initialize_graphics(self, context, canvas):

        for i in range(30):
            self.spheres.append(Sphere(canvas, context))

        canvas.create_rectangle(0, 0, context.width, context.height, width=5)
        print(context.width)
        print(context.height)
        pass

    def paint_function(self, context, canvas, sleep_time, total_time):
        for s in self.spheres:
            s.tick(canvas, sleep_time)
        self.ticker += 1
        self.ticker %= self.physics_frequency
        if self.ticker == 0:
            i = 0
            maxw = len(self.spheres) / 2
            while i < maxw:
                i2 = i + 1
                while i2 < len(self.spheres):
                    sphere1 = self.spheres[i]
                    sphere2 = self.spheres[i2]
                    sphere1.hit(sphere2)
                    i2 += 1
                i += 1


class Sphere:

    def __init__(self, canvas, context):
        quarter = math.pi / 2
        self.alpha1 = quarter
        self.alpha2 = quarter * 2
        self.alpha3 = quarter + 3

        self.maxwidth = context.width
        self.maxheight = context.height
        self.x = random.random() * self.maxwidth
        self.y = random.random() * self.maxheight
        self.r = 30
        self.alpha = random.random() * math.pi * 2
        self.oval = canvas.create_oval(self.x, self.y, self.x + self.r,
                                       self.y + self.r, fill=Sphere.get_random_color())
        self.direction = canvas.create_line(self.x, self.y,
                                            self.x + self.r * math.cos(self.alpha),
                                            self.y + self.r * math.sin(self.alpha))
        pass

    def tick(self, canvas, sleep_time):
        hypo = 100
        if self.alpha < 0:
            self.alpha = 0
        elif self.alpha > math.pi * 2:
            self.alpha = math.pi * 2

        if self.x + self.r >= self.maxwidth:
            if 0 <= self.alpha <= self.alpha1:
                self.alpha = self.alpha2 - self.alpha
            elif self.alpha >= self.alpha3:
                diff = math.pi * 2 - self.alpha
                self.alpha = self.alpha2 + diff
        elif self.x - self.r <= 0:
            if self.alpha1 <= self.alpha <= self.alpha2:
                diff = self.alpha - self.alpha1
                self.alpha = self.alpha1 - diff
            elif self.alpha2 <= self.alpha <= self.alpha3:
                diff = self.alpha - self.alpha2
                self.alpha = math.pi * 2 - diff
        if self.y - self.r <= 0:
            if self.alpha2 <= self.alpha <= self.alpha3:
                diff = self.alpha - self.alpha2
                self.alpha = self.alpha2 - diff
            elif self.alpha3 <= self.alpha:
                diff = self.alpha - self.alpha3
                self.alpha = self.alpha1 - diff
        elif self.y + self.r >= self.maxheight:
            if 0 <= self.alpha <= self.alpha1:
                self.alpha = math.pi * 2 - self.alpha
            elif self.alpha1 < self.alpha < self.alpha2:
                diff = self.alpha - self.alpha1
                self.alpha = self.alpha3 - diff

        self.x += sleep_time * math.cos(self.alpha) * hypo
        self.y += sleep_time * math.sin(self.alpha) * hypo

        canvas.coords(self.oval, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canvas.coords(self.direction, self.x, self.y, self.x + self.r * math.cos(self.alpha),
                      self.y + self.r * math.sin(self.alpha))

    def hit(self, sphere2):
        distance = ((self.x - sphere2.x) ** 2 + (self.y - sphere2.y) ** 2) ** 0.5
        mindistance = self.r + sphere2.r
        if distance < mindistance:
            # self.x = 0
            pass

    @staticmethod
    def get_random_color():
        """Generate a random color in hexadecimal format."""
        # Each color component (Red, Green, Blue) needs a random number between 0 and 255.
        # Format it into two hexadecimal digits.
        return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'


g = MassenStoesse()

root = tk.Tk()
app = Simulation.TkinterApp(root, g, sim_speed=1, sleep_time=0.05)

# Start the Tkinter event loop
root.mainloop()
