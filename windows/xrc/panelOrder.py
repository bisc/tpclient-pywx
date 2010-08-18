# This file has been automatically generated.
# Please do not edit it manually.

# Python Imports
import os.path

# wxPython imports
import wx
from wx.xrc import XRCCTRL, XmlResourceWithHandlers

# Local imports
from requirements import location

class panelOrderBase(wx.Panel):
	xrc = os.path.join(location(), "windows", "xrc", 'panelOrder.xrc')

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
		if not res.LoadOnPanel(pre, parent, "panelOrder"):
			raise IOError("Did not find the panelOrder in the XRC file")
		self.PreCreate(pre)
		self.PostCreate(pre)

		# Define variables for the controls
		self.Master = XRCCTRL(self, "Master")
		self.Queues = XRCCTRL(self, "Queues")
		if hasattr(self, "OnQueues"):
			self.Queues.Bind(wx.EVT_CHOICE, self.OnQueues)

		self.OrderNew = XRCCTRL(self, "OrderNew")
		if hasattr(self, "OnOrderNew"):
			self.Bind(wx.EVT_BUTTON, self.OnOrderNew, self.OrderNew)

		self.Orders = XRCCTRL(self, "Orders")
		self.DetailsParentPanel = XRCCTRL(self, "DetailsParentPanel")
		self.ArgumentLine = XRCCTRL(self, "ArgumentLine")
		self.DetailsBorderPanel = XRCCTRL(self, "DetailsBorderPanel")
		self.DetailsPanel = XRCCTRL(self, "DetailsPanel")
		self.ButtonsPanel = XRCCTRL(self, "ButtonsPanel")
		self.Message = XRCCTRL(self, "Message")
		self.Save = XRCCTRL(self, "Save")
		if hasattr(self, "OnSave"):
			self.Bind(wx.EVT_BUTTON, self.OnSave, self.Save)

		self.Revert = XRCCTRL(self, "Revert")
		if hasattr(self, "OnRevert"):
			self.Bind(wx.EVT_BUTTON, self.OnRevert, self.Revert)

		self.Delete = XRCCTRL(self, "Delete")
		if hasattr(self, "OnDelete"):
			self.Bind(wx.EVT_BUTTON, self.OnDelete, self.Delete)



def strings():
	pass
	_("&New Order");
	_("Insert new order.");
	_("&Save");
	_("&Revert");
	_("&Delete");
	_("Delete the currently selected order(s)");
