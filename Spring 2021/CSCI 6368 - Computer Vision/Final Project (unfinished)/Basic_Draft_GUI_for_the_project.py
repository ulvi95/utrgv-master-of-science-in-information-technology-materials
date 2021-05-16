import tkinter as tk


Menu_modes = ["Image Mode", "Video Mode", "Turn on the camera", "Turn off the camera", "Process the image", "Upload new image"]

window = tk.Tk(className=" CSCI6368 Project Basic-Draft GUI")

window.geometry("1000x500")
window.minsize(820, 370)

for i in range(len(Menu_modes)):
    
    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(sticky="W", row=0, column=i, padx=0, pady=0)

    label = tk.Button(master=frame, text=Menu_modes[i], relief=tk.RAISED)
    label.pack(padx=0, pady=0)

label1 = tk.Label(width=50, height=20, master=window, text="There should be either the video or the audio", bg="black", fg="white", justify=tk.LEFT)

label1.place(x=0, y=50)

label2 = tk.Label(width=50, height=5, master=window, text="There should be the result of detection", bg="blue", fg="white", justify=tk.LEFT)

label2.place(x=450, y=125)

window.mainloop()