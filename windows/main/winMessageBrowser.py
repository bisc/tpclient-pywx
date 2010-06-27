"""\
This module contains the Message Browser window. This window shows all message boards,
allows the player to read them and write new messages to them.
"""

# wxPython imports
import wx
import wx.html

# Local imports
from windows.winBase import winReportXRC
from windows.xrc.winMessageBrowser import winMessageBrowserBase

class winMessageBrowser(winReportXRC, winMessageBrowserBase):
	title = _("Message Browser")

	def __init__(self, application, parent):
		winMessageBrowserBase.__init__(self, parent)
		winReportXRC.__init__(self, application, parent)

		self.application = application

		# FIXME integrate it with panel Messages data
		self.html_message = """\
<html>
<body>
<center>
	<table cols=1 width="100%%">
		<tr>
			<td><b>Subject:</b> %(subject)s</td>
		</tr>
		<tr>
			<td>%(body)s</td>
		</tr>
	</table>
</center>
</body>
</html>"""

		self.application.gui.Binder(self.application.CacheClass.CacheUpdateEvent, self.OnCacheUpdate)
		self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnItemClicked, self.Boards)

	def OnCacheUpdate(self, evt):
		# Clear all
		self.Boards.DeleteAllItems()
		self.item_to_message = {}
		self.item_to_board = {}

		# Create the tree of boards and messages
		root = self.Boards.AddRoot('root')
		for bid in self.application.cache.boards.keys():
			# Create each board
			messages = self.application.cache.messages[bid]
			board_item = self.Boards.AppendItem(root, self.application.cache.boards[bid].name)
			self.item_to_board[board_item] = self.application.cache.boards[bid]

			# Append messages for each board
			for i, msg in enumerate(messages):
				message_item = self.Boards.AppendItem(board_item, msg.CurrentOrder.subject)
				self.item_to_message[message_item] = msg.CurrentOrder
			self.Boards.Expand(board_item)

		self.Boards.Expand(root)

	def OnItemClicked(self, evt):
		"""
		Called when an item in the board tree is clicked (equal to selection change event)
		if we have the single item selection style.
		"""
		selected_item = self.Boards.GetSelection()
		print("selected: %s " % selected_item)

		# Need to compare tree item ids directly, not through has_key
		# Find among boards, do nothing
		for key in self.item_to_board.keys():
			if key == selected_item:
				print("board selected, dunno what to do")

		# Find among messages, set text
		for key in self.item_to_message.keys():
			if key == selected_item:
				msg = self.item_to_message[key]
				self.Message.SetPage(self.html_message % {'subject' : msg.subject, 'body' : msg.body})
				break





