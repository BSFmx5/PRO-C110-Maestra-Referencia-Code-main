# importa el módulo time.
import time
  
# define la cuenta regresiva de la funcion timer.
def countdown_timer(seconds):
    
    while seconds > 0:       

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        seconds -= 1
      
    print('¡Se acabó el tiempo!')
  
  
# input tiempo en segundos.
seconds = input("Escribe el tiempo en numeros de segundos: ")
  
# Llama a la función
countdown_timer(int(seconds))
