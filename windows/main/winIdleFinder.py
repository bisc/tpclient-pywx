"""\
This module contains the idle objects finder display.
"""

# wxPython imports
import wx
import wx.gizmos
from wx import *
import wx.lib.anchors

# Local imports
from windows.winBase import winReportXRC, ShiftMixIn
from windows.xrc.winIdleFinder import IdleFinderBase
# Shows messages from the game system to the player.
class winIdleFinder(winReportXRC, IdleFinderBase):
	title = _("Objects Without Orders")
	
	def __init__(self, application, parent):
		IdleFinderBase.__init__(self, parent)
		winReportXRC.__init__(self, application, parent)
		
		self.application = application

		# Create a panel for the current window.
		self.idlelist.InsertColumn(0, "Item ID", width = 100)
		self.idlelist.InsertColumn(1, "Item Name", width = 200)
		self.idlelist.InsertColumn(2, "Item Type", width = 100)

		self.Bind(wx.EVT_SHOW, self.OnShow)
		self.Bind(wx.EVT_ACTIVATE, self.OnShow)

	def OnShow(self, evt):
		"""\
		Runs when the window is shown.
		"""
		self.idlelist.DeleteAllItems()
		universe = self.application.cache.objects.keys()
		for object in universe:
			if hasattr(self.application.cache.objects[object], "owner"):
				if self.application.cache.objects[object].owner == self.application.cache.players[0].id:
					if object in self.application.cache.orders.keys():
						if self.application.cache.orders[object] == []:
							self.idlelist.InsertStringItem(0, "%d" % object)
							self.idlelist.SetStringItem(self.idlelist.FindItem(-1, "%d" % object), 1, self.application.cache.objects[object].name)
							if self.application.cache.objects[object].subtype == 0:
								self.idlelist.SetStringItem(self.idlelist.FindItem(-1, "%d" % object), 2, "Universe")
							elif self.application.cache.objects[object].subtype == 1:
								self.idlelist.SetStringItem(self.idlelist.FindItem(-1, "%d" % object), 2, "Galaxy")
							elif self.application.cache.objects[object].subtype == 2:
								self.idlelist.SetStringItem(self.idlelist.FindItem(-1, "%d" % object), 2, "System")
							elif self.application.cache.objects[object].subtype == 3:
								self.idlelist.SetStringItem(self.idlelist.FindItem(-1, "%d" % object), 2, "Planet")
							elif self.application.cache.objects[object].subtype == 4:
								self.idlelist.SetStringItem(self.idlelist.FindItem(-1, "%d" % object), 2, "Fleet")

	def OnClose(self, evt):
		"""\
		Runs when the window is closed.
		"""
		self.Hide()
	
	# Config Functions (required by winBase.py) -----------------------------------------------------------------------------
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