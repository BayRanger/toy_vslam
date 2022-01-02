import sdl2.ext
import warnings

class Display(object):
	def __init__(self,W,H):
		sdl2.ext.init()
		warnings.filterwarnings("ignore")
		self.W = W
		self.H = H
		self.window = sdl2.ext.Window("toy slam",size=(W,H),position=(2000,0))
		self.window.show()
	
	def paint(self,img):
		events = sdl2.ext.get_events()
		for event in events:
			if event.type == sdl2.SDL_QUIT:
				exit(0)
		surf = sdl2.ext.pixels3d(self.window.get_surface())
		surf[:,:,:3] = img.swapaxes(0,1)
		self.window.refresh()	
	
