# KIND   # FUEL       #     #
#############################
# ember  #  0% -  30% # 0-1 #
# tongue # 30% -  70% # 2-3 #
# body   # 70% - 100% # 4-5 #
#############################

from random import randint

class Particle:
	def __init__(self, x, y, fuel=10, SPREAD = 0.05, UPDRAFT = 5):
		self.x = x
		self.y = y
		self.fuel = fuel
		self.c = ' '
		self.SPREAD = SPREAD
		self.UPDRAFT = UPDRAFT
	
	def step(self):
		#Moves particles vertically
		if randint(0, int(self.fuel ** 2 / self.UPDRAFT)) == 0:
			self.y -= 1
			self.x += randint(-1, 1)
			self.fuel -= 7 / self.UPDRAFT
		#Moves particles horizontally
		if randint(0, 1 + int(self.y / self.SPREAD)) == 0:
			self.x += randint(-1, 1)
		#Chooses particle character
		if self.fuel > 7:
			if randint(0, 1):
				self.c = '%'
			else:
				self.c = '&'
		elif self.fuel > 3:
			if randint(0, 1):
				self.c = '('
			else:
				self.c = ')'
		else:
			r = randint(0,4)
			if r == 0:
				self.c = '.'
			elif r == 1:
				self.c = ','
			elif r == 2:
				self.c = '\''
			elif r == 3:
				self.c = '*'
			else:
				self.c = '`'
	
	def draw(self, win):
		if not self.oob(win):
			win.addstr(self.y, self.x, self.c)

	def oob(self, win):
		return self.x < 0 or self.y < 0 or self.x >= win.getmaxyx()[1] - 1 or self.y >= win.getmaxyx()[0] - 1

class Fire:
	def __init__(self, x, y, w=5.0, h=10.0, nPart=32):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.nPart = nPart
		self.particles = []
		self.stopped = False

		for i in xrange(0, nPart):
			self.particles.append(Particle(self.x, self.y, SPREAD=self.w/60, UPDRAFT=self.h/1.5))
	
	def step(self):
		for p in self.particles:
			if p.fuel <= 0:
				self.particles.remove(p)
				if not self.stopped:
					self.particles.append(Particle(self.x, self.y, SPREAD=self.w/60, UPDRAFT=self.h/1.5))
			else:
				p.step()
	
	def draw(self, win):
		for p in self.particles:
			p.draw(win)

	def stop(self):
		self.stopped = True
		for p in self.particles:
			p.fuel *= 0.8

	def start(self):
		self.stopped = False
		while len(self.particles) < self.nPart:
			self.particles.append(Particle(self.x, self.y, SPREAD=self.w/60, UPDRAFT=self.h/1.5))