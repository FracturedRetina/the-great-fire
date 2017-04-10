import curses
from fire import Fire
from time import sleep
from typist import UnTypist
from snow import Snow
import lyrics
from pygame import mixer

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.nodelay(True)
mixer.init()
mixer.music.load("1519.mp3")
mixer.music.play()

lyr = lyrics.load()
fires = [Fire(14, 14), Fire(stdscr.getmaxyx()[1] - 14, 14)]
snow = Snow(stdscr)

title = UnTypist("The Great Fire - OK GO", x="center", y="center", win=stdscr)
tps = UnTypist("", x=16, y=16)
tps2 = UnTypist("", x=40, y=16)
t = 40
currtps = True
paused = False

while True:
	#Input
	k = stdscr.getch()

	if k == ord('q'):
		break
	if k == ord('p'):
		paused = not paused

	#Step
	if not paused:
		if t / 8.0 <= 20  or (t - 3) / 4 % 4 or t / 8.0 >= 82:
			for f in fires:
				f.step()
		tps.step()
		tps2.step()
		if t / 8.0 in lyr:
			if currtps:
				tps = UnTypist(lyr[t/8], x=16, y=16, sustain=lyrics.getdur(lyr[t/8]))
			else:
				tps2 = UnTypist(lyr[t/8], x=40, y=16, sustain=lyrics.getdur(lyr[t/8]))
			currtps = not currtps
	if t / 8.0 >= 12:
		title.step()
	if t / 8.0 == 82:
		snow = Snow(stdscr)
		for f in fires:
			f.stop()
	if t / 8.0 >= 82:
		snow.step()
	if t / 8.0 == 124:
		for f in fires:
			f.start()
	if t / 8.0 >= 130 and t % 4 == 0:
		for f in fires:
			if f.x < stdscr.getmaxyx()[1] / 2 or f.x <= 14:
				f.x += 1
			elif f.x >= stdscr.getmaxyx()[1] / 2 or f.x >= stdscr.getmaxyx()[1] - 14:
				f.x -= 1
	if t / 8.0 == 164:
		snow.stop()
	if t / 8.0 == 220:
		snow.start()
		for f in fires:
			f.stop()
	if t / 8.0 == 252:
		title = UnTypist("Animation by Evan Shimoniak", x="center", y="center", win=stdscr)

	#Draw
	stdscr.clear()
	if t / 8.0 >= 82:
		snow.draw(stdscr)
	for f in  fires:
		f.draw(stdscr)
	tps.draw(stdscr)
	tps2.draw(stdscr)
	title.draw(stdscr)

#	stdscr.addstr(0, 0, "measure=%i" % (t / 32 + 1))
#	stdscr.addstr(1, 0, "beat=%i" % ((t % 32) / 8 + 1))
#	stdscr.addstr(2, 0, "cbeat=%i" % (t / 8 + 1))
#	stdscr.addstr(3, 0, "t=%i" % t)
	
	stdscr.refresh()
	
	
	t += 1
#	sleep(1.0 / 8.0) #60 bpm (maybe)
	sleep(12.0 / 13.0 / 8.0) #65 bpm (maybe)
#	sleep(13.0 / 12.0 / 8.0) #65 bpm (maybe)


stdscr.keypad(0)
curses.echo()
curses.nocbreak()
curses.curs_set(1)
stdscr.nodelay(True)

curses.endwin()
