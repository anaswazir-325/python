# Trafic_light = input("Enter the light name: ").lower()
# boolean = "red , green, yellow"
# for light_time in Trafic_light
# if(Trafic_light == "red"):
#     print("stop")
# elif(Trafic_light == "green"):
#     print("Go")
# elif(Trafic_light == "yellow"):
#     print("Wait OR look")
# else:
#     print("Error!")





# Even and odd
# number = int(input("Enter the number: "))

# if number % 2 == 0:
#     print("Number: Even")
# else:
#     print("Number: Odd")





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













# import tkinter as tk

# root = tk.Tk()
# root.title("Anas wazir")

# convas = tk.Canvas(root, width=100, height=250, bg="black")
# convas.pack()
# # Umbrella
# umbrella = convas.create_arc(
#     10, 0, 90, 50,
#     start = 0,
#     extent = 180,
#     fill = "gray",
#     outline = "red",
#     width = 2
# )





# # creat light oval shap
# red = convas.create_oval(25, 10, 75, 60, fill="black")
# green = convas.create_oval(25, 150, 75, 200, fill="black")
# yellow = convas.create_oval(25, 80, 75, 130, fill="black")

# def cycle_light(state = "red"):
#     convas.itemconfig(red, fill="black")
#     convas.itemconfig(yellow, fill="black")
#     convas.itemconfig(green, fill="black")
#     if state == "red":
#         convas.itemconfig(red, fill="red")
#         root.after(3000, lambda: cycle_light("green"))
#     elif state == "green":
#         convas.itemconfig(green, fill="green")
#         root.after(6000, lambda: cycle_light("yellow"))
#     elif state  == "yellow":
        
#         convas.itemconfig(yellow, fill="yellow")
#         root.after(1500, lambda: cycle_light("red"))
        
# print(cycle_light())
# print(root.mainloop())
        
        
    
    
 