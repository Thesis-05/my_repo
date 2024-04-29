import tkinter as tk
import subprocess

def open_external_screen():
    # Create a new Tkinter window
    root = tk.Tk()
    
    # Set the window title
    root.title("External Screen")
    
    # Create a label widget
    label = tk.Label(root, text="This is the external screen!")
    label.pack(padx=200, pady=200)
    
    output_text = tk.Text(root, width=40, height=10)
    output_text.pack(padx=20, pady=10)
    
    #to run 1.my_file.py
    
    process = subprocess.Popen(['python', '1.my_file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    
    output_text.insert(tk.END, stdout.decode("utf-8"))
    output_text.insert(tk.END, stderr.decode("utf-8"))
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    open_external_screen()
