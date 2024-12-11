import os
import tkinter as tk
from tkinter import ttk, messagebox
import json

def run_file(filename):
    """Run the selected file."""
    full_path = os.path.join(filename + extension_dict.get(filename, ""))
    try:
        os.startfile(full_path)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to run '{filename}': {str(e)}")

def refresh_file_list():
    """Refresh the list of files in the Files directory."""
    file_list.delete(0, tk.END)
    global extension_dict
    extension_dict.clear()
    files_path = os.path.join('.')

    if not os.path.exists(files_path):
        messagebox.showerror("Error", f"The 'Files' folder does not exist in the current directory.")
        return

    allowed_extensions = {".py", ".bat"}

    for file in os.listdir(files_path):
        if os.path.isfile(os.path.join(files_path, file)):
            name, ext = os.path.splitext(file)
            if ext in allowed_extensions and name.lower() != "maingui":  # Exclude files named "guitest"
                extension_dict[name] = ext
                file_list.insert(tk.END, name)


# Create the main Tkinter window
root = tk.Tk()
root.title("3rd Person & 1st Person Dungeons Menu")
root.geometry("450x500")
root.resizable(False, False)
root.configure(background="#00274d")  # Dark blue background

# Style setup
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=5, relief="flat", borderwidth=0, background="#00274d", foreground="white")
style.configure("TLabel", font=("Arial", 14, "bold"), anchor="center", background="#00274d", foreground="white")
style.configure("TFrame", background="#00274d")
root.configure(background="#00274d")

# Frame for the listbox
frame = ttk.Frame(root, padding=10)
frame.pack(expand=True, fill="both")

# Label
label = ttk.Label(frame, text="Choose an Action")
label.pack(pady=(0, 10))
try:
    root.iconbitmap("icon.ico")  # Replace with your .ico file path
except Exception as e:
    print(f"Error setting icon: {e}")

# Listbox with centered text
file_list = tk.Listbox(frame, width=30, height=6, font=("Arial", 16), justify="center", borderwidth=5, highlightthickness=0, selectbackground="#4a90e2", relief="flat", background="#001f3f", foreground="white")
file_list.pack(pady=5, padx=10)

# Frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(fill="x", pady=10)

# Run button
# Style for the Run button with a larger size and outline
style.configure("Run.TButton", font=("Arial", 16, "bold"), padding=10, borderwidth=2, relief="raised", background="#001f3f", foreground="white")
style.map("Run.TButton", background=[("active", "#001f3f")])

# Run button with the new style
run_button = ttk.Button(button_frame, text="Run Selected Action", style="Run.TButton", command=lambda: run_file(file_list.get(tk.ACTIVE)))
run_button.pack(expand=True, pady=10, padx=20)

# Initialize extension dictionary
extension_dict = {}

# Initialize the file list
refresh_file_list()

class Settings:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.settings = {}
        self.load_settings()

    def load_settings(self):
        """Load settings from a JSON file."""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as file:
                self.settings = json.load(file)
        else:
            print("Settings file not found, using default settings.")
            self.settings = {
                'Sensitivity': 24,
            }
            self.save_settings()

    def save_settings(self):
        """Save settings to a JSON file."""
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        """Get a setting by key."""
        return self.settings.get(key, default)

    def set(self, key, value):
        """Set a setting."""
        self.settings[key] = value
        self.save_settings()

# Create settings instance
settings = Settings()

# Function to update sensitivity label from slider without saving
def update_sensitivity_label(value):
    sensitivity = round(float(value))  # Round to the nearest whole number
    sensitivity_label.config(text=f"Sensitivity: {sensitivity}")  # Update label with rounded value

# Function to save sensitivity when Apply is clicked
def save_sensitivity():
    sensitivity = round(float(sensitivity_slider.get()))
    settings.set('Sensitivity', sensitivity)
    messagebox.showinfo("Settings Saved", f"Sensitivity set to {sensitivity}")  # Optional: Show confirmation

# Frame for sensitivity slider
sensitivity_frame = ttk.Frame(root, padding=10)
sensitivity_frame.pack(fill="x", pady=10)

# Label for sensitivity
sensitivity_label = ttk.Label(sensitivity_frame, text=f"Sensitivity: {settings.get('Sensitivity')}", font=("Arial", 12), background="#00274d", foreground="white")
sensitivity_label.pack()

# Sensitivity slider (0-100)
sensitivity_slider = ttk.Scale(sensitivity_frame, from_=1, to=99, orient="horizontal", command=update_sensitivity_label, length=300)
sensitivity_slider.set(settings.get('Sensitivity'))  # Set the initial slider position
sensitivity_slider.pack(pady=10)

# Apply button under sensitivity slider
apply_button = ttk.Button(sensitivity_frame, text="Apply", style="apply.TButton", command=save_sensitivity)
apply_button.pack(pady=10)  # Adjust padding as needed

# Run the Tkinter event loop
root.mainloop()
