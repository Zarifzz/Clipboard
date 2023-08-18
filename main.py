import customtkinter as ctk


window = ctk.CTk()

ctk.set_appearance_mode("dark")

window.title("ClipBoard")
window.geometry("1024x576")
window.resizable(False, False)

select_frame = ctk.CTkFrame(master=window, width=171 - 10, height=576 - 10)
select_frame.grid(row=0, column=0, padx=5, pady=5)

text_frame = ctk.CTkFrame(master=window, width=853 - 10, height=576 - 10)
text_frame.grid(row=0, column=1, padx=5, pady=5)




window.mainloop()

