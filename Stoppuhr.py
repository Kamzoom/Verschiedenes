import time
import tkinter as tk

fenster = tk.Tk()
fenster.wm_title("Stoppuhr")
# Setze die Fenstergröße auf 800x500 Pixel
fenster.geometry("400x390")

# Verhindere das Ändern der Fenstergröße
# Setze sowohl die Breite (width) als auch die Höhe (height) auf False
fenster.resizable(width=False, height=False)

uhr = tk.Label(master=fenster, font=('Arial', 70), fg='white', width=10, height=3)
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
        startzeit = 0
        laufzeit = 0
        startzeit = int(time.time()) - laufzeit
        tick()
    if laufend == False:
        startzeit = 0
        laufzeit = 0
    uhr.config(text=f'{laufzeit // 3600}:{(laufzeit // 60) % 60}:{laufzeit % 60}')



startButton = tk.Button(fenster, height=3, width=11, text="Start", bg="blue", command=start)
startButton.pack(side=tk.LEFT)

stopButton = tk.Button(fenster, height=3, width=11, text="Stop", command=stop)
stopButton.pack(side=tk.LEFT)

restartButton = tk.Button(fenster, height=3, width=11, text="Refresh", command=refresh)
restartButton.pack(side=tk.RIGHT)

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
