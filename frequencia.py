import pandas as pd
import unidecode
from tkinter import *




class presenca:
    def __init__(self, mestre) :
        self.mestre = mestre
        self.mestre.title('Presença')
        self.frameMestre = Frame(self.mestre)
        self.frameMestre.pack()
        self.frame1 = Frame(self.frameMestre)
        self.frame1['padx'] = 100   
        self.frame1['pady'] = 100
        self.frame1.pack()

        self.title = Label(self.frame1, text='Sistema de presença', justify='center', font='Arial 20 bold', bd=20 )
        self.title.pack()

        self.mes1 = Label(self.frame1, text='Digite o nome do arquivo do primeiro mês:', font='Arial 12 normal', bd=8)
        self.mes1.pack()
        self.mes1Input = Entry(self.frame1, width=40)
        self.mes1Input.pack()

        self.colunaMes1 = Label(self.frame1, text='Digite o nome da coluna que possui a frequência do primeiro mês:', font='Arial 12 normal', bd=8)
        self.colunaMes1.pack()
        self.colunaMes1Input = Entry(self.frame1, width=40)
        self.colunaMes1Input.pack()

        self.mes2 = Label(self.frame1, text='Digite o nome do arquivo do segundo mês:', font='Arial 12 normal', bd=8)
        self.mes2.pack()
        self.mes2Input = Entry(self.frame1, width=40)
        self.mes2Input.pack()

        self.colunaMes2 = Label(self.frame1, text='Digite o nome da coluna que possui a frequência do Segundo mês:', font='Arial 12 normal', bd=8)
        self.colunaMes2.pack()
        self.colunaMes2Input = Entry(self.frame1, width=40)
        self.colunaMes2Input.pack()

        self.button = Button(self.frame1, text='Criar arquivo', command=self.criar)
        self.button.pack()

        self.obs = Label(self.frame1, text='OBS: O arquivo deve estar no formato .xlsx ou .xls; \n \n Para mais informações sobre o sistema e um tutorial de como utilizar: \n Acesse o site: https://github.com/Adryan1928/Minha-frequencia', font='Arial 10 normal', bd=8, foreground='#ffcc00')
        self.obs.pack()

        msg = ''

        self.error = Label(self.frame1, text=msg)
        self.error.pack()
    def criar (self):
        try:
            lista = pd.read_excel(self.mes1Input.get())
            mes1= pd.DataFrame(lista)
            lista = pd.read_excel(self.mes2Input.get())
            mes2= pd.DataFrame(lista)
            lista = pd.read_excel("Lista do sistema.xlsx")
            presenca = pd.DataFrame(lista)
        except:
           self.error['foreground'] = 'red'
           self.error['text'] = 'O arquivo não foi encontrado'
           return
        
        try:
            mes1[self.colunaMes1Input.get()]
            mes2[self.colunaMes2Input.get()]
        except:
            self.error['foreground'] = 'red'
            self.error['text'] = 'A coluna não foi encontrada'
            return

        percentual_Mes1 = []
        def fmes1():
            for x in range (0,len(presenca)):
              for y in range(1,len(mes1["Aluno"])):
                if unidecode.unidecode(presenca["Aluno"][x]).upper().strip() == unidecode.unidecode(mes1["Aluno"][y]).upper().strip():
                    percentual_Mes1.append(mes1[self.colunaMes1Input.get()][y])
              if len(percentual_Mes1) < x+1:
                percentual_Mes1.append("Não está na lista")
            
            return percentual_Mes1

        percentual_Mes2 = []
        def fmes2():
            for x in range(0,len(presenca)):
              for y in range(1,len(mes2["Aluno"])):
                if unidecode.unidecode(presenca["Aluno"][x]).upper().strip() == unidecode.unidecode(mes2["Aluno"][y]).upper().strip():
                    percentual_Mes2.append(mes2[self.colunaMes2Input.get()][y])
              if len(percentual_Mes2)< x+1:
                    percentual_Mes2.append("Não está na lista")
            return percentual_Mes2

        presenca[f"Percentual de Presença do primeiro mês"] = fmes1()
        presenca[f"Percentual de Presença do segundo mês"] = fmes2()

        presenca.to_excel("Lista de presença atualizada.xlsx")

        self.error['foreground'] = 'green'
        self.error['text'] = 'Arquivo criado com sucesso'
        

raiz = Tk()
presenca(raiz)
raiz.mainloop()