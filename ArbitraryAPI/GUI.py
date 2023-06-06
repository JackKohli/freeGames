import PySimpleGUI as sg
import ArbitraryAPI as api

nG = []
oG = []

def updateGames():
    newGames, oldGames = api.filterGames(api.getGames())
    global nG, oG
    nG = newGames
    oG = oldGames

def gameNames(gamelist):
    namelist = []
    for game in gamelist:
        namelist.append(game.title)
    return namelist

sg.theme('DarkAmber')
updateGames()
layout_l = [[sg.Text('New')],
            [sg.Listbox(values = gameNames(nG), size=(100,10),enable_events = True, k='_NEWGAMES_')],#newgames list box
            [sg.Text('Older')],
            [sg.Listbox(values = gameNames(oG), size=(100,10),enable_events = True, k='_OLDGAMES_')],#older games list box
            [sg.Button('Update')]]#update button
layout_r = [[sg.Text('Details')],
            [sg.Multiline(size = (100,24), k = '_GAMEDETAILS_' + sg.WRITE_ONLY_KEY, do_not_clear = False, disabled = True)],#box for displaying game details
            [sg.Button('Close')]]

Layout = [[sg.Col(layout_l), sg.Col(layout_r)]]

window = sg.Window('Free Game Giveaways', Layout)

while True:
    event, values = window.read()
    if event == 'Update':
        window['_NEWGAMES_'].update(gameNames(nG))
        window['_OLDGAMES_'].update(gameNames(oG))
    if event == '_NEWGAMES_':
        for game in nG:
            if values[event][0] == game.title:
                window['_GAMEDETAILS___WRITE ONLY__'].update(value = 'Title: '+game.title+'\n'+'Start Date: '+game.start+'\n'+ 'End Date: '+game.end+'\n'+ 'Link: ' + game.link)
                break
    elif event == '_OLDGAMES_':
        for game in oG:
            if values[event][0] == game.title:
                window['_GAMEDETAILS___WRITE ONLY__'].update(value = 'Title: '+game.title+'\n'+'Start Date: '+game.start+'\n'+ 'End Date: '+game.end+'\n'+ 'Link: ' + game.link)
                break
    if event in (sg.WIN_CLOSED, 'Close'):
        break
window.close()