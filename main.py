import tkinter as tk # Python 3
import time
from PIL import Image

fileim = input("Path to Gif: ")
speed = input("Speed: ")
blcol = input("Color to delete (Recommended #666557): ")

im = Image.open(fileim)
frc = 0
try:
	while 1:
		im.seek(im.tell()+1)
		frc+=1
except EOFError:
	pass

root = tk.Tk()
root.image = tk.PhotoImage(file=fileim, format="gif -index 1")
frames = [tk.PhotoImage(file=fileim, format = "gif -index %i" %(i)) for i in range(frc)]

def update(ind):
	if ind == frc:
		ind = 0
	print(ind)
	frame = frames[ind]
	ind += 1
	label.configure(image=frame)
	root.after(speed, update, ind)

label = tk.Label(root, image=root.image, bg=blcol)
root.overrideredirect(True)
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", blcol)
label.pack()
root.after(0,update,1)
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('+{}+{}'.format(x, y))
label.mainloop()