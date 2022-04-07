from os import system

system("clear")
noEdited = """
Ángel
Ojo
Pizza
Enojado
Fuegos artificiales
Calabaza
Bebé
Flor
Arco iris
Barba
Platillo volador
Reciclar
Biblia
Jirafa
Castillo  arena
Bikini
Gafas
Copo  nieve
Libro
Tacón
Escalera
Cucurucho  helado
Estrella  mar
Abejorro
Iglú
Fresa
Mariposa
Escarabajo
Sol
Cámara
Lámpara
Neumático
Gato
León
Tostada
Iglesia
Buzón
Cepillo de dientes
Lápiz de color
Noche
Pasta dental
Delfín
Nariz
Camión
Huevo
Juegos Olímpicos
Voleibol
Torre Eiffel
Maní
Beso
Cerebro
Cachorro
Patio  recreo
Britney Spears
Baño  burbujas
Kiwi
Pastel  calabaza
Hebilla
Lápiz labial
Gota  lluvia
Autobús
Langosta
Robot
Accidente automovilistico
Chupete
Castillo  arena
Imán
Zapatilla
Sierra  cadena
Megáfono
Bola  nieve
Tienda  circo
Sirena
Aspersor
Computadora
Minivan
Estatua Libertad

Cuna
Monte Everest
Renacuajo
Dragón
Música
Campamento
Pesa
Polo Norte
Telescopio
Anguila
Enfermera
Tren
Rueda
fortuna
Búho
Triciclo
Bandera
Chupete
Tutú
Correo
deseado
Piano
Ático
Pegamento
Reloj  bolsillo
Asiento trasero
Silla alta
Banda  rock
México
Cumpleaños
Hockey
Piegrande
Calabozo
Hotel
Huevos revueltos
Tormenta nieve
Cuerda saltar
Cinturón seguridad
Burrito
Koala
Ignorar
Capitán
Duende
Eclipse solar
Candelabro
Rápido
Espacio
Cuna
Mascara
Estetoscopio
Crucero
Mecánico
Cigüeña
Baile
Mama
Bronceado
Desodorante
Señor Cara Papa
Hilo
Facebook
Saturno
Turista
Plano
Plato papel
Estados Unidos
Marco
Foto
WIFI
Luna llena
Monja
Zombi
Juego
Pirata
"""
noEdited = noEdited.split("\n")

wordsNoSpaces = ""
for w in noEdited:
    wordsNoSpaces += w + ","

# print(wordsNoSpaces)

wordsNoSpaces = wordsNoSpaces.split(" ")
# print(wordsNoSpaces)

edited = ""
for w in wordsNoSpaces:
    edited += w + ","

finalWords = edited.split(",")
print(finalWords)

finalWords = list(set(finalWords))
