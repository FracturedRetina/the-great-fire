import types

class Typist:
	def __init__(self, string, speed=1, x=0, y=0, win=None):
		self.string = string
		self.speed = speed
		if type(x) in types.StringTypes and win != None:
			self.x = int(win.getmaxyx()[1] / 2.0 - len(string) / 2.0)
		else:
			self.x = x
		if type(y) in types.StringTypes and win != None:
			self.y = win.getmaxyx()[0] / 2
		else:
			self.y = y
		self.i = 0

	def done(self):
		return self.i >= len(self.string)
	
	def step(self):
		if not self.done():
			self.i += self.speed
	
	def draw(self, win):
		alphaprint(win, self.x, self.y, self.string[:self.i], False)

class UnTypist(Typist):
	def __init__(self, string, speed=1, x=0, y=0, sustain=20, unspeed=0, win=None):
		Typist.__init__(self, string, speed, x, y, win)
		self.sustain = sustain
		if unspeed == 0:
			self.unspeed = 2 * speed
		else:
			self.unspeed = unspeed
	
	def done(self):
		return self.i >= 2*len(self.string) + self.sustain
	
	def step(self):
		if not self.done() and self.i >= len(self.string):
			self.i += self.unspeed
		elif self.i < len(self.string) + self.sustain:
			self.i += self.speed
		elif not self.done():
			self.i += 1
	
	def draw(self, win):
		if self.i < len(self.string) + self.sustain:
			alphaprint(win, self.x, self.y, self.string[:self.i])
		elif not self.done():
			alphaprint(win, self.x, self.y, self.string[:2*len(self.string) + self.sustain - self.i])

def alphaprint(win, x, y, string, alphaspaces=True):
	dx = 0
	dy = 0

	for c in string:
		if c == ' ' and alphaspaces:
			dx += 1
		elif c == '\n':
			dy += 1
			dx = 0
		else:
			win.addstr(y + dy, x + dx, c)
			dx += 1