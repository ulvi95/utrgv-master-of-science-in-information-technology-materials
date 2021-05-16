import tkinter as tk
from PIL import Image, ImageTk
import cv2
class MainWindow():
    def __init__(self, window):
        self.window = window
        self.window.geometry("700x700")
        self.window.minsize(700, 700)
        
        self.frame_image_mode_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_image_mode_button.grid(sticky="W", row=0, column=0, padx=0, pady=0)
        
        self.frame_video_mode_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_video_mode_button.grid(sticky="W", row=0, column=1, padx=0, pady=0)
        
        self.frame_turn_on_the_camera_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_turn_on_the_camera_button.grid(sticky="W", row=0, column=2, padx=0, pady=0)
        
        self.frame_turn_off_the_camera_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_turn_off_the_camera_button.grid(sticky="W", row=0, column=3, padx=0, pady=0)
        
        self.frame_process_the_image_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_process_the_image_button.grid(sticky="W", row=0, column=4, padx=0, pady=0)
        
        self.frame_upload_new_image_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_upload_new_image_button.grid(sticky="W", row=0, column=5, padx=0, pady=0)
        
        
        self.label_image_mode_button = tk.Button(master=self.frame_image_mode_button, text="Image Mode", relief=tk.RAISED, command = self.Image_mode_switcher)
        self.label_image_mode_button.pack(padx=0, pady=0)
        
        self.label_video_mode_button = tk.Button(master=self.frame_video_mode_button, text="Video Mode", relief=tk.RAISED, command = self.Video_mode_switcher)
        self.label_video_mode_button.pack(padx=0, pady=0)
        
        self.label_turn_on_the_camera_button = tk.Button(master=self.frame_turn_on_the_camera_button, text="Turn on the camera", relief=tk.RAISED, state=tk.DISABLED, command = self.Camera_turn_on)
        self.label_turn_on_the_camera_button.pack(padx=0, pady=0)
        
        self.label_turn_off_the_camera_button = tk.Button(master=self.frame_turn_off_the_camera_button, text="Turn off the camera", relief=tk.RAISED, state=tk.DISABLED, command = self.Camera_turn_off)
        self.label_turn_off_the_camera_button.pack(padx=0, pady=0)
        
        self.label_process_the_image_button = tk.Button(master=self.frame_process_the_image_button, text="Process the image", relief=tk.RAISED, state=tk.DISABLED)
        self.label_process_the_image_button.pack(padx=0, pady=0)
        
        self.label_upload_new_image_button = tk.Button(master=self.frame_upload_new_image_button, text="Upload new image", relief=tk.RAISED, state=tk.DISABLED)
        self.label_upload_new_image_button.pack(padx=0, pady=0)
        
    
    def Image_mode_switcher(self):
        self.label_process_the_image_button['state'] = tk.NORMAL
        self.label_upload_new_image_button['state'] = tk.NORMAL
        self.label_turn_on_the_camera_button['state'] = tk.DISABLED
        self.label_turn_off_the_camera_button['state'] = tk.DISABLED
        self.label_image_mode_button.configure(bg = "red", fg="white")
        self.label_video_mode_button.configure(fg = "black", bg="SystemButtonFace")
    
    def Video_mode_switcher(self):
        self.label_process_the_image_button['state'] = tk.DISABLED
        self.label_upload_new_image_button['state'] = tk.DISABLED
        self.label_turn_on_the_camera_button['state'] = tk.NORMAL
        self.label_turn_off_the_camera_button['state'] = tk.DISABLED
        self.label_video_mode_button.configure(bg = "red", fg="white")
        self.label_image_mode_button.configure(fg = "black", bg="SystemButtonFace")
    
    def Camera_turn_on(self):
        self.cap = cv2.VideoCapture(0)
        self.label_turn_on_the_camera_button['state'] = tk.DISABLED
        self.label_turn_off_the_camera_button['state'] = tk.NORMAL
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=self.width, height=self.height)
        self.update_image()
    
    def Camera_turn_off(self):
        self.label_turn_off_the_camera_button['state'] = tk.DISABLED
        self.label_turn_on_the_camera_button['state'] = tk.NORMAL
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=self.width, height=self.height)
        self.cap.release()
        cv2.destroyAllWindows()
        
    def update_image(self):
        if self.cap.isOpened() == True:
            self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
            self.image = Image.fromarray(self.image)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 250, anchor=tk.W, image=self.image)
            self.window.after(self.interval, self.update_image)
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()