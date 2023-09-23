import tkinter as tk
from tkinter import ttk

class view(tk.Tk):
    '''
    classDocs
    '''
    #* il s'agit d'une variable de classe
    PAD = 10
    
    #* Une variable de classe, pour le nbre de boutton par linge
    MAX_BUTTONS_PER_ROW = 4
    
    #* creation d'une variable de classe, contenant les boutons du calculatrice
    #! En parcourant la liste, nous creons dynamiquement nos bouttons
    button_caption = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]
    
    def __init__(self, controler):
        '''
        constructor
        '''
        super().__init__()
        
        self.title('PyCalc1.0')
        
        self.controler = controler
        
        self.value_var = tk.StringVar()
        
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self.center_windows()
    
    def mainView(self):
        self.mainloop()
    
    #* le underscore du debut indique la methode n'est utilisable que dans la classe view.
    def _make_main_frame(self):
        #* le self. ici rend main_frm un attribut de la classe view (pour etre accessible dans _make_entry())
        self.main_frm = ttk.Frame(self)
        #* pack() defini un cadre avec un padding et x et y
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
    
    def _make_entry(self):
        #* pour ent, pas besoin de le rendre un attribut de la classe view (par ce que pas besoin de l'utiliser ailleurs)
        ent = ttk.Entry(self.main_frm, justify='right', textvariable=self.value_var, state='disabled')
        ent.pack(fill='x')
    
    def _make_buttons(self):
        #* ce cadre emballe nos boutons extérieurement
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        
        #* ce frm n'a pas besoin d'etre un attribue de classe, car les autres methodes n'ont pas besoin de lui. 
        #! Or lui a besoin de self.main_frm (son conteneur parent)
        frm = ttk.Frame(outer_frm)
        #* ce cadre emballe nos boutons
        frm.pack()
        
        #* pour avoir 4 boutton sur  la rangée
        buttons_in_row = 0
        
        for caption in self.button_caption:
        #* avant de créer le boutton et le cadre, verifier si la rangée a 4 bouttons
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                #* si oui, créer d'abord un nouveau cadre dans le cadre outer_frm
                frm = ttk.Frame(outer_frm)
                frm.pack()
                
                #* à chaque création d'un nouveau cadre, il faut...
                buttons_in_row = 0
                
            #* si non créer le boutton et son cadre
            btn = ttk.Button(
                #* l'option command prend une fonction lamda pour appeler on_button_click (function de rappel) du fichier controler.py
                #* ici on recupère le button créé, et on trasmet le button à on_button_click;
                #* ici caption, est un paramètre de la fonction on_button_click;
                
                frm, text=caption, command= 
                lambda button=caption: self.controler.on_button_click(button)
                )
            btn.pack(side='left')

            buttons_in_row += 1
    
    def center_windows(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )
    
    #! suite à partir de la vidéo 10 à 0:00
        