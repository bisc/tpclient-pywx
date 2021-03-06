# This file has been automatically generated.
# Please do not edit it manually.

# Python Imports
import os.path

# wxPython imports
import wx
from wx.xrc import XRCCTRL, XmlResourceWithHandlers

# Local imports
from requirements import location

class infoPosition3DBase(wx.Panel):
	xrc = os.path.join(location(), "windows", "xrc", 'infoPosition3D.xrc')

	def PreCreate(self, pre):
		""" This function is called during the class's initialization.
		
		Override it for custom setup before the window is created usually to
		set additional window styles using SetWindowStyle() and SetExtraStyle()."""
		pass

	def __init__(self, parent, *args, **kw):
		""" Pass an initialized wx.xrc.XmlResource into res """
		f = os.path.join(os.path.dirname(__file__), self.xrc)
		res = XmlResourceWithHandlers(f)		

		# Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
		pre = wx.PrePanel()
		if not res.LoadOnPanel(pre, parent, "infoPosition3D"):
			raise IOError("Did not find the infoPosition3D in the XRC file")
		self.PreCreate(pre)
		self.PostCreate(pre)

		# Define variables for the controls
		self.PositionLabel = XRCCTRL(self, "PositionLabel")
		self.GotoPosition = XRCCTRL(self, "GotoPosition")
		if hasattr(self, "OnGotoPosition"):
			self.Bind(wx.EVT_BUTTON, self.OnGotoPosition, self.GotoPosition)



def strings():
	pass
	_("(0, 0, 0)");
	_("Zoom To Here");
