import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class SchoolSistema:
    def __init__(self, master):
        self.master = master
        
        master.title('Sistema Aluno')
        master.geometry('400x400')
        master.config(bg="#2C3E50")
        
        self.criar_widgets()
        
    def criar_widgets(self):
        self.label_nome = tk.Label(self.master, text='Nome:', bg="#2C3E50", fg='white')
        self.label_nome.pack(pady=10)
        
        self.entry_nome = tk.Entry(self.master, width=30)
        self.entry_nome.pack()
        
        self.label_age = tk.Label(self.master, text='Idade:', bg="#2C3E50", fg='white')
        self.label_age.pack(pady=10)
        
        self.entry_age = tk.Entry(self.master, width=6)
        self.entry_age.pack()
        
        self.label_photo = tk.Label(self.master,  text='Escolhe a foto:', bg="#2C3E50", fg='white')
        self.label_photo.pack()
        
        self.btn_foto = tk.Button(self.master,  text='Escolher foto', bg="#3498DB" ,command=self.carregar_foto)
        self.btn_foto.pack(pady=10)
        
        self.btn_cadastro = tk.Button(self.master, bg="#2ECC71", text='Cadastrar', command=self.registro_estudante)
        self.btn_cadastro.pack()
        
        self.photo_path = None
        
    def carregar_foto(self):
        self.photo_path = filedialog.askopenfilename(filetypes=[('image files', '*.jpg* . png')])
        if (not self.photo_path):
            return
        messagebox.showinfo('Info', 'Foto carregada com sucesso!')
        
    def registro_estudante(self):
        nome = self.entry_nome.get()
        idade = self.entry_age.get()
        
        if (not nome or not idade or not self.photo_path):
            messagebox.showwarning('Info', 'Ops, Preencha todos os campos.')
            return
        
        
        self.studante_info(nome, idade)
        
    def studante_info(self, nome, idade):
        info_window = tk.Toplevel(self.master)
        info_window.title("Dados do Aluno")
        info_window.geometry("300x400")
        info_window.config(bg="#ECF0F1")

        label_info = tk.Label(info_window, text="Dados do Aluno", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 16))
        label_info.pack(pady=10)

        label_name = tk.Label(info_window, text=f"Nome: {nome}", bg="#ECF0F1", fg="#2C3E50")
        label_name.pack(pady=5)
        
        label_name = tk.Label(info_window, text=f"Idade: {idade}", bg="#ECF0F1", fg="#2C3E50")
        label_name.pack(pady=5)

        if self.photo_path:
            img = Image.open(self.photo_path)
            img = img.resize((150, 150), Image.LANCZOS)  # Usando LANCZOS para redimensionar
            self.photo = ImageTk.PhotoImage(img)
            label_photo = tk.Label(info_window, image=self.photo)
            label_photo.pack(pady=10)

        button_close = tk.Button(info_window, text="Fechar", command=info_window.destroy, bg="#E74C3C", fg="#FFFFFF")
        button_close.pack(pady=20)

        
        
    
if __name__ == '__main__':
    window = tk.Tk()
    app = SchoolSistema(window)
    window.mainloop()
            



