from random import randint

class SnowParticle:
	def __init__(self, x, y=0, SWAY=0, GRAVITY=1):
		self.x = x
		self.y = y
		self.SWAY = SWAY
		self.GRAVITY = GRAVITY
	
	def step(self):
		#Vertical movement
		if self.GRAVITY > 1:
			self.y += self.GRAVITY
		elif randint(0, 1 / (self.GRAVITY) + 1) == 0:
			self.y += 1
		#Horizontal movement
		if self.SWAY > 1:
			self.x += randint(-1 * self.SWAY, self.SWAY)
		elif randint(0, 1 / (self.SWAY + 1)) == 0:
			self.x += randint(-1, 1)
	
	def draw(self, win):
		if not self.oob(win.getmaxyx()[1], win.getmaxyx()[0]):
			win.addstr(self.y, self.x, '*')
	
	def oob(self, w, h):
		return self.x < 0 or self.y < 0 or self.x >= w - 1 or self.y >= h - 1

class Snow:
	def __init__(self, win, SWAY=1, GRAVITY=1, nPart=30):
		self.SWAY = SWAY
		self.GRAVITY = GRAVITY
		self.nPart = nPart
		self.h, self.w = win.getmaxyx()
		self.particles = []
		self.stopped = False
		if self.nPart / self.h:
			for i in xrange(0, self.nPart / self.h):
				if len(self.particles) < self.nPart:
					self.particles.append(SnowParticle(randint(0, self.w - 1), SWAY=self.SWAY, GRAVITY=self.GRAVITY))
		elif randint(0, 2 * self.h / self.nPart):
			if len(self.particles) < self.nPart:
				self.particles.append(SnowParticle(randint(0, self.w - 1), SWAY=self.SWAY, GRAVITY=self.GRAVITY))
	
	def step(self):
		if self.nPart / self.h:
			for i in xrange(0, self.nPart / self.h):
				if not self.stopped and len(self.particles) < self.nPart:
					self.particles.append(SnowParticle(randint(0, self.w - 1), SWAY=self.SWAY, GRAVITY=self.GRAVITY))
		elif randint(0, self.h / self.nPart):
			if not self.stopped and len(self.particles) < self.nPart:
				self.particles.append(SnowParticle(randint(0, self.w - 1), SWAY=self.SWAY, GRAVITY=self.GRAVITY))
		for p in self.particles:
			if p.oob(self.w, self.h):
				self.particles.remove(p)
				if not self.stopped:
					self.particles.append(SnowParticle(randint(0, self.w - 1), SWAY=self.SWAY, GRAVITY=self.GRAVITY))
			else:
				p.step()
	
	def draw(self, win):
		for p in self.particles:
			p.draw(win)
		self.h, self.w = win.getmaxyx()

	def stop(self):
		self.stopped = True

	def start(self):
		self.stopped = False
