import customtkinter as ctk


window = ctk.CTk()

ctk.set_appearance_mode("dark")

window.title("ClipBoard")
window.geometry("1028x576")
# window.resizable(False, False)


select_frame = ctk.CTkFrame(master=window, width=171 - 10, height=576 - 10)
select_frame.grid(row=0, column=0, padx=5, pady=5)

text_frame = ctk.CTkFrame(master=window, width=853 - 10, height=576 - 10)
text_frame.grid(row=0, column=1, padx=5, pady=5)


textbox = ctk.CTkTextbox(master=text_frame, width=(853 - 10) -5, height=((576 - 10) - 50) - 10)
textbox.grid(row=0, column=0, padx=5, pady=5)

entry = ctk.CTkEntry(master=text_frame, placeholder_text="Enter Text", width=(853 - 10) -5, height=40, font=("Arial", 15))
entry.grid(row=1, column=0, padx=5, pady=5)


window.mainloop()

