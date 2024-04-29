# # import subprocess
# # command = "terminate by 5007"
# # correct_password = "mayank007511"
# # password = input("please enter password to terminate the code: ")
# # if password == correct_password:
# #     subprocess.run(['python', 'good_one.py'])
# # else:
# #     print("!!incorrect password!!\n")
# #
# # import getpass
# #
# # def protected_function():
# #     password = getpass.getpass("Enter password: ")
# #     if password == "mypassword":
# #
# #     else:
# #         print("Incorrect password.")
# #
# # def unprotected_function():
# #
# #
# #
# # while True:
# #     choice = input("Enter a choice (1 for protected function, 2 for unprotected function): ")
# #     if choice == "1":
# #         protected_function()
# #     elif choice == "2":
# #         unprotected_function()
# #     else:
# #         print("Invalid choice.")
# #



# import os

# # specify the path of the file to be deleted
# file_path = "K:\mayank\coding\Mayank's Python programming folder\mayank_python_projects\my_file.py"

# try:
#     # remove the file
#     os.remove(file_path)
#     print(f"{file_path} has been deleted successfully.")
# except FileNotFoundError:
#     print(f"{file_path} does not exist.")
# except PermissionError:
#     print(f"You do not have permission to delete {file_path}.")
# except Exception as e:
#     print(f"An error occurred while deleting {file_path}: {e}")

# import tkinter as tk
# from tkinter import filedialog

# def select_save_location():
#   """Opens a file save dialog and returns the selected directory."""
#   directory = filedialog.askdirectory()
#   return directory

# # Example usage (uncomment if you want to run the code)
# root = tk.Tk()
# root.withdraw()  # Hide the main window
# selected_directory = select_save_location()
# print(selected_directory)



import os
import tkinter as tk
from tkinter import messagebox

def list_files_in_window(directory):
  """Creates a Tkinter window and displays a list of files in a Listbox widget.

  Args:
      directory: The path to the directory containing the files.
  """

  window = tk.Tk()
  window.title("Files in " + directory)

  # Create a Listbox widget to display the file list
  file_list = tk.Listbox(window)
  file_list.pack(expand=True, fill="both")

  # Get the list of files
  try:
    all_files = os.listdir(directory)
    for filename in all_files:
      file_list.insert(tk.END, filename)
  except FileNotFoundError:
    messagebox.showerror("Error", "Directory not found!")
    window.destroy()  # Close the window on error
    return

  # No selection functionality here (as tkinter.filedialog is limited)
  # Inform the user about limitations
  messagebox.showinfo("Selection", "This window displays files, but you cannot select them here.\nUse the filenames for further processing.")

  window.mainloop()

# Example usage (replace with your directory path)
directory = "test"
list_files_in_window(directory)

from tkinter import filedialog

def select_save_location():
  """Opens a file save dialog and returns the selected directory."""
  directory = filedialog.askdirectory()
  return directory

# Example usage (uncomment if you want to run the code)
root = tk.Tk()
root.withdraw()  # Hide the main window
selected_directory = select_save_location()
print(selected_directory)