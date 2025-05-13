import tkinter as tk
from time import strftime


my_window = tk.Tk()
my_window.title("Simple Clock")
my_window.geometry("600x500")
my_window.configure(bg='#0D1B2A')


header = tk.Frame(my_window, bg='#3E5C76', height=80)
header.pack(fill='x')


try:
    logo_photo = tk.PhotoImage(file="relogio 1.png")
    logo_label = tk.Label(header, image=logo_photo, bg='#3E5C76')
    logo_label.image = logo_photo  
    logo_label.pack(side='left', padx=20)
except Exception as e:
    print("Erro ao carregar a imagem:", e)


emoji_label = tk.Label(header, text="🕒 ⏱️ ⏰", font=('Arial', 20), bg='#3E5C76', fg='white')
emoji_label.pack(side='right', padx=20)

def time_clock():
    display_time = strftime('%H:%M:%S')
    label.config(text=display_time)
    label.after(1000, time_clock)

frame = tk.Frame(my_window, bg='black', bd=10)
frame.pack(pady=50)

label = tk.Label(
    frame,
    font=('Arial', 50, 'bold'),
    background='black',
    foreground='floralwhite',
    padx=20,
    pady=10
)
label.pack()


footer = tk.Frame(my_window, bg='#3E5C76')
footer.pack(side='bottom', fill='x', pady=20)

for text in [
    "@Adryel Guedes",
    "@Iago Leonam",
    "@Ryan José",
    "© 2025 Todos os direitos reservados."
]:
    tk.Label(
        footer,
        text=text,
        bg='#3E5C76',
        fg='white',
        font=('Arial', 10)
    ).pack(pady=2)


time_clock()
my_window.mainloop()
