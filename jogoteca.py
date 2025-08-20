from flask import Flask, render_template, request, redirect
from unicodedata import category


# Melhor trabalhar com classes

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

games_data = [
        ("DOOM (1993)", "Clássico / Boomer Shooter", "PC (MS-DOS)"),
        ("DOOM (2016)", "Ação / Single-player", "Multiplataforma (PC/PS4/XOne)"),
        ("DOOM Eternal", "Ação / Single-player", "Multiplataforma (PC/PS4/PS5/XOne/XSX/Switch)"),
        ("Quake", "Arena Shooter", "PC"),
        ("Quake II", "Arena Shooter", "PC"),
        ("Quake III Arena", "Arena Shooter", "PC"),
        ("Quake Champions", "Arena Shooter", "PC"),
        ("Unreal Tournament", "Arena Shooter", "PC"),
        ("Unreal Tournament 2004", "Arena Shooter", "PC"),
        ("Half-Life", "Narrativo / Sci-Fi", "PC"),
        ("Half-Life 2", "Narrativo / Sci-Fi", "PC"),
        ("Counter-Strike 1.6", "Tático / Competitivo", "PC"),
        ("Counter-Strike: Source", "Tático / Competitivo", "PC"),
        ("Counter-Strike: Global Offensive", "Tático / Competitivo", "PC"),
        ("Counter-Strike 2", "Tático / Competitivo", "PC"),
        ("Team Fortress 2", "Classes / Arcade", "PC"),
        ("Call of Duty 4: Modern Warfare (2007)", "Militar Moderno", "Multiplataforma (PC/PS3/X360)"),
        ("Call of Duty: Modern Warfare (2019)", "Militar Moderno", "Multiplataforma (PC/PS4/XOne)"),
        ("Call of Duty: Warzone", "Battle Royale / Militar", "Multiplataforma (PC/PS/Xbox)"),
        ("Battlefield 1942", "Militar / Segunda Guerra", "PC"),
        ("Battlefield 3", "Militar Moderno", "Multiplataforma (PC/PS3/X360)"),
        ("Battlefield 4", "Militar Moderno", "Multiplataforma (PC/PS/Xbox)"),
        ("Battlefield 1", "Militar / Primeira Guerra", "Multiplataforma (PC/PS4/XOne)"),
        ("Battlefield V", "Militar / Segunda Guerra", "Multiplataforma (PC/PS4/XOne)"),
        ("Halo: Combat Evolved", "Sci-Fi", "Xbox"),
        ("Halo 3", "Sci-Fi", "Xbox 360"),
        ("Halo Infinite", "Sci-Fi", "Xbox/PC"),
        ("Titanfall 2", "Sci-Fi / Parkour", "Multiplataforma (PC/PS4/XOne)"),
        ("Apex Legends", "Battle Royale / Hero Shooter", "Multiplataforma (PC/PS/Xbox/Switch)"),
        ("Rainbow Six Siege", "Tático / Operações", "Multiplataforma (PC/PS/Xbox)"),
        ("Far Cry 3", "Ação / Mundo Aberto", "Multiplataforma (PC/PS3/X360)"),
        ("Far Cry 5", "Ação / Mundo Aberto", "Multiplataforma (PC/PS4/XOne)"),
        ("BioShock", "Narrativo / Immersive Sim", "Multiplataforma (PC/PS3/X360)"),
        ("BioShock Infinite", "Narrativo / Immersive Sim", "Multiplataforma (PC/PS3/X360)"),
        ("Metro 2033", "Horror / Narrativo", "Multiplataforma (PC/X360)"),
        ("Metro: Last Light", "Horror / Narrativo", "Multiplataforma (PC/PS3/X360)"),
        ("Metro Exodus", "Horror / Narrativo", "Multiplataforma (PC/PS4/PS5/XOne/XSX)"),
        ("Crysis", "Sci-Fi / Tech Shooter", "PC"),
        ("Crysis 2", "Sci-Fi / Ação", "Multiplataforma (PC/PS3/X360)"),
        ("Crysis 3", "Sci-Fi / Ação", "Multiplataforma (PC/PS3/X360)"),
        ("F.E.A.R.", "Horror / Ação", "Multiplataforma (PC/PS3/X360)"),
        ("F.E.A.R. 2: Project Origin", "Horror / Ação", "Multiplataforma (PC/PS3/X360)"),
        ("S.T.A.L.K.E.R.: Shadow of Chernobyl", "Sobrevivência / Imersivo", "PC"),
        ("S.T.A.L.K.E.R.: Call of Pripyat", "Sobrevivência / Imersivo", "PC"),
        ("Serious Sam: The First Encounter", "Arcade / Horda", "PC"),
        ("Wolfenstein 3D", "Clássico", "PC (MS-DOS)"),
        ("Wolfenstein: The New Order", "Ação / Narrativo", "Multiplataforma (PC/PS3/PS4/X360/XOne)"),
        ("Wolfenstein II: The New Colossus", "Ação / Narrativo", "Multiplataforma (PC/PS4/XOne/Switch)"),
        ("GoldenEye 007", "Espionagem / Arcade", "Nintendo 64"),
        ("Perfect Dark", "Sci-Fi / Espionagem", "Nintendo 64"),
        ("Destiny 2", "Looter Shooter / MMO", "Multiplataforma (PC/PS/Xbox)"),
        ("Borderlands 2", "Looter Shooter / RPG", "Multiplataforma (PC/PS3/PS4/X360/XOne)"),
        ("Borderlands 3", "Looter Shooter / RPG", "Multiplataforma (PC/PS/Xbox)"),
        ("Insurgency", "Tático / Realista", "PC"),
        ("Insurgency: Sandstorm", "Tático / Realista", "Multiplataforma (PC/PS/Xbox)"),
        ("ARMA 3", "Simulador Militar", "PC"),
        ("Squad", "Tático Militar", "PC"),
        ("Hell Let Loose", "Tático / Segunda Guerra", "Multiplataforma (PC/PS5/XSX)"),
        ("SWAT 4", "Tático / Operações", "PC"),
        ("Red Orchestra 2: Heroes of Stalingrad", "Tático / Segunda Guerra", "PC"),
        ("Rising Storm 2: Vietnam", "Tático / Guerra do Vietnã", "PC"),
        ("Planetside 2", "MMOFPS", "PC/PS4"),
        ("Paladins", "Hero Shooter", "Multiplataforma (PC/PS/Xbox/Switch)"),
        ("Overwatch", "Hero Shooter", "Multiplataforma (PC/PS/Xbox/Switch)"),
        ("VALORANT", "Tático / Competitivo", "PC"),
        ("Escape from Tarkov", "Extraction / Sobrevivência", "PC"),
        ("Project I.G.I.", "Tático / Espionagem", "PC"),
        ("Prey (2017)", "Immersive Sim / Sci-Fi", "Multiplataforma (PC/PS4/XOne)"),
        ("Painkiller", "Arcade / Horda", "PC"),
        ("Bulletstorm", "Ação / Arcade", "Multiplataforma (PC/PS3/X360)"),
        ("Killzone 2", "Sci-Fi", "PlayStation 3"),
        ("Resistance: Fall of Man", "Sci-Fi", "PlayStation 3"),
        ("TimeSplitters 2", "Arcade", "PS2/GameCube/Xbox"),
        ("TimeSplitters: Future Perfect", "Arcade", "PS2/GameCube/Xbox"),
        ("Turok: Dinosaur Hunter", "Aventura / Sci-Fi", "Nintendo 64"),
        ("Shadow Warrior (2013)", "Ação / Single-player", "Multiplataforma (PC/PS4/XOne)"),
        ("Shadow Warrior 2", "Ação / Co-op", "Multiplataforma (PC/PS4/XOne)"),
        ("Heretic", "Fantasia / Clássico", "PC (MS-DOS)"),
        ("Hexen", "Fantasia / Clássico", "PC (MS-DOS)"),
        ("Medal of Honor: Allied Assault", "Militar / Segunda Guerra", "PC"),
        ("Black", "Ação / Arcade", "PlayStation 2 / Xbox"),
        ("Verdun", "Militar / Primeira Guerra", "Multiplataforma (PC/PS/Xbox)"),
        ("Tannenberg", "Militar / Primeira Guerra", "Multiplataforma (PC/PS/Xbox)"),
    ]


app = Flask(__name__)

@app.route('/')
def index():
     #____#

    games = [Game(name, category, console) for (name, category, console) in games_data]
    return render_template('list.html', title='Games', games=games)

@app.route('/new')
def new():
    return render_template('new.html',titulo='New Game')

@app.route('/create',methods=['POST',])
def create():
    name     = request.form['name']
    category = request.form['category']
    console  = request.form['console']
    game     = Game(name, category, console)
    games_data.append(game)
    return redirect('/')
app.run(host='0.0.0.0', port=8080,debug=True)
