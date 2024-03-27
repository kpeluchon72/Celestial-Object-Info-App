import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.resizable(width=False, height=False)

# Create the info_frame outside of the confirm function
info_frame = tk.Frame(root, bg='gray', width=500, height=500)
info_frame.grid(row=1, rowspan=4, column=0, columnspan=3)
info_frame.grid_propagate(False)  # Prevents frame from resizing to fit contents


def confirm():
    # Clear existing labels
    for widget in info_frame.winfo_children():
        widget.destroy()

    # Create and place new labels
    label1 = tk.Label(info_frame, text="hi")
    label1.grid(row=0, column=0)

# Rest of your GUI setup
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

explain = tk.Label(root, text="Enter a Celestial Body")
entry = tk.Entry(root, width=50)
confirm_button = tk.Button(root, text="Confirm", command=confirm)

explain.grid(row=0, column=0, sticky=tk.N, pady=10)
entry.grid(row=0, column=1, sticky=tk.N, pady=10)
confirm_button.grid(row=0, column=2, sticky=tk.N, pady=10)

root.mainloop()
