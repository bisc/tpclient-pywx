# This file has been automatically generated.
# Please do not edit it manually.

# Python Imports
import os.path

# wxPython imports
import wx
from wx.xrc import XRCCTRL, XmlResourceWithHandlers

# Local imports
from requirements import location

class winMessageBrowserBase:
	"""\
Unlike a normal XRC generated class, this is a not a full class but a MixIn.
Any class which uses this as a base must also inherit from a proper wx object
such as the wx.Frame class.

This is so that a the same XRC can be used for both MDI and non-MDI frames.
"""

	xrc = os.path.join(location(), "windows", "xrc", 'winMessageBrowser.xrc')

	def PreCreate(self, pre):
		""" This function is called during the class's initialization.
		
		Override it for custom setup before the window is created usually to
		set additional window styles using SetWindowStyle() and SetExtraStyle()."""
		pass

	def __init__(self, parent, *args, **kw):
		""" Pass an initialized wx.xrc.XmlResource into res """
		f = os.path.join(os.path.dirname(__file__), self.xrc)
		res = XmlResourceWithHandlers(f)		

		# Figure out what Frame class (MDI, MiniFrame, etc) is actually our base...
		bases = set()
		def findbases(klass, set):
			for base in klass.__bases__:
				set.add(base)
				findbases(base, set)
		findbases(self.__class__, bases)

		for base in bases:
			if base.__name__.endswith("Frame"):
				break
		
		# Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
		pre = getattr(wx, "Pre%s" % base.__name__)()
		if not res.LoadOnFrame(pre, parent, "winMessageBrowser"):
			raise IOError("Did not find the winMessageBrowser in the XRC file")
		self.PreCreate(pre)
		self.PostCreate(pre)

		# Define variables for the controls
		self.BoardName = XRCCTRL(self, "BoardName")
		self.Filter = XRCCTRL(self, "Filter")
		if hasattr(self, "OnFilter"):
			self.Bind(wx.EVT_BUTTON, self.OnFilter, self.Filter)

		self.Boards = XRCCTRL(self, "Boards")
		self.Message = XRCCTRL(self, "Message")
		self.New = XRCCTRL(self, "New")
		if hasattr(self, "OnNew"):
			self.Bind(wx.EVT_BUTTON, self.OnNew, self.New)

		self.Goto = XRCCTRL(self, "Goto")
		if hasattr(self, "OnGoto"):
			self.Bind(wx.EVT_BUTTON, self.OnGoto, self.Goto)

		self.Delete = XRCCTRL(self, "Delete")
		if hasattr(self, "OnDelete"):
			self.Bind(wx.EVT_BUTTON, self.OnDelete, self.Delete)



def strings():
	pass
	_("Boards");
	_("Board Name");
	_("Filter messages using this message as a template.");
	_("F");
	_("Boards avaliable on the server.");
	_("<html>\n<body>\n<center>\n        <table cols=1 width=\"100%\" background=\"\">\n                <tr>\n                        <td><b>Subject:</b> Subject goes here!</td>\n                </tr>\n                <tr>\n                        <td>A really cool message body should go here.</td>\n                </tr>\n        </table>\n</center>\n</body>\n</html>");
	_("New");
	_("Create a new message on the current board.");
	_("Goto");
	_("Goto objects referenced by this message.");
	_("Delete");
	_("Delete this message.");
	_("Message Browser");
