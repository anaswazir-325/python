import tkinter as tk

# Initialize the window
root = tk.Tk()
root.title("Anasa wazir")
canvas = tk.Canvas(root, width=100, height=250, bg="red")
canvas.pack()

# Create light shapes
red = canvas.create_oval(25, 10, 75, 60, fill="black")
yellow = canvas.create_oval(25, 80, 75, 130, fill="black")
green = canvas.create_oval(25, 150, 75, 200, fill="black")

def cycle_lights(state="red"):
    # Reset all lights
    canvas.itemconfig(red, fill="black")
    canvas.itemconfig(yellow, fill="black")
    canvas.itemconfig(green, fill="black")
    
    # Update based on state
    if state == "red":
        canvas.itemconfig(red, fill="red")
        root.after(3000, lambda: cycle_lights("green"))
    elif state == "green":
        canvas.itemconfig(green, fill="green")
        root.after(3000, lambda: cycle_lights("yellow"))
    elif state == "yellow":
        canvas.itemconfig(yellow, fill="yellow")
        root.after(1500, lambda: cycle_lights("red"))

# Start cycle
cycle_lights()
root.mainloop()