"""\
This module contains the Message Browser window. This window shows all message boards,
allows the player to read them and write new messages to them.
"""

# wxPython imports
import wx
import wx.gizmos

# Local imports
from windows.winBase import winReportXRC
from windows.xrc.winMessageBrowser import winMessageBrowserBase

class winMessageBrowser(winReportXRC, winMessageBrowserBase):
	title = _("Message Browser")

	def __init__(self, application, parent):
		winMessageBrowserBase.__init__(self, parent)
		winReportXRC.__init__(self, application, parent)

		self.application = application

		self.application.gui.Binder(self.application.CacheClass.CacheUpdateEvent, self.OnCacheUpdate)

	def OnCacheUpdate(self, evt):
		print("____________________________")
		print("1. %s" % self.application.cache.boards)
		print("2. %s" % self.application.cache.boards[0])
		print("3. %s" % self.application.cache.messages)
		print("4. %s" % self.application.cache.messages[0])

		self.Boards.DeleteAllItems()
		self.item_to_message = {}
		self.item_to_board = {}
		
		root = self.Boards.AddRoot('root')
		for bid in self.application.cache.boards.keys():
			messages = self.application.cache.messages[bid]
			board_item = self.Boards.AppendItem(root, 'board%s' % bid)
			self.item_to_board[board_item] = self.application.cache.boards[bid]
			for i, msg in enumerate(messages):
				message_item = self.Boards.AppendItem(board_item, msg.CurrentOrder.subject)
				self.item_to_message[message_item] = msg.CurrentOrder
			self.Boards.Expand(board_item)

		self.Boards.Expand(root)



