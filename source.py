import tkinter as tk
from tkinter import filedialog, messagebox
import base64

def UploadAction():
    filename = filedialog.askopenfilename()

    if filename:
        with open(filename, 'r') as file:
            content = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)

def DecodeAction():
    encoded_text = text_widget.get(1.0, tk.END)
    try:
        decoded_text = base64.b64decode(encoded_text.encode()).decode()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, decoded_text)
    except Exception as e:
        print(f"Error decoding: {e}")
        messagebox.showerror('Python Error', f'Error decoding: {e}')

def EncodeAction():
    text_to_encode = text_widget.get(1.0, tk.END)
    try:
        encoded_text = base64.b64encode(text_to_encode.encode()).decode()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, encoded_text)
    except Exception as e:
        print(f"Error encoding: {e}")
        messagebox.showerror('Python Error', f"Error encoding: {e}")

def SaveAction():
    content_to_save = text_widget.get(1.0, tk.END)
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if filename:
        with open(filename, 'w') as file:
            file.write(content_to_save)

window = tk.Tk()
window.title("Encoder/Decoder")
window.geometry("340x250+100+100")
window.resizable(False, False)

button_open = tk.Button(window, text='Open', command=UploadAction)
button_open.pack()

text_widget = tk.Text(window, wrap="word", height=10, width=40)
text_widget.pack()

button_decode = tk.Button(window, text='Decode', command=DecodeAction)
button_decode.pack()

button_encode = tk.Button(window, text='Encode', command=EncodeAction)
button_encode.pack()

button_save = tk.Button(window, text='Save', command=SaveAction)
button_save.pack()

window.mainloop()
