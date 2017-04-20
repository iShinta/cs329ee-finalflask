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
@app.route('/call-of-duty-modern-warfare-3')
def callofdutymodernwarfare3():
	return render_template('call-of-duty-modern-warfare-3.html')

@app.route('/fifa-2016')
def fifa2016():
	return render_template('fifa-2016.html')

@app.route('/final-fantasy-viii')
def finalfantasyviii():
	return render_template('final-fantasy-viii.html')

@app.route('/grand-theft-auto-v')
def grandtheftautov():
	return render_template('grand-theft-auto-v.html')

@app.route('/grand-turismo-3-a-spec')
def grandturismo3aspec():
	return render_template('grand-turismo-3-a-spec')

@app.route('/just-dance-3')
def justdance3():
	return render_template('just-dance-3')

@app.route('/kinect-adventures')
def kinectadventures():
	return render_template('kinect-adventures')

@app.route('/mario-and-sonic-at-the-olympic-games')
def marioandsonicattheolympicgames():
	return render_template('mario-and-sonic-at-the-olympic-games')

@app.route('/mario-kart-8')
def mariokart8():
	return render_template('mario-kart-8')

@app.route('/mario-kart-wii')
def mariokartwii():
	return render_template('mario-kart-wii')

@app.route('/pac-man')
def pacman():
	return render_template('pac-man')

@app.route('/pokemon-emerald-version')
def pokemonemeraldversion():
	return render_template('pokemon-emerald-version')

@app.route('/pokemon-red-pokemon-blue')
def pokemonredpokemonblue():
	return render_template('pokemon-red-pokemon-blue')

@app.route('/street-fighter-ii-the-world-warrior')
def streetfighteriitheworldwarrior():
	return render_template('street-fighter-ii-the-world-warrior')

@app.route('/super-mario-bros')
def supermariobros():
	return render_template('super-mario-bros')
	
@app.route('/super-smash-bros-melee')
def supersmashbrosmelee():
	return render_template('super-smash-bros-melee')

@app.route('/the-elder-scrolls-v-skyrim')
def theelderscrollsvskyrim():
	return render_template('the-elder-scrolls-v-skyrim')

@app.route('/the-legend-of-zelda')
def thelegendofzelda():
	return render_template('the-legend-of-zelda')
	
@app.route('/wii-sports')
def wiisports():
	return render_template('wii-sports')

@app.route('/wii-sports-resort')
def wiisportsresort():
	return render_template('wii-sports-resort')

@app.route('/world-of-warcraft')
def worldofwarcraft():
	return render_template('world-of-warcraft')
	
#platforms
#PLATFORMS

@app.route('/atari-2600')
def atari2600():
	return render_template('atari-2600')

@app.route('/gb')
def gb():
	return render_template('gb')
@app.route('/gba')
def gba():
	return render_template('gba')

@app.route('/gc')
def gc():
	return render_template('gc')

@app.route('/nes')
def nes():
	return render_template('nes')

@app.route('/pc')
def pc():
	return render_template('pc')

@app.route('/ps')
def ps():
	return render_template('ps')

@app.route('/ps2')
def ps2():
	return render_template('ps2')

@app.route('/ps3')
def ps3():
	return render_template('ps3')

@app.route('/ps4')
def ps4():
	return render_template('ps4')

@app.route('/snes')
def snes():
	return render_template('snes')

@app.route('/wii')
def wii():
	return render_template('wii')

@app.route('/wiiu')
def wiiu():
	return render_template('wiiu')

@app.route('/x360')
def x360():
	return render_template('x360')

@app.route('/xone')
def xone():
	return render_template('xone')

#PUBLISHERS

@app.route('/activision')
def activision():
	return render_template('activision')

@app.route('/atari')
def atari():
	return render_template('atari')

@app.route('/bethesda')
def bethesda():
	return render_template('bethesda')

@app.route('/capcom')
def capcom():
	return render_template('capcom')

@app.route('/ea')
def ea():
	return render_template('ea')

@app.route('/microsoft-game-studios')
def microsoftgamestudios():
	return render_template('microsoft-game-studios')

@app.route('/nintendo')
def nintendo():
	return render_template('nintendo')

@app.route('/sega')
def sega():
	return render_template('sega')

@app.route('/sony')
def sony():
	return render_template('sony')

@app.route('/squaresoft')
def squaresoft():
	return render_template('squaresoft')

@app.route('/take-two-interactive')
def taketwointeractive():
	return render_template('take-two-interactive')

@app.route('/ubisoft')
def ubisoft():
	return render_template('ubisoft')

	
if __name__ == '__main__':
	app.run() # Run application