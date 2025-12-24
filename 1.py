import tkinter as tk
from tkinter import messagebox
from aqi import calculate_aqi_for_all
#file name is 1.py

def submit():
    try:
        conc_values = {
            "PM2.5": float(entry_pm25.get()),
            "PM10": float(entry_pm10.get()),
            "CO": float(entry_co.get()),
            "SO2": float(entry_so2.get()),
            "NO2": float(entry_no2.get()),
            "O3": float(entry_o3.get())
        }
        aqi_results = calculate_aqi_for_all(conc_values)
        result_text = "\n".join([f"{k}: AQI = {v}" for k, v in aqi_results.items()])
        messagebox.showinfo("AQI Results", result_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")


# GUI Setup
root = tk.Tk()
root.title("Air Quality Index Calculator")
root.geometry("350x400")

tk.Label(root, text="Enter PM2.5 (μg/m³):").pack()
entry_pm25 = tk.Entry(root)
entry_pm25.pack()

tk.Label(root, text="Enter PM10 (μg/m³):").pack()
entry_pm10 = tk.Entry(root)
entry_pm10.pack()

tk.Label(root, text="Enter CO (mg/m³):").pack()
entry_co = tk.Entry(root)
entry_co.pack()

tk.Label(root, text="Enter SO2 (μg/m³):").pack()
entry_so2 = tk.Entry(root)
entry_so2.pack()

tk.Label(root, text="Enter NO2 (μg/m³):").pack()
entry_no2 = tk.Entry(root)
entry_no2.pack()

tk.Label(root, text="Enter O3 (μg/m³):").pack()
entry_o3 = tk.Entry(root)
entry_o3.pack()

submit_btn = tk.Button(root, text="Calculate AQI", command=submit)
submit_btn.pack(pady=20)

root.mainloop()