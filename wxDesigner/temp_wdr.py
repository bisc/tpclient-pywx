#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: temp.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxWindows' modules
from wxPython.wx import *

# Window functions

MESSAGE_FILTER = 10000
MESSAGE_TITLE = 10001
MESSAGE_ID = 10002
MESSAGE_HTML = 10003
MESSAGE_PREV = 10004
MESSAGE_GOTO = 10005
MESSAGE_NEXT = 10006
MESSAGE_LINE = 10007
MESSAGE_NEW = 10008
MESSAGE_DEL = 10009

def panelMessage( parent, call_fit = true, set_sizer = true ):
    item0 = wxFlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    item0.AddGrowableRow( 1 )
    
    item1 = wxFlexGridSizer( 0, 3, 0, 0 )
    item1.AddGrowableCol( 0 )
    item1.AddGrowableCol( 1 )
    item1.AddGrowableCol( 2 )
    
    item2 = wxCheckBox( parent, MESSAGE_FILTER, "Filter", wxDefaultPosition, wxDefaultSize, 0 )
    item1.AddWindow( item2, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticText( parent, MESSAGE_TITLE, "Title", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item1.AddWindow( item3, 0, wxALIGN_CENTRE|wxALL, 5 )

    item4 = wxStaticText( parent, MESSAGE_ID, "# of #", wxDefaultPosition, wxDefaultSize, 0 )
    item1.AddWindow( item4, 0, wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item1, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item5 = wxFlexGridSizer( 0, 2, 0, 0 )
    item5.AddGrowableCol( 0 )
    item5.AddGrowableRow( 0 )
    
    item6 = wxScrolledWindow( parent, MESSAGE_HTML, wxDefaultPosition, wxSize(200,160), wxHSCROLL|wxVSCROLL )
    item6.SetScrollbars( 10, 10, 20, 100, 0, 0 )
    item5.AddWindow( item6, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    item7 = wxBoxSizer( wxVERTICAL )
    
    item8 = wxButton( parent, MESSAGE_PREV, "Prev", wxDefaultPosition, wxDefaultSize, 0 )
    item7.AddWindow( item8, 0, wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item9 = wxButton( parent, MESSAGE_GOTO, "Goto", wxDefaultPosition, wxDefaultSize, 0 )
    item7.AddWindow( item9, 0, wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxButton( parent, MESSAGE_NEXT, "Next", wxDefaultPosition, wxDefaultSize, 0 )
    item7.AddWindow( item10, 0, wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxStaticLine( parent, MESSAGE_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item11.Enable(false)
    item7.AddWindow( item11, 0, wxALIGN_CENTRE|wxALL, 5 )

    item12 = wxButton( parent, MESSAGE_NEW, "New", wxDefaultPosition, wxDefaultSize, 0 )
    item7.AddWindow( item12, 0, wxALIGN_CENTRE|wxALL, 5 )

    item13 = wxButton( parent, MESSAGE_DEL, "Delete", wxDefaultPosition, wxDefaultSize, 0 )
    item7.AddWindow( item13, 0, wxALIGN_CENTRE|wxALL, 5 )

    item5.AddSizer( item7, 0, wxGROW|wxALIGN_RIGHT|wxALL, 5 )

    item0.AddSizer( item5, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ORDER_LIST = 10010
ORDER_LINE = 10011
ORDER_NEW = 10012
ORDER_DELETE = 10013
ORDER_EDIT = 10014

def panelOrders( parent, call_fit = true, set_sizer = true ):
    item0 = wxFlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    item0.AddGrowableRow( 0 )
    item0.AddGrowableRow( 4 )
    
    item1 = wxListCtrl( parent, ORDER_LIST, wxDefaultPosition, wxSize(160,120), wxLC_REPORT|wxSUNKEN_BORDER )
    item0.AddWindow( item1, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticLine( parent, ORDER_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    item3 = wxFlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wxButton( parent, ORDER_NEW, "New Order", wxDefaultPosition, wxDefaultSize, 0 )
    item3.AddWindow( item4, 0, wxALIGN_CENTRE|wxALL, 5 )

    item5 = wxButton( parent, ORDER_DELETE, "Delete Order", wxDefaultPosition, wxDefaultSize, 0 )
    item3.AddWindow( item5, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item3, 0, wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticLine( parent, ORDER_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item6, 0, wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxFlexGridSizer( 0, 2, 0, 0 )
    
    item8 = parent.FindWindowById( ORDER_EDIT )
    item7.AddWindow( item8, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item7, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

OBJ_PICT = 10015
OBJ_LINE = 10016
OBJ_ICON = 10017
OBJ_NAME = 10018
OBJ_PANEL = 10019
OBJ_NEXT = 10020
OBJ_PREV = 10021

def panelObject( parent, call_fit = true, set_sizer = true ):
    item0 = wxFlexGridSizer( 1, 0, 0, 0 )
    item0.AddGrowableCol( 2 )
    item0.AddGrowableRow( 0 )
    
    item1 = wxStaticText( parent, OBJ_PICT, "No image", wxDefaultPosition, wxSize(128,128) )
    item0.AddWindow( item1, 0, wxALIGN_CENTRE|wxALL, 5 )

    item2 = wxStaticLine( parent, OBJ_LINE, wxDefaultPosition, wxSize(-1,20), wxLI_VERTICAL )
    item0.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    item3 = wxFlexGridSizer( 0, 1, 0, 0 )
    item3.AddGrowableCol( 0 )
    item3.AddGrowableRow( 2 )
    
    item4 = wxFlexGridSizer( 1, 0, 0, 0 )
    item4.AddGrowableCol( 1 )
    item4.AddGrowableRow( 0 )
    
    item5 = wxStaticText( parent, OBJ_ICON, "No image", wxDefaultPosition, wxSize(16,16) )
    item4.AddWindow( item5, 0, wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticText( parent, OBJ_NAME, "Object Name", wxDefaultPosition, wxDefaultSize, 0 )
    item4.AddWindow( item6, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3.AddSizer( item4, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item7 = wxPanel( parent, OBJ_PANEL, wxDefaultPosition, wxSize(150,80), 0 )
    item3.AddWindow( item7, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item3, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    item8 = wxFlexGridSizer( 0, 1, 0, 0 )
    
    item9 = wxButton( parent, OBJ_NEXT, "NEXT", wxDefaultPosition, wxDefaultSize, 0 )
    item8.AddWindow( item9, 0, wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxStaticLine( parent, OBJ_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item8.AddWindow( item10, 0, wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxButton( parent, OBJ_PREV, "PREV", wxDefaultPosition, wxDefaultSize, 0 )
    item8.AddWindow( item11, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item8, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

OBJ_SHIP_FUELSLD = 10022
OBJ_SHIP_FUEL = 10023
OBJ_SHIP_CARGOSLD = 10024
OBJ_SHIP_CARGO = 10025
OBJ_SHIP_CON = 10026

def panelObject_Ship( parent, call_fit = true, set_sizer = true ):
    item0 = wxFlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    item0.AddGrowableRow( 0 )
    item0.AddGrowableRow( 1 )
    item0.AddGrowableRow( 2 )
    
    item1 = wxFlexGridSizer( 0, 2, 0, 0 )
    item1.AddGrowableCol( 0 )
    item1.AddGrowableRow( 0 )
    item1.AddGrowableRow( 1 )
    
    item2 = wxSlider( parent, OBJ_SHIP_FUELSLD, 0, 0, 100, wxDefaultPosition, wxSize(100,10), wxSL_HORIZONTAL )
    item2.SetBackgroundColour( wxRED )
    item1.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    item3 = wxStaticText( parent, OBJ_SHIP_FUEL, "# of # fu", wxDefaultPosition, wxDefaultSize, 0 )
    item3.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item1.AddWindow( item3, 0, wxALIGN_CENTRE|wxALL, 5 )

    item4 = wxGauge( parent, OBJ_SHIP_CARGOSLD, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item1.AddWindow( item4, 0, wxALIGN_CENTRE|wxALL, 5 )

    item5 = wxStaticText( parent, OBJ_SHIP_CARGO, "# of # kt", wxDefaultPosition, wxDefaultSize, 0 )
    item5.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item1.AddWindow( item5, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item6 = wxListCtrl( parent, OBJ_SHIP_CON, wxDefaultPosition, wxSize(160,120), wxLC_REPORT|wxSUNKEN_BORDER )
    item6.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item0.AddWindow( item6, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

OBJ_PLT_TEXT = 10027
OBJ_PLT_POP = 10028
OBJ_PLT_LINE = 10029
OBJ_PLT_HAB = 10030
OBJ_PLT_GRAV = 10031
OBJ_PLT_RAD = 10032
OBJ_PLT_TEMP = 10033
OBJ_PLT_FACT = 10034
OBJ_PLT_MINE = 10035
OBJ_PLT_DEFNO = 10036
OBJ_PLT_SCAN = 10037
OBJ_PLT_DEF = 10038

def panelObject_Planet( parent, call_fit = true, set_sizer = true ):
    item0 = wxFlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wxFlexGridSizer( 1, 0, 0, 0 )
    item1.AddGrowableCol( 1 )
    
    item2 = wxStaticText( parent, OBJ_PLT_TEXT, "Population", wxDefaultPosition, wxDefaultSize, 0 )
    item2.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item1.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    item3 = wxGauge( parent, OBJ_PLT_POP, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item3.SetBackgroundColour( wxWHITE )
    item1.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4 = wxStaticLine( parent, OBJ_PLT_LINE, wxDefaultPosition, wxSize(-1,10), wxLI_VERTICAL )
    item1.AddWindow( item4, 0, wxALIGN_CENTRE|wxALL, 5 )

    item5 = wxStaticText( parent, OBJ_PLT_TEXT, "Hab", wxDefaultPosition, wxDefaultSize, 0 )
    item5.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item1.AddWindow( item5, 0, wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticText( parent, OBJ_PLT_HAB, "10%", wxDefaultPosition, wxDefaultSize, 0 )
    item6.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item1.AddWindow( item6, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item7 = wxStaticLine( parent, OBJ_PLT_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item7, 0, wxALIGN_CENTRE|wxALL, 5 )

    item8 = wxFlexGridSizer( 0, 2, 0, 0 )
    
    item9 = wxFlexGridSizer( 0, 2, 0, 0 )
    
    item10 = wxStaticText( parent, OBJ_PLT_TEXT, "Gravity", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item10.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item9.AddWindow( item10, 0, wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxGauge( parent, OBJ_PLT_GRAV, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item11.SetBackgroundColour( wxBLUE )
    item9.AddWindow( item11, 0, wxALIGN_CENTRE|wxALL, 5 )

    item12 = wxStaticText( parent, OBJ_PLT_TEXT, "Radiation", wxDefaultPosition, wxDefaultSize, 0 )
    item12.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item9.AddWindow( item12, 0, wxALIGN_CENTRE|wxALL, 5 )

    item13 = wxGauge( parent, OBJ_PLT_RAD, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item13.SetBackgroundColour( wxRED )
    item9.AddWindow( item13, 0, wxALIGN_CENTRE|wxALL, 5 )

    item14 = wxStaticText( parent, OBJ_PLT_TEXT, "Temperture", wxDefaultPosition, wxDefaultSize, 0 )
    item14.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item9.AddWindow( item14, 0, wxALIGN_CENTRE|wxALL, 5 )

    item15 = wxGauge( parent, OBJ_PLT_TEMP, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item15.SetBackgroundColour( wxGREEN )
    item9.AddWindow( item15, 0, wxALIGN_CENTRE|wxALL, 5 )

    item8.AddSizer( item9, 0, wxALIGN_CENTRE|wxALL, 5 )

    item16 = wxFlexGridSizer( 0, 2, 0, 0 )
    
    item17 = wxStaticText( parent, OBJ_PLT_TEXT, "Factories", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item17.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item16.AddWindow( item17, 0, wxALIGN_CENTRE|wxALL, 5 )

    item18 = wxGauge( parent, OBJ_PLT_FACT, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item16.AddWindow( item18, 0, wxALIGN_CENTRE|wxALL, 5 )

    item19 = wxStaticText( parent, OBJ_PLT_TEXT, "Mines", wxDefaultPosition, wxDefaultSize, 0 )
    item19.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item16.AddWindow( item19, 0, wxALIGN_CENTRE|wxALL, 5 )

    item20 = wxGauge( parent, OBJ_PLT_MINE, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item16.AddWindow( item20, 0, wxALIGN_CENTRE|wxALL, 5 )

    item21 = wxStaticText( parent, OBJ_PLT_TEXT, "Defense", wxDefaultPosition, wxDefaultSize, 0 )
    item21.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item16.AddWindow( item21, 0, wxALIGN_CENTRE|wxALL, 5 )

    item22 = wxGauge( parent, OBJ_PLT_DEFNO, 100, wxDefaultPosition, wxSize(100,10), 0 )
    item16.AddWindow( item22, 0, wxALIGN_CENTRE|wxALL, 5 )

    item8.AddSizer( item16, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item8, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item23 = wxStaticLine( parent, OBJ_PLT_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item23, 0, wxALIGN_CENTRE|wxALL, 5 )

    item24 = wxFlexGridSizer( 0, 2, 0, 0 )
    
    item25 = wxStaticText( parent, OBJ_PLT_TEXT, "Scanner:", wxDefaultPosition, wxDefaultSize, 0 )
    item25.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item24.AddWindow( item25, 0, wxALIGN_CENTRE|wxALL, 5 )

    item26 = wxStaticText( parent, OBJ_PLT_SCAN, "Large Scanner Array 600", wxDefaultPosition, wxDefaultSize, 0 )
    item26.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item24.AddWindow( item26, 0, wxALIGN_CENTRE|wxALL, 5 )

    item27 = wxStaticText( parent, OBJ_PLT_TEXT, "Defense Type:", wxDefaultPosition, wxDefaultSize, 0 )
    item27.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item24.AddWindow( item27, 0, wxALIGN_CENTRE|wxALL, 5 )

    item28 = wxStaticText( parent, OBJ_PLT_DEF, "Planetry Shield", wxDefaultPosition, wxDefaultSize, 0 )
    item28.SetFont( wxFont( 10, wxSWISS, wxNORMAL, wxNORMAL ) )
    item24.AddWindow( item28, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item24, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 10039
ID_HOST = 10040
ID_USERNAME = 10041
ID_PASSWORD = 10042
ID_OK = 10043
ID_CANCEL = 10044

def panelConnect( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxBoxSizer( wxHORIZONTAL )
    
    item2 = wxStaticText( parent, ID_TEXT, "Connect to a Thousand Parsec Server", wxDefaultPosition, wxDefaultSize, 0 )
    item2.SetFont( wxFont( 16, wxROMAN, wxNORMAL, wxBOLD ) )
    item1.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 0, wxALIGN_CENTRE|wxALL, 5 )

    item3 = wxFlexGridSizer( 0, 2, 0, 0 )
    
    item4 = wxStaticText( parent, ID_TEXT, "Host", wxDefaultPosition, wxDefaultSize, 0 )
    item3.AddWindow( item4, 0, wxALIGN_CENTRE|wxALL, 5 )

    item5 = wxComboBox( parent, ID_HOST, "", wxDefaultPosition, wxSize(200,-1), 
        ["code-bear.dyndns.org:6923"] , wxCB_DROPDOWN )
    item3.AddWindow( item5, 0, wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticText( parent, ID_TEXT, "Username", wxDefaultPosition, wxDefaultSize, 0 )
    item3.AddWindow( item6, 0, wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxComboBox( parent, ID_USERNAME, "", wxDefaultPosition, wxSize(200,-1), [], wxCB_DROPDOWN )
    item3.AddWindow( item7, 0, wxALIGN_CENTRE|wxALL, 5 )

    item8 = wxStaticText( parent, ID_TEXT, "Password", wxDefaultPosition, wxDefaultSize, 0 )
    item3.AddWindow( item8, 0, wxALIGN_CENTRE|wxALL, 5 )

    item9 = wxTextCtrl( parent, ID_PASSWORD, "", wxDefaultPosition, wxSize(200,-1), wxTE_PASSWORD )
    item3.AddWindow( item9, 0, wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxBoxSizer( wxHORIZONTAL )
    
    item3.AddSizer( item10, 0, wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxBoxSizer( wxHORIZONTAL )
    
    item12 = wxButton( parent, ID_OK, "OK", wxDefaultPosition, wxDefaultSize, 0 )
    item11.AddWindow( item12, 0, wxALIGN_CENTRE|wxALL, 5 )

    item13 = wxButton( parent, ID_CANCEL, "Cancel", wxDefaultPosition, wxDefaultSize, 0 )
    item11.AddWindow( item13, 0, wxALIGN_CENTRE|wxALL, 5 )

    item3.AddSizer( item11, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item3, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

ID_NEW_GAME = 10045
ID_NEW_RACE = 10046
ID_NEW = 10047
ID_MENU = 10048
ID_OPEN = 10049
ID_SAVE = 10050
ID_CLOSE = 10051
ID_REVERT = 10052
ID_LOADTURN = 10053
ID_GENTURN = 10054
ID_EXIT = 10055
ID_FILE = 10056
ID_STAT_EAAG = 10057
ID_STAT_SYSTEM = 10058
ID_STAT_PLANET = 10059
ID_STAT_FLEET = 10060
ID_STAT_BATTLE = 10061
ID_STATS = 10062
ID_WIN_STARMAP = 10063
ID_WIN = 10064
ID_HELP = 10065

def MainMenu():
    item0 = wxMenuBar()
    
    item1 = wxMenu( wxMENU_TEAROFF )
    
    item2 = wxMenu()
    item2.Append( ID_NEW_GAME, "Game", "Start a new Game" )
    item2.Append( ID_NEW_RACE, "Race", "Start a new Race" )
    item1.AppendMenu( ID_NEW, "New", item2 )

    item1.AppendSeparator()
    item1.Append( ID_OPEN, "Open Game\tCtrl-O", "Open a diffrent Game" )
    item1.Append( ID_SAVE, "Save Game\tCtrl-S", "Save this Game" )
    item1.Append( ID_CLOSE, "Close Game\tCtrl-C", "Close this Game" )
    item1.AppendSeparator()
    item1.Append( ID_REVERT, "Revert Game", "Forget non-saved changes" )
    item1.AppendSeparator()
    item1.Append( ID_LOADTURN, "Load Turn File\tCtrl-L", "Load a turn file" )
    item1.Append( ID_GENTURN, "Generate Turn File\tCtrl-T", "Generate a turn file" )
    item1.AppendSeparator()
    item1.Append( ID_EXIT, "Exit", "Exit" )
    item0.Append( item1, "File" )
    
    item3 = wxMenu()
    item3.Append( ID_STAT_EAAG, "Empire at a Glance", "" )
    item3.AppendSeparator()
    item3.Append( ID_STAT_SYSTEM, "Systems", "" )
    item3.Append( ID_STAT_PLANET, "Planets", "" )
    item3.Append( ID_STAT_FLEET, "Fleets", "" )
    item3.AppendSeparator()
    item3.Append( ID_STAT_BATTLE, "Battles", "" )
    item0.Append( item3, "Statistics" )
    
    item4 = wxMenu()
    item4.Append( ID_WIN_STARMAP, "TP: Starmap", "", true )
    item0.Append( item4, "Windows" )
    
    item5 = wxMenu()
    item0.Append( item5, "Help" )
    
    return item0

# Toolbar functions

# Bitmap functions


# End of generated file
