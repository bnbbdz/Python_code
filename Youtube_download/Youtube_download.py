from __future__ import unicode_literals
import youtube_dl
from tkinter.filedialog import askdirectory
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('CAPTAIN TEEMO ON DUTY')
root.iconbitmap('icon.ico')
root.geometry('1366x768')
canvas1 = tk.Canvas(root, width = 1366, height = 768)
canvas1.pack()

load_img = Image.open('bg6.jpg')
load_img_2 = ImageTk.PhotoImage(load_img)
img = tk.Label(root, image = load_img_2)
img.place(x=0,y=0)

lable1 = tk.Label(root, text = 'Copy link nhanh cái tay lên',bg = '#020820')
lable1.config(font=("MS Sans Serif",15,"bold"),fg='#37A3BF')
canvas1.create_window(400,320,window = lable1)

entry1 = tk.Entry (root)
canvas1.create_window(400, 370, window=entry1,width=500)

def input_file_location():
    global folder_selected
    folder_selected = askdirectory()
    text = tk.Label(text=folder_selected)
    text.place(x=250,y=70)

def download_link_youtube ():
	global x1
	x1 = entry1.get()
	ydl_opts = {'outtmpl': folder_selected+'/'+'%(title)s.%(ext)s'}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl :
		ydl.download([x1])
	kq = tk.Label(text="DOWNLOAD COMPLETE")
	kq.place(x=330,y=190) 

button1 = tk.Button (root, text='Chọn chỗ đẹp mà lưu',command=input_file_location, bg='#303030', font=('Arial', 11, 'bold'),fg = '#9EEAE8') 
canvas1.create_window(400, 270, window=button1)

button2 = tk.Button (root, text='Tải cái nhẹ', command=download_link_youtube, bg='#303030', font=('Arial', 11, 'bold'),fg = '#9EEAE8')
canvas1.create_window(400, 430, window=button2)

button3 = tk.Button (root, text='Thoát nhanh còn kịp', command=root.destroy, bg='#303030', font=('Arial', 11, 'bold'),fg = '#9EEAE8')
canvas1.create_window(400, 480, window=button3)
 
root.mainloop()