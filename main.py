############################
#File: main.py
#Function: GUI for automatic key detector
#Author: Derek Wilson
#Date: 2025-05-17
############################

#NOTE: See References list in README.md

#Gui based on template from CustomTkinter github [5], updated with assistance from ChatGPT
import customtkinter
from tkinter import filedialog
import keydetect
import os
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x450")
app.title("Key & Tempo Detector")


def browse_and_analyze():
    filepath = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[("Audio files", "*.wav *.mp3"), ("All files", "*.*")]
    )
    if filepath:
        filename_var.set(os.path.basename(filepath))
        result_textbox.delete("0.0", "end")
        result_textbox.insert("end", "Analyzing file...\n")
        progress_bar.set(0.25)

        # Run analysis in a separate thread to keep UI responsive
        def analyze():
            try:
                progress_bar.set(0.5)
                key, sorted_keys, bpm_data = keydetect.find_data(filepath)
                bpm = round(float(bpm_data))
                progress_bar.set(0.75)

                result_textbox.delete("0.0", "end")
                result_textbox.insert("end", f"Detected Key: {key}\n")
                result_textbox.insert("end", f"Estimated Tempo: {bpm} BPM\n\n")
                result_textbox.insert("end", "Top Similar Keys:\n")
                for k, val in sorted_keys[:3]:
                    result_textbox.insert("end", f"{k:<10}: {val:.3f}\n")
            except Exception as e:
                result_textbox.delete("0.0", "end")
                result_textbox.insert("end", f"Error processing file:\n{e}")
            finally:
                progress_bar.set(1.0)

        threading.Thread(target=analyze, daemon=True).start()


# UI layout
frame = customtkinter.CTkFrame(master=app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title_label = customtkinter.CTkLabel(
    master=frame,
    text="Audio Key & Tempo Detector",
    font=customtkinter.CTkFont(size=20, weight="bold")
)
title_label.pack(pady=10)

subtitle_label = customtkinter.CTkLabel(
    master=frame,
    text="By Derek Wilson",
    font=customtkinter.CTkFont(size=15)
)
subtitle_label.pack(pady=15)

filename_var = customtkinter.StringVar()
filename_label = customtkinter.CTkLabel(master=frame, textvariable=filename_var, text_color="gray")
filename_label.pack(pady=2)

browse_button = customtkinter.CTkButton(
    master=frame,
    text="Browse Audio File (.wav/.mp3)",
    command=browse_and_analyze
)
browse_button.pack(pady=10)

# progress bar
progress_bar = customtkinter.CTkProgressBar(master=frame, width=500)
progress_bar.pack(pady=10)
progress_bar.set(0)

result_textbox = customtkinter.CTkTextbox(master=frame, height=200, width=500)
result_textbox.pack(pady=10, padx=10)
result_textbox.insert("0.0", "Select an audio file to analyze...\n")

app.mainloop()
