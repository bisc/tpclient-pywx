"""\
This module contains the "Waiting" window which informs
a user about his and other players' EOT request status.
Also this window allows user to request end of turn.
"""

# wxPython Imports
import wx

from extra.decorators import freeze_wrapper, onlyshown, onlyenabled

# Local Imports
from windows.winBase import winReportXRC
from windows.xrc.winWaiting import winWaitingBase

ID = 0
NAME = 1
STATUS = 2

class winWaiting(winReportXRC, winWaitingBase):
	"""\
	The Waiting window class.
	"""
	title = _("Waiting")

	def __init__(self, application, parent):
		winWaitingBase.__init__(self, parent)
		winReportXRC.__init__(self, application, parent)
		
		self.application = application
		self.waiting = []

		self.WaitingList.InsertColumn(ID, _("Player ID"), width = 100)
		self.WaitingList.InsertColumn(NAME, _("Player Name"), width = 200)
		self.WaitingList.InsertColumn(STATUS, _("Player Status"), width = 100)
		
		self.Bind(wx.EVT_SHOW, self.OnShow)
		self.application.gui.Binder(self.application.CacheClass.CacheUpdateEvent, self.OnCacheUpdate)
		self.application.gui.Binder(self.application.NetworkClass.NetworkTimeRemainingEvent, self.OnNetworkTimeRemaining)

	def OnShow(self, evt):
		self.CenterOnParent()
		self.UpdateWaitingList()

	def OnCacheUpdate(self, evt):
		self.UpdateWaitingList()

	def OnNetworkTimeRemaining(self, evt):
		"""\
		This is a handler for any async frame that carries
		information about waiting players.
		By chance, NetworkTimeRemaining frame and event are used now.
		"""
		self.waiting = evt.frame.waiting
		self.UpdateEOTStatus()
		self.UpdateWaitingList()

	@freeze_wrapper
	def UpdateWaitingList(self, evt=None):
		"""\
		Internal routine to update information in the list of players.
		"""
		self.WaitingList.DeleteAllItems()

		# Insert players' info into the list
		for pid, player in self.application.cache.players.items():
			if pid == 0:
				continue

			i = self.WaitingList.GetItemCount()

			self.WaitingList.InsertStringItem(i, "%d" % pid)
			self.WaitingList.SetStringItem(i, NAME, player.name)

			if pid in self.waiting:
				self.WaitingList.SetStringItem(i, STATUS, _("Waiting"))
			else:
				self.WaitingList.SetStringItem(i, STATUS, _("Ready!"))

			# Associate list item with player's pid
			self.WaitingList.SetItemData(i, pid)

	@freeze_wrapper
	def UpdateEOTStatus(self):
		"""\
		Internal routine to update label and button according to EOT status.
		"""
		playerID = self.application.cache.players[0].id
		requestedEOT = not playerID in self.waiting

		self.EndTurn.Enable(not requestedEOT)
		if requestedEOT:
			self.TitleText.SetLabel(_("You have requested end of turn"))
		else:
			self.TitleText.SetLabel(_("You have not requested end of turn"))

	@onlyshown
	@onlyenabled("EndTurn")
	def OnEndTurn(self, evt):
		self.application.network.Call(self.application.network.RequestEOT)
		self.UpdateEOTStatus()

	@onlyshown
	@onlyenabled("Close")
	def OnClose(self, evt):
		winReportXRC.OnClose(self, evt)
		self.application.gui.Show(self.application.gui.main)
