from filemanager import manager
from main_ui.mainwindow import Ui_MainWindow
from PyQt4 import QtGui as gui, QtCore as core
import sys
import time

# Import page functionality classes
from pages.view_module      import func as c_func_view_module
from pages.view_baseplate   import func as c_func_view_baseplate
from pages.view_sensor      import func as c_func_view_sensor
from pages.view_PCB         import func as c_func_view_PCB
from pages.view_kapton_step import func as c_func_view_kapton_step
from pages.view_sensor_step import func as c_func_view_sensor_step
from pages.view_pcb_step    import func as c_func_view_pcb_step

# Set up page widgets
from pages_ui.view_module import Ui_Form as form_view_module
class widget_view_module(gui.QWidget,form_view_module):
	def __init__(self,parent):
		super(widget_view_module,self).__init__(parent)
		self.setupUi(self)

from pages_ui.view_baseplate import Ui_Form as form_view_baseplate
class widget_view_baseplate(gui.QWidget,form_view_baseplate):
	def __init__(self,parent):
		super(widget_view_baseplate,self).__init__(parent)
		self.setupUi(self)

from pages_ui.view_sensor import Ui_Form as form_view_sensor
class widget_view_sensor(gui.QWidget,form_view_sensor):
	def __init__(self,parent):
		super(widget_view_sensor,self).__init__(parent)
		self.setupUi(self)

from pages_ui.view_PCB import Ui_Form as form_view_PCB
class widget_view_PCB(gui.QWidget,form_view_PCB):
	def __init__(self,parent):
		super(widget_view_PCB,self).__init__(parent)
		self.setupUi(self)

from pages_ui.view_kapton_step import Ui_Form as form_view_kapton_step
class widget_view_kapton_step(gui.QWidget,form_view_kapton_step):
	def __init__(self,parent):
		super(widget_view_kapton_step,self).__init__(parent)
		self.setupUi(self)

from pages_ui.view_sensor_step import Ui_Form as form_view_sensor_step
class widget_view_sensor_step(gui.QWidget,form_view_sensor_step):
	def __init__(self,parent):
		super(widget_view_sensor_step,self).__init__(parent)
		self.setupUi(self)

from pages_ui.view_pcb_step import Ui_Form as form_view_pcb_step
class widget_view_pcb_step(gui.QWidget, form_view_pcb_step):
	def __init__(self,parent):
		super(widget_view_pcb_step,self).__init__(parent)
		self.setupUi(self)


# Dict of page IDs by name (as the name shows up in the page list widgets)
PAGE_IDS = {
	'modules':0,
	'baseplates':1,
	'sensors':2,
	'PCBs':3,
	'kapton placement steps':4,
	'sensor placement steps':5,
	'PCB placement steps':6,
}
	

def id_generator():
	"""creates a generator for unique ID values"""
	next_id = 0
	while True:
		yield next_id
		next_id += 1


class mainDesigner(gui.QMainWindow,Ui_MainWindow):

	def __init__(self):
		super(mainDesigner,self).__init__(None)
		print("Setting up main UI ...")
		self.setupUi(self)
		print("Finished setting up main UI.")
		print("Initializing file manager...")
		self.fm = manager.manager()
		print("Finished initializing file manager.")
		print("Setting up pages' UI...")
		self.setupPagesUI()
		print("Finished setting up pages' UI.")
		print("Initializing pages...")
		self.initPages()
		print("Finished initializing pages.")
		print("Rigging UI...")
		self.rig()
		print("Finished rigging UI.")
		self.setUIPage('modules')

		self.setWindowTitle("Module Production User Interface")
	
		self.timer_setup()


	def setupPagesUI(self):
		self.page_view_module      = widget_view_module(None)      ; self.swPages.addWidget(self.page_view_module)
		self.page_view_baseplate   = widget_view_baseplate(None)   ; self.swPages.addWidget(self.page_view_baseplate)
		self.page_view_sensor      = widget_view_sensor(None)      ; self.swPages.addWidget(self.page_view_sensor)
		self.page_view_PCB         = widget_view_PCB(None)         ; self.swPages.addWidget(self.page_view_PCB)
		self.page_view_kapton_step = widget_view_kapton_step(None) ; self.swPages.addWidget(self.page_view_kapton_step)
		self.page_view_sensor_step = widget_view_sensor_step(None) ; self.swPages.addWidget(self.page_view_sensor_step)
		self.page_view_pcb_step    = widget_view_pcb_step(None)    ; self.swPages.addWidget(self.page_view_pcb_step)

	def initPages(self):
		self.func_view_module      = c_func_view_module(      self.fm, self.page_view_module     , self.setUIPage, self.setSwitchingEnabled)
		self.func_view_baseplate   = c_func_view_baseplate(   self.fm, self.page_view_baseplate  , self.setUIPage, self.setSwitchingEnabled)
		self.func_view_sensor      = c_func_view_sensor(      self.fm, self.page_view_sensor     , self.setUIPage, self.setSwitchingEnabled)
		self.func_view_PCB         = c_func_view_PCB(         self.fm, self.page_view_PCB        , self.setUIPage, self.setSwitchingEnabled)
		self.func_view_kapton_step = c_func_view_kapton_step( self.fm, self.page_view_kapton_step, self.setUIPage, self.setSwitchingEnabled)
		self.func_view_sensor_step = c_func_view_sensor_step( self.fm, self.page_view_sensor_step, self.setUIPage, self.setSwitchingEnabled)
		self.func_view_pcb_step    = c_func_view_pcb_step(    self.fm, self.page_view_pcb_step   , self.setUIPage, self.setSwitchingEnabled)

		# This list must be in the same order that the pages are in in the stackedWidget in the main UI file.
		# This is the same order as in the dict PAGE_IDS
		self.func_list = [
			self.func_view_module,
			self.func_view_baseplate,
			self.func_view_sensor,
			self.func_view_PCB,
			self.func_view_kapton_step,
			self.func_view_sensor_step,
			self.func_view_pcb_step
			]

	def rig(self):
		self.listInformation.itemActivated.connect(self.changeUIPage)
		self.listAssembly.itemActivated.connect(self.changeUIPage)
		self.listShippingAndReceiving.itemActivated.connect(self.changeUIPage)
		self.swPages.currentChanged.connect(self.pageChanged)

		# later: add forward/back keyboard shortcuts (along with history support)

	def timer_setup(self):
		self.timer_id_gen = id_generator() # unique ID generator for timers
		self.timers = {} # dict of timers {ID:timer}



	def timer_add(self,interval=None,cxn=None,start=False):
		timer = core.QTimer(self)
		ID    = next(self.timer_id_gen)
		self.timers.update([ [ID, timer] ])

		if not (interval is None):
			self.timer_set_interval(ID,interval)

		if not (cxn is None):
			self.timer_connect(ID,cxn)

		if start:
			if interval is None:
				print("Warning: cannot start timer without interval")
			else:
				self.timer_start(ID)

		return ID

	def timer_remove(self,ID):
		if ID in self.timers.keys():
			timer = self.timers.pop(ID)
			timer.stop()
			timer.timeout.disconnect()
			del timer
		else:
			print("Warning: tried to remove nonexistent timer with ID {}".format(ID))

	def timer_start(self,ID):
		if ID in self.timers.keys():
			self.timers[ID].start()
		else:
			print("Warning: tried to start nonexistent timer with ID {}".format(ID))

	def timer_stop(self,ID):
		if ID in self.timers.keys():
			self.timers[ID].stop()
		else:
			print("Warning: tried to stop nonexistent timer with ID {}".format(ID))

	def timer_connect(self,ID,cxn):
		if ID in self.timers.keys():
			self.timers[ID].timeout.connect(cxn)
		else:
			print("Warning: tried to connect {} to nonexistent timer with ID {}".format(cxn,ID))

	def timer_disconnect(self,ID):
		if ID in self.timers.keys():
			self.timers[ID].timeout.disconnect()
		else:
			print("Warning: tried to disconnect nonexistent timer with ID {}".format(ID))

	def timer_set_interval(self,ID,interval_ms):
		if ID in self.timers.keys():
			self.timers[ID].setInterval(interval_ms)
		else:
			print("Warning: tried to set interval of nonexistent timer with ID {} to {}".format(ID, interval_ms))


	

	def pageChanged(self,*args,**kwargs):
		self.func_list[args[0]].changed_to()

	def changeUIPage(self,*args,**kwargs):
		self.setUIPage(args[0].text())

	def setUIPage(self,which_page,**kwargs):
		if which_page in PAGE_IDS.keys():

			if self.func_list[PAGE_IDS[which_page]].mode == 'setup':
				print("page {} not yet setup; doing setup".format(which_page))
				self.func_list[PAGE_IDS[which_page]].setup()

			self.swPages.setCurrentIndex(PAGE_IDS[which_page])
			if len(kwargs) > 0:
				self.func_list[PAGE_IDS[which_page]].load_kwargs(kwargs)
		else:
			print("Page <{}> not supported yet".format(which_page))

	def setSwitchingEnabled(self,enabled):
		self.listInformation.setEnabled(enabled)
		self.listAssembly.setEnabled(enabled)
		self.listShippingAndReceiving.setEnabled(enabled)

	


if __name__ == '__main__':
	app = gui.QApplication(sys.argv)
	m=mainDesigner()
	m.resize(1366,768)
	m.show()
	sys.exit(app.exec_())
