import os
import tkinter as tk
from tkinter import ttk, messagebox
import json

# Predefined list of files with names and extensions combined
files_data = [
    {"File": "Initial Setup.py"},
    {"File": "Inject.py"},
    {"File": "Setup Controller.py"},
    {"File": "Activate 3rd Person.py"},
    {"File": "Activate 1st Person.py"},
]

# Remove file extensions for display
for file in files_data:
    file["File"] = os.path.splitext(file["File"])[0]  # Strip file extension

# Folder where the files are located
MODULE_FOLDER = "module"

# Ensure the folder exists
if not os.path.exists(MODULE_FOLDER):
    os.makedirs(MODULE_FOLDER)

def run_file(filename):
    """Run the selected file from the 'module' folder."""
    full_path = os.path.join(MODULE_FOLDER, filename + ".py")  # Add extension when running
    if not os.path.exists(full_path):
        messagebox.showerror("Error", f"File '{filename}' not found in folder '{MODULE_FOLDER}'!")
        return
    try:
        os.startfile(full_path)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to run '{filename}': {str(e)}")

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
                'Sensitivity': 50,  # Default value
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

def update_sensitivity_label(value):
    """Update sensitivity label as slider value changes."""
    sensitivity = round(float(value))
    sensitivity_label.config(text=f"Sensitivity: {sensitivity}")  # Update label with rounded value

def save_sensitivity():
    """Save sensitivity setting."""
    sensitivity = round(float(sensitivity_slider.get()))
    settings.set('Sensitivity', sensitivity)
    messagebox.showinfo("Settings Saved", f"Sensitivity set to {sensitivity}")

# Create the main Tkinter window
root = tk.Tk()
root.title("3rd Person & 1st Person Dungeons Menu")
root.geometry("450x700")  # Increased height for the sensitivity slider
root.resizable(False, False)
root.configure(background="#00274d")  # Dark blue background

# Style setup
style = ttk.Style()
style.theme_use("clam")

# Configure styles
style.configure("TButton", font=("Arial", 12), padding=5, background="#00274d", foreground="white")
style.configure("TLabel", font=("Arial", 14, "bold"), anchor="center", background="#00274d", foreground="white")
style.configure("Treeview", background="#001f3f", foreground="white", rowheight=25, fieldbackground="#001f3f", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#00274d", foreground="white")
style.map("Treeview", background=[("selected", "#4a90e2")])

# Custom frame style
style.configure("Custom.TFrame", background="#00274d")

# Frame for the table
frame = ttk.Frame(root, padding=10, style="Custom.TFrame")
frame.pack(expand=True, fill="both")

# Label
label = ttk.Label(frame, text="Choose an Action", style="TLabel")
label.pack(pady=(0, 10))

# Treeview (table)
columns = ("File",)
file_table = ttk.Treeview(frame, columns=columns, show="headings", height=10)
file_table.pack(expand=True, fill="both", pady=10)

# Define column heading
file_table.heading("File", text="File")

# Adjust column width
file_table.column("File", width=350, anchor="center")

# Add files to the table
for file in files_data:
    file_table.insert("", "end", values=(file["File"],))

# Frame for buttons
button_frame = ttk.Frame(root, padding=10, style="Custom.TFrame")
button_frame.pack(fill="x")

# Run button
run_button = ttk.Button(
    button_frame,
    text="Run Selected Action",
    command=lambda: run_file(file_table.item(file_table.focus())["values"][0] if file_table.focus() else None)
)
run_button.pack(pady=10)

# Frame for sensitivity slider
sensitivity_frame = ttk.Frame(root, padding=10, style="Custom.TFrame")
sensitivity_frame.pack(fill="x", pady=20)

# Label for sensitivity
sensitivity_label = ttk.Label(sensitivity_frame, text=f"Sensitivity: {settings.get('Sensitivity')}", style="TLabel")
sensitivity_label.pack()

# Sensitivity slider (1-100)
sensitivity_slider = ttk.Scale(sensitivity_frame, from_=1, to=100, orient="horizontal", command=update_sensitivity_label, length=300)
sensitivity_slider.set(settings.get('Sensitivity'))  # Set initial slider value
sensitivity_slider.pack(pady=10)

# Apply button under sensitivity slider

# Create a style for the button text

# Apply the style to the button
# Apply button under sensitivity slider
apply_button = ttk.Button(sensitivity_frame, text="Apply", style="Run.TButton", command=save_sensitivity)
apply_button.pack(pady=10, padx=20)  # Adjust padding as needed


# Run the Tkinter event loop
root.mainloop()
