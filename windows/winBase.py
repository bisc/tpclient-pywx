"""\
This module contains the "base" for all main windows. It does things
like prepending "TP:" to the title, vetoing closing of the window
and raising all the other windows when one is clicked.
"""

import wx
import os.path

class Blank:
	pass
wx.local = Blank()

if wx.Platform == "__WXMAC__":
	wx.local.smallSize  = wx.Size(25,25)
	wx.local.buttonSize = wx.Size(60,30)
	wx.local.spinSize   = wx.Size(50,25)

	wx.local.normalFont = wx.Font(12,  wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	try:
		wx.local.tinyFont   = wx.Font(10,  wx.DEFAULT, wx.LIGHT, wx.NORMAL)
	except:
		wx.local.tinyFont   = wx.Font(10,  wx.DEFAULT, wx.NORMAL, wx.NORMAL)	
	wx.local.largeFont  = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

else:
	wx.local.smallSize  = wx.Size(15,15)
	wx.local.buttonSize = wx.Size(50,20)
	wx.local.spinSize   = wx.Size(40,15)

	wx.local.normalFont = wx.Font(7,  wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	try:
		wx.local.tinyFont   = wx.Font(6,  wx.DEFAULT, wx.LIGHT, wx.NORMAL)
	except:
		wx.local.tinyFont   = wx.Font(6,  wx.DEFAULT, wx.NORMAL, wx.NORMAL)	
	wx.local.largeFont  = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

class ConfigMixIn(object):
	def ConfigDefault(self, config=None):
		"""\
		Fill out the config with defaults (if the options are not valid or nonexistant).
		"""
		raise AssertionError("ConfigSave not implimented")

	def ConfigSave(self):
		"""\
		Returns the configuration of the Window (and it's children).
		"""
		return self.config
		
	def ConfigLoad(self, config={}):
		"""\
		Loads the configuration of the Window (and it's children).
		"""
		raise AssertionError("ConfigLoad not implimented")

	def ConfigUpdate(self):
		"""\
		Updates the config details using external sources.
		"""
		raise AssertionError("ConfigUpdate not implimented")

	def ConfigDisplay(self, panel, sizer):
		"""\
		Display a config panel with all the config options.
		"""
		raise AssertionError("ConfigDisplay not implimented")
	
	def ConfigDisplayUpdate(self, evt):
		"""\
		Update the Display because it's changed externally.
		"""
		raise AssertionError("ConfigDisplayUpdate not implimented")

class winBaseMixIn(object):
	def __init__(self, application, parent, config=None):
		self.application = application
		self.parent = parent
		self.children = {}
		self.config = self.ConfigDefault()
	
		if hasattr(parent, 'children'):
			self.parent.children[self.title] = self

		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.Bitmap(os.path.join("graphics", "icon.ico"), wx.BITMAP_TYPE_ANY))
		self.SetIcon(icon)

		self.Bind(wx.EVT_ACTIVATE, self.OnRaise)
		self.Bind(wx.EVT_CLOSE, self.OnProgramExit)

	def OnProgramExit(self, evt):
		# Ignore close events
		evt.Veto(True)

	def OnRaise(self, evt):
		# Raise the other windows when we raise this window
		if not evt.GetActive():
			return
		
		if wx.Platform != '__WXMSW__':
			if not self.config.has_key('raise') or self.config['raise'] == "All on All" or self.config['raise'] == "All on Main":
				if hasattr(self, "children"):
					for window in self.children.values():
						window.Raise()

	def Post(self, event):
		# Post an event to this window and it's children
		func = 'On' + event.__class__.__name__[:-5]	
		if hasattr(self, func):
			getattr(self, func)(event)

		for window in self.children.values():
			try:
				window.Post(event)
			except Exception, e:
				print e

	def Hide(self):
		# Hide this window and it's children
		for window in self.children.values():
			window.Hide()
		return super(winBaseMixIn, self).Hide()

	def Raise(self):
		# Raise this window and it's children
		for window in self.children.values():
			window.Raise()
		return super(winBaseMixIn, self).Raise()
	
	def SetSizeHard(self, pos):
		self.SetMinSize(pos)
		self.SetMaxSize(pos)
		self.SetSize(pos)

class winConfigMixIn(ConfigMixIn):
	def ConfigDefault(self, config=None):
		"""\
		Fill out the config with defaults (if the options are not valid or nonexistant).
		"""
		if config == None:
			config = {}

		SCREEN_X = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_X)
		SCREEN_Y = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_Y)
		
		# Is the window shown?
		try:
			if not isinstance(config['show'], bool):
				raise ValueError('Config-%s: a show value of %s is not valid' % (self, config['position']))
		except (ValueError, KeyError), e:
			if self.DefaultShow.has_key((SCREEN_X, SCREEN_Y)):
				config['show'] = self.DefaultShow[(SCREEN_X, SCREEN_Y)]
			else:
				print "Config-%s: Did not find a default show for your resolution (using 1024x768 defaults)" % (self,)
				config['show'] = self.DefaultShow[(1024, 768)]

		# Where is the window position
		try:
			if not isinstance(config['position'][0], int) or not isinstance(config['position'][1], int):
				raise ValueError('Config-%s: position %s is not valid' % (self, config['position']))
			if config['position'][0] > SCREEN_X or config['position'][1] > SCREEN_Y:
				raise ValueError('Config-%s: position %s is off the screen' % (self, config['position']))
		except (ValueError, KeyError), e:
			if self.DefaultPosition.has_key((SCREEN_X, SCREEN_Y)):
				config['position'] = self.DefaultPosition[(SCREEN_X, SCREEN_Y)]
			else:
				print "Config-%s: Did not find a default position for your resolution (using 1024x768 defaults)" % (self,)
				config['position'] = self.DefaultPosition[(1024, 768)]

		# How big is the window
		try:
			if not isinstance(config['size'][0], int) or not isinstance(config['size'][1], int):
				raise ValueError('Config-%s: size %s is not valid' % (self, config['size']))
		except (ValueError, KeyError), e:
			if self.DefaultSize.has_key((SCREEN_X, SCREEN_Y)):
				config['size'] = self.DefaultSize[(SCREEN_X, SCREEN_Y)]
			else:
				print "Config-%s: Did not find a default size for your resolution (using 1024x768 defaults)" % (self,)
				config['size'] = self.DefaultSize[(1024, 768)]

		return config

	def ConfigLoad(self, config):
		"""\
		Loads the configuration of the Window (and it's children).
		"""
		self.config = config
		self.ConfigDefault(config)

		self.SetPosition(config['position'])
		self.SetSizeHard(config['size'])
		if self.application.gui.current in (self, self.parent):
			self.Show(config['show'])

		self.ConfigDisplayUpdate(None)
		
	def ConfigUpdate(self):
		"""\
		Updates the config details using external sources.
		"""
		if self.application.gui.current in (self, self.parent):
			self.config['show'] = self.IsShown()
			self.config['position'] = self.GetPosition()
			self.config['size'] = self.GetSize()

	def ConfigDisplay(self, panel, sizer):
		"""\
		Display a config panel with all the config options.
		"""
		# Sizes we will need
		SCREEN_X = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_X)
		SCREEN_Y = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_Y)
	
		SIZER_FLAGS = wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL
		
		# The box around the items
		box = wx.StaticBox(panel, -1, self.title)
		box_sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
		sizer.Add(box_sizer, 1, SIZER_FLAGS, 5 )
	
		# Checkbox for "Show"
		show = wx.CheckBox(panel, -1, _("Show?"))
		box_sizer.Add(show, 0, SIZER_FLAGS, 5 )
		panel.Bind(wx.EVT_CHECKBOX, self.OnConfigDisplayDoShow, show)

		# Location Boxes
		location = wx.FlexGridSizer( 0, 2, 0, 0 )
		location.AddGrowableCol( 1 )

		# X Position
		x_text = wx.StaticText(panel, -1, _("X Pos"))
		location.Add( x_text, 0, SIZER_FLAGS, 5 )
		
		x_box = wx.SpinCtrl(panel, -1, "0", wx.DefaultPosition, wx.Size(50,-1), 0, 0, SCREEN_X, 0 )
		location.Add( x_box, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
		
		panel.Bind(wx.EVT_SPINCTRL, self.OnConfigDisplayX, x_box)

		# Y Position
		y_text = wx.StaticText(panel, -1, _("Y Pos"))
		location.Add( y_text, 0, SIZER_FLAGS, 5 )
		
		y_box = wx.SpinCtrl(panel, -1, "0", wx.DefaultPosition, wx.Size(50,-1), 0, 0, SCREEN_Y, 0 )
		location.Add( y_box, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )

		panel.Bind(wx.EVT_SPINCTRL, self.OnConfigDisplayY, y_box)

		# Width
		width_text = wx.StaticText(panel, -1, _("Width"))
		location.Add( width_text, 0, SIZER_FLAGS, 5 )
		
		width = wx.SpinCtrl(panel, -1, "0", wx.DefaultPosition, wx.Size(50,-1), 0, 0, SCREEN_X, 0 )
		location.Add( width, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
		
		panel.Bind(wx.EVT_SPINCTRL, self.OnConfigDisplayWidth, width)

		# Height
		height_text = wx.StaticText(panel, -1, _("Height"))
		location.Add( height_text, 0, SIZER_FLAGS, 5 )
		
		height = wx.SpinCtrl(panel, -1, "0", wx.DefaultPosition, wx.Size(50,-1), 0, 0, SCREEN_Y, 0 )
		location.Add( height, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )

		panel.Bind(wx.EVT_SPINCTRL, self.OnConfigDisplayHeight, height)

		box_sizer.Add( location, 0, SIZER_FLAGS, 5)

		self.ConfigWidgets = [show, x_box, y_box, width, height]
		self.Bind(wx.EVT_MOVE, self.OnConfigDisplayMove)
		self.Bind(wx.EVT_ACTIVATE, self.ConfigDisplayUpdate)

	def ConfigDisplayUpdate(self, evt):
		"""\
		Update the Display because it's changed externally.
		"""
		if not hasattr(self, 'ConfigWidgets'):
			return
		
		show, x_box, y_box, width, height = self.ConfigWidgets
		show.SetValue(self.config['show'])
		x_box.SetValue(self.config['position'][0])
		y_box.SetValue(self.config['position'][1])
		width.SetValue(self.config['size'][0])
		height.SetValue(self.config['size'][1])

	def OnConfigDisplayDoShow(self, evt):
		if self.application.gui.current in (self, self.parent):
			self.Show(evt.Checked())
		self.ConfigUpdate()
	
	def OnConfigDisplayX(self, evt):
		self.SetPosition(wx.Point(evt.GetInt(), -1))
		self.ConfigUpdate()

	def OnConfigDisplayY(self, evt):
		self.SetPosition(wx.Point(-1, evt.GetInt()))
		self.ConfigUpdate()
		
	def OnConfigDisplayWidth(self, evt):
		self.SetSizeHard(wx.Size(evt.GetInt(), -1))
		self.ConfigUpdate()

	def OnConfigDisplayHeight(self, evt):
		self.SetSizeHard(wx.Size(-1, evt.GetInt()))
		self.ConfigUpdate()
	
	def OnConfigDisplayMove(self, evt):
		self.ConfigUpdate()
		self.ConfigDisplayUpdate(None)

	#-----------------------------------------------------------------------------------------------

# These give a MDI interface under windows
class winMDIBase(ConfigMixIn, winBaseMixIn, wx.MDIParentFrame):
	def __init__(self, application):
		wx.MDIParentFrame.__init__(self, None, -1, 'TP: ' + self.title, wx.DefaultPosition, wx.DefaultSize, \
				wx.DEFAULT_FRAME_STYLE)
		winBaseMixIn.__init__(self, application, None)

class winMDISubBase(winConfigMixIn, winBaseMixIn, wx.MDIChildFrame):
	def __init__(self, application, parent):
		wx.MDIChildFrame.__init__(self, parent, -1, 'TP: ' + self.title, wx.DefaultPosition, wx.DefaultSize, \
				wx.TAB_TRAVERSAL|wx.RESIZE_BORDER)
		winBaseMixIn.__init__(self, application, parent)

# These give a non-MDI interface under other operating systems
class winNormalBase(ConfigMixIn, winBaseMixIn, wx.Frame):
	def __init__(self, application):
		wx.Frame.__init__(self, None, -1, 'TP: ' + self.title, wx.DefaultPosition, wx.DefaultSize, \
				wx.DEFAULT_FRAME_STYLE)
		winBaseMixIn.__init__(self, application, None)

class winNormalSubBase(winConfigMixIn, winBaseMixIn, wx.MiniFrame):
	def __init__(self, application, parent):
		wx.MiniFrame.__init__(self, parent, -1, 'TP: ' + self.title, wx.DefaultPosition, wx.DefaultSize, \
				wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR|wx.TAB_TRAVERSAL)
		winBaseMixIn.__init__(self, application, parent)

winMainBase = winNormalBase

if wx.Platform != '__WXMSW__':
	winMDIBase = winNormalBase
	winBase = winNormalSubBase
else:
	winBase = winMDISubBase

__all__ = ['winMainBase', 'winBase', 'winMDIBase', '__all__']
