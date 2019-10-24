def podajLiczby():
  loop=True
  while loop:
      global x #deklaracja zmiennej globalnej
      t = input("Wpisz 10 liczb oddzielonych spacjami: ").split() 
      t = [int(i) for i in t] #pętla pobierająca liczby
      x = [y for y in t if y > -1] #pętla wpisująca ciąg liczb do listy
      lenlist = len(t)
      if lenlist == 10:
        break
      else:
        print ("Wprowadziłeś za dużo lub za mało liczb! Podaj je ponownie")
        continue
  
def maxMin():
  min_value = min(x) #funkcja min - najmniejszy element listy
  print("Najmniejsza liczba to: ")
  print(min_value)
  max_value = max(x) #funkcja max - największy element listy
  print("Największa liczba to: ")
  print(max_value)
  
def sredniaLiczb():
  wynik = sum(x)/len(x) #sum - funkcja sumy, len - funkcja "ilości"
  print("Średnia z wprowadzonych liczb: ")
  print (wynik)

def sortowanieLiczb():  
  x.sort() #sort - sortuje rosnąco
  x.reverse() #odwrócenie ciągu rosnącego na malejący, szach mat
  print("Posortowane liczby (malejąco): ")
  print(x)


podajLiczby()
ans=True
while ans:
    print ("""
    1. Największa i najmniejsza wartość elementu
    2. Oblicz średnią z podanych lczb
    3. Posortuj liczby rosnąco
    4. Wyjdź z programu
    """)
    ans=input("Co chcesz zrobić? ") 
    if ans=="1": 
#wywołanie wszystkich czterech metod
      maxMin()
    elif ans=="2":
      sredniaLiczb()
    elif ans=="3":
      sortowanieLiczb()
    elif ans=="4":
      break
    elif ans !="":
      print("\n Wybierz pozycję z menu (1-2)")