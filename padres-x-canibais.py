################################################
## Inteligencia artificial                    ##
## Alunos:Vitor Rolim                         ##
## Problema da travessia do rio               ##
################################################

# regras:
# 1-o numero de missionarios nao pode ser inferior ao numero de canibais, em qualquer uma das margens do rio.
# 2-o jogo acaba quando todos os personagens do jogo estiverem na outra margem do rio.

# x = Canibal.
# o = Missionario.

#solucao:
from Tkinter import *

arvore = {
          '0-xxxooo-dir' : ['x-xxooo-esq','o-xxxoo-esq','xx-xooo-esq','oo-xxxo-esq','xo-xxoo-esq'],
          'x-xxooo-esq'  : ['0-xxxooo-dir'],
          'x-xxooo-dir'  : ['xx-xooo-esq','xo-xxoo-esq','xxx-ooo-esq','xoo-xxo-esq','xxo-xoo-esq'],
          'o-xxxoo-esq'  : ['0-xxxooo-dir'],
          'o-xxxoo-dir'  : ['oo-xxxo-esq','xo-xxoo-esq','ooo-xxx-esq','xxo-xoo-esq','xoo-xxo-esq'],
          'xx-xooo-esq'  : ['0-xxxooo-dir','x-xxooo-dir'],
          'xx-xooo-dir'  : ['xxx-ooo-esq','xxo-xoo-esq','xxxo-oo-esq','xxoo-xo-esq'],
          'oo-xxxo-esq'  : ['0-xxxooo-dir','o-xxxoo-dir'],
          'oo-xxxo-dir'  : ['ooo-xxx-esq','xoo-xxo-esq','xxoo-xo-esq','xooo-xx-esq'],
          'xo-xxoo-esq'  : ['0-xxxooo-dir','x-xxooo-dir','o-xxxoo-dir'],
          'xo-xxoo-dir'  : ['xxo-xoo-esq','xoo-xxo-esq','xxxo-oo-esq','xooo-xx-esq','xxoo-xo-esq'],
          'xxx-ooo-esq'  : ['x-xxooo-dir','xx-xooo-dir'],
          'xxx-ooo-dir'  : ['xxxo-oo-esq','xxxoo-o-esq'],
          'ooo-xxx-esq'  : ['o-xxxoo-dir','oo-xxxo-dir'],
          'ooo-xxx-dir'  : ['xooo-xx-esq','xxooo-x-esq'],
          'xoo-xxo-esq'  : ['x-xxooo-dir','o-xxxoo-dir','xo-xxoo-dir','oo-xxxo-dir'],
          'xoo-xxo-dir'  : ['xxoo-xo-esq','xxxoo-o-esq','xxooo-x-esq'],
          'xxo-xoo-esq'  : ['x-xxooo-dir','o-xxxoo-dir','xx-xooo-dir','xo-xxoo-dir'],
          'xxo-xoo-dir'  : ['xxxo-oo-esq','xxoo-xo-esq','xxooo-x-esq','xxxoo-o-esq'],
          'xxxo-oo-esq'  : ['xx-xooo-dir','xo-xxoo-dir','xxx-ooo-dir','xxo-xoo-dir'],
          'xxxo-oo-dir'  : ['xxxoo-o-esq','xxxooo-0-esq'],
          'xxoo-xo-esq'  : ['xx-xooo-dir','oo-xxxo-dir','xo-xxoo-dir','xxo-xoo-dir','xoo-xxo-dir'],
          'xxoo-xo-dir'  : ['xxxoo-o-esq','xxooo-x-esq','xxxooo-0-esq'],
          'xooo-xx-esq'  : ['xo-xxoo-dir','oo-xxxo-dir','xoo-xxo-dir','ooo-xxx-dir'],
          'xooo-xx-dir'  : ['xxooo-x-esq','xxxooo-0-esq'],
          'xxxoo-o-esq'  : ['xxx-ooo-dir','xoo-xxo-dir','xxoo-xo-dir','xxxo-oo-dir'],
          'xxooo-x-esq'  : ['xxoo-xo-dir','xooo-xx-dir','ooo-xxx-dir','xxo-xoo-dir','xoo-xxo-dir'],
          'xxxooo-0-esq' : []
          }

class EstruturaDeFila:

    #inicializa o objeto fila.
    def __init__(self):
        self.fila = []

    #metodo de inserir elementos na fila.	
    def enfileira(self,elem):
        self.fila.append(elem)

    #metodo de remover elemento da fila.
    def desenfileira(self):
        elem = None
        try:
            elem = self.fila[0]
            if len(self.fila) == 1:
                self.fila = []
            else:
                self.fila = self.fila[1:]	
        except:
            pass
                    
        return elem

    #consulta se a fila esta vazia.
    def IsEmpty(self):
        resposta = False
        if len(self.fila) == 0:
            resposta = True
        return resposta

class TravessiaDoRio:

    #inicializacao do objeto self.est_fila, q instancia a classe EstruturaDeFila, trazendo todas as propriedades dela.
    def __init__(self):
        self.est_fila = EstruturaDeFila()

    #metodo de validacao das jogadas.
    def valida(self,caminho):
        ok=[]
        if caminho!=[]:
            for no in caminho:

                vazio_final=0
                canibal_dir=0
                missionario_dir=0
                vazio_inicial=0
                canibal_esq=0
                missionario_esq=0
                
                var_aux = no.split('-')
                esquerda = var_aux[0]
                direita = var_aux[1]
                
                for personagem in esquerda:
                    if personagem=='o':
                        missionario_esq+=1
                    if personagem=='x':
                        canibal_esq+=1
                    if personagem=='0':
                        vazio_inicial+=1

                for personagem in direita:   
                    if personagem=='o':
                        missionario_dir+=1
                    if personagem=='x':
                        canibal_dir+=1
                    if personagem=='0':
                        vazio_final+=1

                if missionario_dir!=0 and (canibal_dir>missionario_dir):
                    ok.append(0)

                elif missionario_esq!=0 and (canibal_esq>missionario_esq):
                    ok.append(0)

                elif missionario_dir==0 and (canibal_dir>missionario_dir):
                    ok.append(1)

                elif missionario_esq==0 and (canibal_esq>missionario_esq):
                    ok.append(1)
                
                elif (canibal_dir<=missionario_dir)and((canibal_esq<=missionario_esq)or(vazio_inicial==1)):
                    ok.append(1)

                elif (canibal_esq==missionario_esq)and(vazio_final==1):
                    ok.append(1)

            if ok.__contains__(0)==True:
                return False
            else:
                return True
                
        else:
            return False

    #metodo de busca em largura(extensao).
    def busca_largura(self,arvore,inicio,fim):
        travessia=TravessiaDoRio()
        
        aux = [inicio]
        self.est_fila.enfileira(aux)
        
        while self.est_fila.IsEmpty() == False:
            aux = self.est_fila.desenfileira()
            ultimo_no = aux[len(aux)-1]
            
            if ultimo_no == fim:
                if travessia.valida(aux)==True:
                    travessia.imprime(aux)        
                
            for no in arvore[ultimo_no]:
                if no not in aux:
                    var_aux = []
                    var_aux = aux + [no]
                    self.est_fila.enfileira(var_aux)

    #metodo de impressao.
    def imprime(self,lista):
        
        self.root = Tk()
        self.root.title("Travessia do rio")
        
        lista_aux=[]
        jogada=[]
        posicao=[]
        for elem in lista:
            aux=elem.split('-')
            var_aux=aux[0]+'-'+aux[1]
            jogada.append(var_aux)
            posicao.append(aux[2])
            lista_aux=zip(jogada,posicao)

            
        self.labelframe = LabelFrame(self.root,foreground="red",text="---------------------Jogada              Direção do barco-----------------",font=("Helvetica",12))
        self.labelframe.pack()
        
        for jog,pos in lista_aux:
            if pos=='esq':
                pos='Esquerda'
            elif pos=='dir':
                pos='Direita'
            var=jog+'                                  '+pos+'\n'
            if pos=="Esquerda":
                self.janela = Label(self.labelframe,background="green", text=var,relief=SUNKEN)
            elif pos=="Direita":
                self.janela = Label(self.labelframe,background="yellow", text=var,relief=SUNKEN)               
            self.janela.pack(fill=BOTH)

        self.button_2 = Button(self.root, text="Próximo resultado", fg="red",
                         command=self.root.destroy)
        self.button_2.pack(fill=BOTH)

        self.button = Button(self.root, text="Sair", fg="red",
                         command=quit)
        self.button.pack(fill=BOTH)
 
        self.root.mainloop()    



game=TravessiaDoRio()
game.busca_largura(arvore,'0-xxxooo-dir','xxxooo-0-esq')





























