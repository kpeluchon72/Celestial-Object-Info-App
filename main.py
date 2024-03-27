import tkinter as tk
import retrieve_data as rd


root = tk.Tk()
root.geometry("600x600")
root.resizable(width=False, height=False)
root.configure(bg="#404040")

info_frame = tk.Frame(root, bg='#C0C0C0', width=500, height=500)
info_frame.grid(row=1, rowspan=4, column=0, columnspan=3)
info_frame.grid_propagate(False)

for i in range(7):
    info_frame.rowconfigure(i, weight=1)

for j in range(2):
    info_frame.columnconfigure(j, weight=1)


def confirm():
    for widget in info_frame.winfo_children():
        widget.destroy()

    body_info = rd.ExtractData(rd.get_body_data(entry.get()))

    name = tk.Label(info_frame, text=body_info.english_name(), width=200, font=("Arial", 16, "bold"), bg="#E0E0E0")
    history_person = body_info.body_history()[0]
    history_date = body_info.body_history()[1]

    if not body_info.body_history()[0]:
        history_person = "NA"
    if not body_info.body_history()[1]:
        history_date = "NA"

    info = tk.Label(info_frame, text=f"Type: {body_info.body_type()}\n"
                                       f"Volume: {body_info.body_volume()['volValue']}^{body_info.body_volume()['volExponent']} Cubic Kilometers (km3)\n"
                                       f"Mass: {body_info.body_mass()['massValue']}^{body_info.body_mass()['massExponent']} Kilograms (kg)\n"
                                       f"Density: {body_info.body_density()} grams per cubic centimeters (g/cm3)\n"
                                       f"Gravity: {body_info.body_gravity()} meters per second squared (m/s2)\n"
                                       f"Average Temperature: {body_info.body_average_temperature()} Kelvin (K)\n"
                                       f"Sideral orbit in Earth Days: {(body_info.body_time_orbit())[0]}\n"
                                       f"Sideral Rotation in Hours: {(body_info.body_time_orbit())[1]}\n"
                                       f"Axial Tilt: {body_info.body_orbit()[0][0]}\n"
                                       f"Inclination: {body_info.body_orbit()[0][1]}°\n"
                                       f"Eccentricity: {body_info.body_orbit()[0][2]}\n"
                                       f"Orbit: {body_info.body_orbit()[1]}\n"
                                     f"Mean Radius: {body_info.body_radis()[0]} km\n"
                                     f"Equatorial Radius: {body_info.body_radis()[1]} km\n"
                                     f"Polar Radius: {body_info.body_radis()[2]} km\n"
                                     f"Perihelion: {body_info.body_perihelion_aphelion()[0]} km\n"
                                     f"Aphelion: {body_info.body_perihelion_aphelion()[1]} km\n"
                                     f"Discovered by: {history_person}\n"
                                     f"Discovered on: {history_date}",
                    width=100, padx=20, font=("Arial", 14), bg="#C0C0C0")

    name.grid(row=0, column=0, columnspan=2, sticky=tk.N)
    info.grid(row=1, column=0, rowspan=6, sticky=tk.NSEW)


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
