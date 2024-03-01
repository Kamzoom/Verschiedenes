
import time
from tkinter import *

fenster = Tk()
fenster.wm_title("Stoppuhr")

uhr = Label(master=fenster, font=('Arial', 70), fg='white', width=10, height=3)
uhr.pack()

# Variablen zur Steuerung der Stoppuhr
laufend = False
startzeit = 0
laufzeit = 0

def start():
    global laufend, startzeit, laufzeit
    if not laufend:
        laufend = True
        startzeit = int(time.time()) - laufzeit
        tick()

def stop():
    global laufend, laufzeit
    if laufend:
        laufend = False
        laufzeit = int(time.time()) - startzeit


def refresh():
    global laufend, startzeit, laufzeit
    if laufend == True:
        laufend = True;
    if laufend == False:
        startzeit = 0
        laufzeit = 0
    uhr.config(text=f'{laufzeit // 3600}:{(laufzeit // 60) % 60}:{laufzeit % 60}')

startButton = Button(fenster, height=3, width=10, text="Start",bg="blue", command=start)
startButton.pack()
stopButton = Button(fenster, height=3, width=10, text="Stop", command=stop)
stopButton.pack()

restartButton = Button(fenster, height=3, width=10, text="Refresh", command=refresh)
restartButton.pack()

def tick():
    global startzeit, laufzeit
    if laufend:
        # Aktualisiere die laufende Zeit
        laufzeit = int(time.time()) - startzeit
        uhr.config(text=f'{laufzeit // 3600}:{(laufzeit // 60) % 60}:{laufzeit % 60}')
        uhr.after(200, tick)
    elif laufzeit > 0:
        # Zeige die gestoppte Zeit
        uhr.config(text=f'{laufzeit // 3600}:{(laufzeit // 60) % 60}:{laufzeit % 60}')

tick()
fenster.mainloop()

# In dieser Version werden folgende Funktionalitäten bereitgestellt:
#
# - **Start**: Beim Klicken auf "Start" beginnt die Stoppuhr, die vergangene Zeit zu messen.
# - **Stop**: Beim Klicken auf "Stop" wird die Messung angehalten, und die vergangene Zeit bleibt sichtbar.
# - **Anzeige der Zeit**: Die Zeit wird im Format Stunden:Minuten:Sekunden angezeigt.
#   **Refresh setzt alle Werte auf Null
