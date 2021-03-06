"""\
This module contains the config window.
"""

# wxPython Imports
import wx
import wx.lib.anchors

# Local Imports
from winBase import winBase

# Shows messages from the game system to the player.
class winConfig(winBase):
	title = _("Config")
	
	def __init__(self, application, windows):
		winBase.__init__(self, application)

		self.application = application

		# The first panel is the current window, we then go through all the other windows.
		main = wx.Panel(self, -1)
		
		base = wx.BoxSizer(wx.VERTICAL)
		notebook = wx.Notebook(main, -1)
		base.Add(notebook, 1, wx.EXPAND)
		# Now add each window which can be configured
		for window in windows:
			panel = wx.Panel(notebook, -1)
			sizer = wx.BoxSizer(wx.HORIZONTAL)
		
			window.ConfigDisplay(panel, sizer)

			panel.SetAutoLayout(True)
			panel.SetSizer(sizer)

			if len(sizer.GetChildren()) == 0:
				continue
			notebook.AddPage(panel, window.title)

		# FIXME: This is only temporary till they fix this on mac!
		if wx.Platform != "__WXMAC__":
			butt = wx.StdDialogButtonSizer()
		else:
			butt = wx.BoxSizer(wx.HORIZONTAL)
		base.Add(butt, 0, wx.ALIGN_RIGHT)

		# Buttons for saving/reverting
		save = wx.Button(main, wx.ID_SAVE)
		self.Bind(wx.EVT_BUTTON, self.OnConfigSave, save)
		
		revert = wx.Button(main, wx.ID_REVERT_TO_SAVED)
		self.Bind(wx.EVT_BUTTON, self.OnConfigRevert, revert)
		revert.SetDefault()
		
		if wx.Platform != "__WXMAC__":
			butt.AddButton(save), butt.SetCancelButton(revert)
			butt.Realize()
		else:
			butt.Add(save, 0, wx.ALIGN_RIGHT)
			butt.Add(revert, 0, wx.ALIGN_RIGHT)
	
		main.SetAutoLayout(True)
		main.SetSizer(base)
		
		base.SetSizeHints(self)

		self.notebook = notebook
		self.Bind(wx.EVT_SHOW, self.OnShow)

	def OnShow(self, evt):
		self.CenterOnParent(wx.BOTH)
		self.MakeModal(evt.GetShow())

		for page in xrange(self.notebook.GetPageCount()):
			if self.notebook.GetPageText(page) == self.application.gui.current.title:
				self.notebook.SetSelection(page)
				break

	def OnConfigSave(self, evt):
		self.application.ConfigSave()
		self.Hide()

	def OnConfigRevert(self, evt):
		self.application.ConfigLoad()
		self.Hide()

	def OnClose(self, evt):
		self.OnConfigRevert(evt)
	
	# Config Functions -----------------------------------------------------------------------------
	def ConfigDefault(self, config=None):
		"""\
		Fill out the config with defaults (if the options are not valid or nonexistant).
		"""
		return {}

	def ConfigSave(self):
		"""\
		Returns the configuration of the Window (and it's children).
		"""
		return {}
	
	def ConfigLoad(self, config={}):
		"""\
		Loads the configuration of the Window (and it's children).
		"""
		pass

	def ConfigUpdate(self):
		"""\
		Updates the config details using external sources.
		"""
		pass

	def ConfigDisplay(self, panel, sizer):
		"""\
		Display a config panel with all the config options.
		"""
		pass

	def ConfigDisplayUpdate(self, evt):
		"""\
		Update the Display because it's changed externally.
		"""
		pass
