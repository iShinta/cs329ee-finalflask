from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''

# MAIN PAGES
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/games')
def games():
	return render_template('games.html')

@app.route('/platforms')
def platforms():
	return render_template('platforms.html')

@app.route('/publishers')
def publishers():
	return render_template('publishers.html')

# SUB PAGES

#games below
@app.route('/games/call-of-duty-modern-warfare-3')
def callofdutymodernwarfare3():
	return render_template('/games/call-of-duty-modern-warfare-3.html')

@app.route('/games/fifa-2016')
def fifa2016():
	return render_template('/games/fifa-2016.html')

@app.route('/games/final-fantasy-viii')
def finalfantasyviii():
	return render_template('/games/final-fantasy-viii.html')

@app.route('/games/grand-theft-auto-v')
def grandtheftautov():
	return render_template('/games/grand-theft-auto-v.html')

@app.route('/games/gran-turismo-3-a-spec')
def granturismo3aspec():
	return render_template('/games/grand-turismo-3-a-spec.html')

@app.route('/games/just-dance-3')
def justdance3():
	return render_template('/games/just-dance-3.html')

@app.route('/games/kinect-adventures')
def kinectadventures():
	return render_template('/games/kinect-adventures.html')

@app.route('/games/mario-and-sonic-at-the-olympic-games')
def marioandsonicattheolympicgames():
	return render_template('/games/mario-and-sonic-at-the-olympic-games.html')

@app.route('/games/mario-kart-8')
def mariokart8():
	return render_template('/games/mario-kart-8.html')

@app.route('/games/mario-kart-wii')
def mariokartwii():
	return render_template('/games/mario-kart-wii.html')

@app.route('/games/pac-man')
def pacman():
	return render_template('/games/pac-man.html')

@app.route('/games/pokemon-emerald-version')
def pokemonemeraldversion():
	return render_template('/games/pokemon-emerald-version.html')

@app.route('/games/pokemon-red-pokemon-blue')
def pokemonredpokemonblue():
	return render_template('/games/pokemon-red-pokemon-blue.html')

@app.route('/games/street-fighter-ii-the-world-warrior')
def streetfighteriitheworldwarrior():
	return render_template('/games/street-fighter-ii-the-world-warrior.html')

@app.route('/games/super-mario-bros')
def supermariobros():
	return render_template('/games/super-mario-bros.html')
	
@app.route('/games/super-smash-bros-melee')
def supersmashbrosmelee():
	return render_template('/games/super-smash-bros-melee.html')

@app.route('/games/the-elder-scrolls-v-skyrim')
def theelderscrollsvskyrim():
	return render_template('/games/the-elder-scrolls-v-skyrim.html')

@app.route('/games/the-legend-of-zelda')
def thelegendofzelda():
	return render_template('/games/the-legend-of-zelda.html')
	
@app.route('/games/wii-sports')
def wiisports():
	return render_template('/games/wii-sports.html')

@app.route('/games/wii-sports-resort')
def wiisportsresort():
	return render_template('/games/wii-sports-resort.html')

@app.route('/games/world-of-warcraft')
def worldofwarcraft():
	return render_template('/games/world-of-warcraft.html')

#platforms
#PLATFORMS

@app.route('/platforms/atari-2600')
def atari2600():
	return render_template('/platforms/atari-2600.html')

@app.route('/platforms/gb')
def gb():
	return render_template('/platforms/gb.html')
@app.route('/platforms/gba')
def gba():
	return render_template('/platforms/gba.html')

@app.route('/platforms/gc')
def gc():
	return render_template('/platforms/gc.html')

@app.route('/platforms/nes')
def nes():
	return render_template('/platforms/nes.html')

@app.route('/platforms/pc')
def pc():
	return render_template('/platforms/pc.html')

@app.route('/platforms/ps')
def ps():
	return render_template('/platforms/ps.html')

@app.route('/platforms/ps2')
def ps2():
	return render_template('/platforms/ps2.html')

@app.route('/platforms/ps3')
def ps3():
	return render_template('/platforms/ps3.html')

@app.route('/platforms/ps4')
def ps4():
	return render_template('/platforms/ps4.html')

@app.route('/platforms/snes')
def snes():
	return render_template('/platforms/snes.html')

@app.route('/platforms/wii')
def wii():
	return render_template('/platforms/wii.html')

@app.route('/platforms/wiiu')
def wiiu():
	return render_template('/platforms/wiiu.html')

@app.route('/platforms/x360')
def x360():
	return render_template('/platforms/x360.html')

@app.route('/platforms/xone')
def xone():
	return render_template('/platforms/xone.html')

#PUBLISHERS

@app.route('/publishers/activision')
def activision():
	return render_template('/publishers/activision.html')

@app.route('/publishers/atari')
def atari():
	return render_template('/publishers/atari.html')

@app.route('/publishers/bethesda')
def bethesda():
	return render_template('/publishers/bethesda.html')

@app.route('/publishers/capcom')
def capcom():
	return render_template('/publishers/capcom.html')

@app.route('/publishers/ea')
def ea():
	return render_template('/publishers/ea.html')

@app.route('/publishers/microsoft-game-studios')
def microsoftgamestudios():
	return render_template('/publishers/microsoft-game-studios.html')

@app.route('/publishers/nintendo')
def nintendo():
	return render_template('/publishers/nintendo.html')

@app.route('/publishers/sega')
def sega():
	return render_template('/publishers/sega.html')

@app.route('/publishers/sony')
def sony():
	return render_template('/publishers/sony.html')

@app.route('/publishers/squaresoft')
def squaresoft():
	return render_template('/publishers/squaresoft.html')

@app.route('/publishers/take-two-interactive')
def taketwointeractive():
	return render_template('/publishers/take-two-interactive.html')

@app.route('/publishers/ubisoft')
def ubisoft():
	return render_template('/publishers/ubisoft.html')

	
if __name__ == '__main__':
	app.run('159.203.132.67', '80') # Run application
