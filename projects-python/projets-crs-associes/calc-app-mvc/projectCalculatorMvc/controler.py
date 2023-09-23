from model import model
from view import view

class controler:

    def __init__(self):
        self.model = model()
        self.view = view(self)
    
    def main(self):
        self.view.mainView()
        # print("in main of controller")
    
    def on_button_click(self, caption):
        # *print(f'button {caption} clicked')
        #* la methode calculate de la classe model renvoie le resultat a la methode on_button_click (f(x) de rappel) de la classe controler
        result = self.model.calculate(caption)
        
        #* pour afficher le result sur la view
        self.view.value_var.set(result)
    
if __name__ == '__main__':
    # print('Hello World')
    calculator = controler()
    calculator.main()