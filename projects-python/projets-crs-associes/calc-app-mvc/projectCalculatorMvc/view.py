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
    #! En parcourant la liste, nous creons dynamiquemlbl nos bouttons
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
        
        #! config() = methode pour la mise en forme de la fenetre (represente par self ) 
        # changer la couleur du backgroud de la fenetre principale.
        self.config(bg="black")
        
        #! Pour configurer ntre objet de style (dans la methode _configure_button_style()), nous allons creer ce attribut...
        self._configure_button_style()
        
        self.controler = controler
        
        self.value_var = tk.StringVar()
        
        self._make_main_frame()
        
        # ! changer la methode _make_entry() (pour ttk) en _make_label (pour tk), car plus facile a formater (en tk)
        self._make_label()
        self._make_buttons()
        self.clbler_windows()
    
    #! Pour configurer les boutons, ns creons un objet de style (ie: usons ttq) car il y a plusieurs boutons.
    def _configure_button_style(self):
        style = ttk.Style()
        # Pour utiliser un theme pour my appli
        style.theme_use('alt')
        
        #! Pour afficher la liste des themes dispos dans mon 6stem 
        # print(style.theme_names())
        # ! Pour voir le theme use par my os
        # print(style.theme_use())
        
        # ! NB: STYLE vs THEME
        # THEME: change le style de all widgets (ie: un champ qui change toute la fenetre/appli)
        # STYLE: change le style individuellemet ( des boutons)
        
        # Style for operator buttons
        style.configure(
            'N.TButton', foreground='white', background='gray'
        )
        
        # Style for numbers buttons
        style.configure(
            'O.TButton', foreground='white', background='orange'
        )
        
        # stle for auther buttons 
        style.configure(
            'A.TButton', background='white'
        )
    
    def mainView(self):
        self.mainloop()
    
    #* le underscore du debut indique la methode n'est utilisable que dans la classe view.
    def _make_main_frame(self):
        #* le self. ici rend main_frm un attribut de la classe view (pour etre accessible dans _make_label())
        self.main_frm = ttk.Frame(self)
        #* pack() defini un cadre avec un padding et x et y
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
    
    def _make_label(self):
        # ! changer la variable enty en lbl
        #* pour lbl, pas besoin de le rendre en attribut dans la classe view (par ce que pas besoin de l'utiliser ailleurs). A la place, nous utilisons " textvariable ", pour garder une trace de la valeur ( de lbl)
        # * AUSSI: nous n'avons pas besoin d'utiliser l'objet label lui-meme, il sera quand meme cree et emballe dans la fenetre, mais nous n'avons pas besoin qu'il soit un attribut (= donnee utilisable partout: this.lbl) de la class
        # ! nous usons l'ancienne etiquette (tk), a la place de la nouvelle (ttk), car dans ce cas (only), nous formatons only cette seule etiquette (ie: pas risq de repetition d'options)
        lbl = tk.Label(self.main_frm, anchor='e', textvariable=self.value_var, bg='black', fg='white', font=('Arial', 30))
        lbl.pack(fill='x')
    
    def _make_buttons(self):
        #* ce cadre emballe nos boutons extérieuremlbl
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        
        
        #* ce frm n'a pas besoin d'etre un attribue de classe, car les autres methodes n'ont pas besoin de lui. 
        #! Or lui a besoin de self.main_frm (son conteneur parlbl)
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
                frm.pack(fill='x')
                
                #* à chaque création d'un nouveau cadre, il faut...
                buttons_in_row = 0
                
            if isinstance(caption, int):
                style_prefix = 'N'
            elif self._is_operator(caption):
                style_prefix = 'O'
            else:
                style_prefix = 'A'
            
            style_name = f'{style_prefix}.TButton'
                
            #* si non créer le boutton et son cadre
            btn = ttk.Button(
                #* l'option command prend une fonction lamda pour appeler on_button_click (function de rappel) du fichier controler.py
                #* ici on recupère le button créé, et on trasmet le button à on_button_click;
                #* ici caption, est un paramètre de la fonction on_button_click;
                
                frm, text=caption, command=( 
                lambda button=caption: self.controler.on_button_click(button)
                ),
                style=style_name
                )
            
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0
            
            btn.pack(fill=fill, expand=expand, side='left')

            buttons_in_row += 1
            
    def _is_operator(self, button_caption):
        return button_caption in ['/', '*', '+', '-', '=']
    
    def clbler_windows(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )
    
    #! suite à partir de la vidéo 13 à 0:00
        