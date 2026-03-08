import random
import json

# =========================
# VARIABLES DEL JUGADOR
# =========================

vida = 100
hambre = 0
armadura = 0

arma = "puños"
daño = 5
municion = 0

nivel = 1
exp = 0
monedas = 0

inventario = []

refugio = False

posicion = 0
exploraciones = 0

tiempo = "día"
clima = "despejado"

mutaciones = []

# =========================
# MAPA
# =========================

mapa = [
"ruinas",
"bosque oscuro",
"pueblo abandonado",
"mina profunda",
"carretera destruida",
"hospital infectado",
"base militar",
"metro abandonado",
"ciudad infectada",
"laboratorio secreto"
]

# =========================
# NPC
# =========================

npc_mapa = {

"ruinas":"sobreviviente",
"bosque oscuro":"leñador",
"pueblo abandonado":"vagabundo",
"mina profunda":"minero",
"carretera destruida":"mercader",
"hospital infectado":"doctor",
"base militar":"soldado",
"metro abandonado":"ingeniero",
"ciudad infectada":"cientifico",
"laboratorio secreto":"IA"

}

# =========================
# ENEMIGOS
# =========================

enemigos = [

"zombie",
"mutante",
"bestia",
"saqueador",
"creeper mutado",
"perro infectado",
"cultista",
"robot antiguo"

]

# =========================
# ARMAS
# =========================

armas = {

"pistola":{"daño":10},
"rifle":{"daño":15},
"katana":{"daño":20},
"pico de diamante":{"daño":25}

}

# =========================
# EQUIPAR ARMA
# =========================

def equipar_arma(nombre):

    global arma, daño

    arma = nombre
    daño = armas[nombre]["daño"]

    print("⚔ arma equipada:",arma)
    print("💥 daño:",daño)

# =========================
# MUTACIONES
# =========================

def obtener_mutacion():

    global armadura, daño, vida

    lista = [
    "piel de hierro",
    "garras mutantes",
    "regeneracion",
    "vision nocturna",
    "fuerza brutal"
    ]

    m = random.choice(lista)

    if m not in mutaciones:

        mutaciones.append(m)

        print("🧬 MUTACIÓN DESPERTADA:",m)

        if m == "piel de hierro":
            armadura += 5

        if m == "garras mutantes":
            daño += 5

        if m == "regeneracion":
            vida += 20

# =========================
# CLIMA
# =========================

def cambiar_clima():

    global clima

    clima = random.choice([
    "despejado",
    "lluvia",
    "tormenta",
    "niebla"
    ])

# =========================
# COFRES
# =========================

def cofre():

    loot = random.choice([
    "comida",
    "botiquin",
    "diamante",
    "pistola",
    "rifle",
    "katana",
    "pico de diamante",
    "nada"
    ])

    if loot == "nada":

        print("📦 cofre vacío")

    elif loot in armas:

        print("⚔ encontraste arma:",loot)
        equipar_arma(loot)

    else:

        inventario.append(loot)
        print("📦 obtienes:",loot)

# =========================
# MINI BOSS
# =========================

def mini_boss():

    global vida, monedas

    boss = random.choice([
    "ogro mutante",
    "robot militar",
    "bestia alfa"
    ])

    boss_vida = 120

    print("\n👹 MINI BOSS:",boss)

    while boss_vida > 0 and vida > 0:

        boss_vida -= daño

        if boss_vida > 0:

            golpe = random.randint(10,25)
            vida -= golpe
            print("💥 el boss golpea")

    if vida > 0:

        print("🏆 derrotaste al mini boss")

        monedas_ganadas = random.randint(20,50)
        monedas += monedas_ganadas

        print("💰 monedas:",monedas_ganadas)

# =========================
# EVENTO RARO
# =========================

def evento_raro():

    evento = random.choice([
    "meteorito",
    "portal extraño",
    "aldeano perdido"
    ])

    print("\n✨ EVENTO:",evento)

    if evento == "meteorito":

        inventario.append("diamante")
        print("☄ encuentras minerales raros")

    elif evento == "portal extraño":

        obtener_mutacion()

    elif evento == "aldeano perdido":

        print("⛏ referencia Minecraft")
        print("te paga 30 monedas")

# =========================
# MAPA VISUAL
# =========================

def mostrar_mapa():

    print("\n🗺 MAPA DEL MUNDO\n")

    for i,l in enumerate(mapa):

        if i == posicion:

            print("➡️",l)

        else:

            print("  ",l)

# =========================
# GUARDAR
# =========================

def guardar():

    datos = {

    "vida":vida,
    "hambre":hambre,
    "armadura":armadura,
    "arma":arma,
    "daño":daño,
    "municion":municion,
    "nivel":nivel,
    "exp":exp,
    "monedas":monedas,
    "inventario":inventario,
    "posicion":posicion,
    "exploraciones":exploraciones,
    "tiempo":tiempo,
    "clima":clima,
    "mutaciones":mutaciones

    }

    with open("savegame.json","w") as f:
        json.dump(datos,f)

    print("💾 partida guardada")

# =========================
# CARGAR
# =========================

def cargar():

    global vida,hambre,armadura,arma,daño
    global municion,nivel,exp,monedas
    global inventario,posicion,exploraciones
    global tiempo,clima,mutaciones

    try:

        with open("savegame.json","r") as f:
            datos = json.load(f)

        vida = datos["vida"]
        hambre = datos["hambre"]
        armadura = datos["armadura"]
        arma = datos["arma"]
        daño = datos["daño"]
        municion = datos["municion"]
        nivel = datos["nivel"]
        exp = datos["exp"]
        monedas = datos["monedas"]
        inventario = datos["inventario"]
        posicion = datos["posicion"]
        exploraciones = datos["exploraciones"]
        tiempo = datos["tiempo"]
        clima = datos["clima"]
        mutaciones = datos["mutaciones"]

        print("📂 partida cargada")

    except:

        print("no hay partida guardada")

# =========================
# INTRO
# =========================

print("☢ TIERRA DEVASTADA RPG")

# =========================
# LOOP PRINCIPAL
# =========================

while vida > 0:

    lugar = mapa[posicion]

    print("\n===================")
    print("📍 lugar:",lugar)
    print("🌤 clima:",clima)
    print("🌙 tiempo:",tiempo)
    print("🧭 exploraciones:",exploraciones,"/2")
    print("❤️ vida:",vida)
    print("🛡 armadura:",armadura)
    print("⭐ nivel:",nivel)
    print("💰 monedas:",monedas)
    print("🧬 mutaciones:",mutaciones)

    print("\n1 explorar")
    print("2 buscar comida")
    print("3 usar objeto")
    print("4 avanzar")
    print("5 tienda")
    print("6 guardar")
    print("7 cargar")
    print("8 mapa")
    print("9 inventario")

    accion = input("> ")

# =========================
# TRUCOS
# =========================

    if accion == "/gamemode 1":

        vida = 999
        armadura = 999
        daño = 50
        municion = 999
        monedas = 999

        print("modo dios activado")
        continue

    if accion == "/quintillizas":

        vida += 50
        monedas += 100

        print("las quintillizas te ayudan")
        continue

# =========================
# ACCIONES
# =========================

    if accion == "1":

        enemigo = random.choice(enemigos)
        enemigo_vida = random.randint(30,60)

        print("⚠ aparece",enemigo)

        while enemigo_vida > 0 and vida > 0:

            enemigo_vida -= daño

            if enemigo_vida > 0:

                golpe = random.randint(5,15)
                vida -= golpe

        if vida > 0:

            print("ganaste")

            monedas += random.randint(5,20)
            exploraciones += 1

            if random.randint(1,4) == 1:
                cofre()

            if random.randint(1,6) == 1:
                mini_boss()

            if random.randint(1,12) == 1:
                evento_raro()

    elif accion == "2":

        if random.randint(1,100) < 50:

            inventario.append("comida")
            print("encuentras comida")

        else:

            print("no encuentras nada")

    elif accion == "3":

        if "comida" in inventario:

            inventario.remove("comida")
            hambre -= 20

            print("comes")

        else:

            print("no tienes comida")

    elif accion == "4":

        if exploraciones < 2:

            print("debes explorar 2 veces")

        else:

            if posicion < len(mapa)-1:

                posicion += 1
                exploraciones = 0
                cambiar_clima()

                print("viajas a",mapa[posicion])

            else:

                print("👑 JEFE FINAL IA")

                jefe = 300

                while jefe > 0 and vida > 0:

                    jefe -= daño
                    vida -= 20

                if vida > 0:

                    print("🎉 venciste la IA")
                    break

    elif accion == "5":

        print("1 botiquin 20")
        print("2 armadura 30")
        print("3 municion 15")

        compra = input("> ")

        if compra == "1" and monedas >= 20:

            monedas -= 20
            inventario.append("botiquin")

        elif compra == "2" and monedas >= 30:

            monedas -= 30
            armadura += 5

        elif compra == "3" and monedas >= 15:

            monedas -= 15
            municion += 10

    elif accion == "6":
        guardar()

    elif accion == "7":
        cargar()

    elif accion == "8":
        mostrar_mapa()

    elif accion == "9":

        print("\n🎒 INVENTARIO")

        if len(inventario) == 0:
            print("vacío")

        else:
            for item in inventario:
                print("-",item)

    hambre += 5

    if hambre > 40:
        vida -= 10

    if tiempo == "día":
        tiempo = "noche"
    else:
        tiempo = "día"

print("💀 fin del juego")