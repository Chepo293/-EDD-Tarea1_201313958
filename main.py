def Menu():
  i = 1
  lista = LSE()
  while i == 1:
    print("----MENU----")
    print("1. Insertar")
    print("2. Modificar")
    print("3. Listar")
    print("4. Eliminar")
    print("5. salir")
    op = int(input("Ingrese una opcion: "))
    if(op == 1):
      data = input("\ninserte el dato: ")
      lista.insertar(data)
    elif(op == 2):
      index = input("\ninserte el index a modificar: ")
      lista.modificar(index)
    elif(op == 3):
      lista.Listar()
    elif(op == 4):
      data = input("Ingrese el dato a eliminar: ")
      lista.eliminar(data)    
    elif(op == 5):
      print ("\nfeliz dia...")
      i = 0
    else:
      print("\n->ERROR:\n-->ingrese una opcion del 1 al 5\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class LSE:
    def __init__(self):
        self.inicio = None

    def Listar(self):
      if self.inicio is None:
          print("\nLa lista esta vacia...\n")
          return
      else:
          n = self.inicio
          print("\nLista Simplemente Enlazada")
          while n is not None:
              print(n.data , end = '')
              print(" ->", end = ' ')
              n = n.siguiente    
          print("NULL\n")    

    def insertar(self,data):
        actual = self.inicio
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.data > data:
                detenerse = True
            else:
                previo = actual
                actual = actual.siguiente
                print("Dato ingresado...\n")

        temp = Node(data)
        if previo == None:
            temp.siguiente = self.inicio
            self.inicio = temp
            print("Dato ingresado...\n")
        else:
            temp.siguiente = actual
            previo.siguiente = temp   
            print("Dato ingresado...\n")     

    def modificar(self, index):
      if self.inicio is None:
          print("\nLa lista esta vacia...\n")
          return
      else:
          n = self.inicio
          for i in range(int(index)+1):
            #print(i)
            if(n is None):
              print("-->Error\n->El index no existe\n")
              break;
            elif(i==(int(index))):
              data = input("Ingrese el nuevo dato: ")
              n.data = data
              print("Dato Modificado...\n")
            n = n.siguiente 

    def eliminar(self, dato):
      if self.inicio is None:
          print("\nLa lista esta vacia...\n")
          return
      else:
          n = self.inicio
          previo = None
          while n is not None:
              if(n.data == dato):
                if(n == self.inicio):
                  self.inicio = None
                else:
                  previo.siguiente = n.siguiente
                  n.siguiente = None
                print("Dato eliminado...\n")
                break
              previo = n  
              n = n.siguiente 
          if n is None:
            print("\nNo se encontro el dato...\n")    

Menu()
