from random import *
print("¡Jugemos!")
print("El juego será piedra, papel o tijera. ")
print("Jugaremos 3 rondas!!\n")
print("En cada ronda deberás seleccionar el número correspodiente: \n 1. Piedra \n 2. Papel \n 3. Tijera \n")
g=0
p=0
e=0
for i in range(1,4):
    print("|  RONDA",i)
    print("Listo?? Yo ya sé que elegir!")
    eb=randint(1,3)
    s=int(input("Ingresa tu selección:"))

    if s<=1 and s>=3:
        print("Lo siento, ingresaste un número no válido. (︶︹︶)")
    
    if eb==1:
        print("Yo elegí piedra")
    elif eb==2:
        print("Yo elegí papel")
    else:
        print("Yo elegí tijeras")
        
    if eb==s:
        print("Empatamos!")
        e+=1
    if (s==1 and eb==3) or (s==2 and eb==1) or (s==3 and eb==2):
        print("Me ganaste!!")
        g+=1
    if (s==1 and eb==2) or (s==2 and eb==3) or (s==3 and eb==1):
        print("Te gane!")
        p+=1
    print("\n")
    
print("Puntaje: \nGanaste:",g,"\nPerdiste:",p,"\nEmpates:",e)
if g==p or e==3:
    print("Hubo empate. (╭ರ╭ ͟ʖ╮•́)⊃")
elif g>p:
    print("Eres el ganador!! ᕙ(`▽´)ᕗ")
else:
    print("Perdiste... (҂◡_◡) ᕤ  Suerte a la proxima!")

print("Gracias por jugar!!")
print("⠀  ⠀   (\__/)")
print("       (•ㅅ•)      Código para ")
print("    ＿ノヽ ノ＼＿      taller Git")
print("`/　`/ ⌒Ｙ⌒ Ｙ  ヽ     CARTER & PARDO")
print("( 　(三ヽ人　 /　  |")
print("|　ﾉ⌒＼ ￣￣ヽ   ノ")
print("ヽ＿＿＿＞､＿_／")
print("    ｜( 王 ﾉ〈   (\__/)")
print("      /ﾐ`ー―彡\  (•ㅅ•)")