import math
import threading
import time
import tkinter as tk
import Simulation
import FederMasseSystem
import MathematischesPendel
import GedeampftesFederMasseSystem

g = GedeampftesFederMasseSystem.FederMasseSystemGedeampft(900, 1, 300, C=2)

root = tk.Tk()
app = Simulation.TkinterApp(root, g, sim_speed=0.5)

# Start the Tkinter event loop
root.mainloop()
