# main.py
import tkinter as tk
from ui.compare_table import ImageComparer

def main():
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle

    # Direkt olarak ImageComparer ekranını aç
    app = ImageComparer(root)
    app.open_compare_table_window()

    root.mainloop()

if __name__ == "__main__":
    main()
