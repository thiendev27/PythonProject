import tkinter as tk
from tkinter import font

#TẠO, TỐI ƯU CỬA SỔ WINDOW
window = tk.Tk()
window.minsize(500,500)
window.resizable(width=False, height=False)
window.rowconfigure(0,weight = 1)
window.columnconfigure(0, weight=1)

#ĐỊNH NGHĨA MỘT VÀI BIẾN
font_list = list(font.families())
index = 0
current_font = font_list[index]
#CẬP NHẬT TIÊU ĐỀ CỦA WINDOW
window.title(f'Font Preview With {len(font_list)} Available Font (made by thiendev)')
#KHUNG HIỂN THỊ CHỮ
text_frame = tk.Frame(master=window,relief = tk.RIDGE, borderwidth=5)

font_text = tk.Label(master=text_frame,text = f'Current Font: {index + 1}. {current_font}')
font_text.config(font=(None,20))

preview = tk.Label(master=text_frame, text='Hello World!')
preview.config(font=(current_font,30))

preview_box = tk.Entry(master=text_frame)
preview_box.config(font=(current_font,20))

font_text.pack(pady=20)
preview.pack(pady=20)
preview_box.pack(pady=20)

text_frame.grid(row=0, column=0,sticky='nsew',padx=10, pady=10)

#CHỨC NĂNG CỦA NÚT
def update():
	global index, current_font, font_list
	current_font = font_list[index]
	font_text.config(text = f'Current Font: {index + 1}. {current_font}')
	font_text.config(font=(None,20))
	preview.config(font=(current_font,30))
	preview_box.config(font=(current_font,20))

def next_():
	global index
	if index < len(font_list)-1:
		index += 1
	else:
		index = 0
	update()
def prev():
	global index
	if index > 0:
		index -= 1
		
	else:
		index = len(font_list) - 1
	update()
def get_font():
	global index, font_list
	preview_box.delete(0, tk.END)
	preview_box.insert(tk.END, font_list[index])
#KHUNG HIỂN THỊ NÚT
btn_frame = tk.Frame(master=window,relief = tk.RIDGE, borderwidth=5)
next_btn = tk.Button(master=btn_frame,text='Next ->', command=next_)
prev_btn = tk.Button(master=btn_frame,text='<- Prev', command=prev)
get_font_btn = tk.Button(btn_frame,text='Get Font',command=get_font)

next_btn.grid(row=0, column=1)
prev_btn.grid(row=0, column=0)
get_font_btn.grid(row=0, column=2)

btn_frame.grid(row=1,column=0,sticky='nsew',padx=10, pady=10)
window.mainloop()
#MADE BY THIENDEV WITH <3