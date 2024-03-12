class Woerterbuch:
    def __init__(self):
        self.woerter = {}
        self.dateiname = "woerterbuch.txt"
        self.laden()

    def speichern(self):
        with open(self.dateiname, "w") as datei:
            datei.write(repr(self.woerter))

    def laden(self):
        try:
            with open(self.dateiname, "r") as datei:
                inhalt = datei.read()
                self.woerter = eval(inhalt) if inhalt else {}
        except FileNotFoundError:
            self.woerter = {}

    def eingabe(self):
        schlüssel = input("Geben Sie das deutsche Wort ein: ")
        bedeutung = input("Geben Sie das englische Wort ein: ")
        self.woerter[schlüssel] = bedeutung
        self.speichern()

    def anzeigen(self, schlüssel):
        print(self.woerter.get(schlüssel, f"'{schlüssel}' ist nicht im Wörterbuch vorhanden."))

    def bearbeiten(self, schlüssel):
        if schlüssel in self.woerter:
            bedeutung_neu = input("Geben Sie die neue Bedeutung ein: ")
            self.woerter[schlüssel] = bedeutung_neu
            self.speichern()
        else:
            print(f"'{schlüssel}' ist nicht im Wörterbuch vorhanden.")

    def loeschen(self, schlüssel):
        if schlüssel in self.woerter:
            del self.woerter[schlüssel]
            print(f"'{schlüssel}' wurde erfolgreich entfernt.")
            self.speichern()
        else:
            print(f"'{schlüssel}' ist nicht im Wörterbuch vorhanden.")

    def alle_woerter_anzeigen(self):
        if self.woerter:
            for schlüssel, bedeutung in self.woerter.items():
                print(f"{schlüssel}: {bedeutung}")
        else:
            print("Das Wörterbuch ist leer.")

mein_woerterbuch = Woerterbuch()

def menu():
    while True:
        eingabe = input("Was möchten Sie tun?\n- Ein Wort eingeben (e)\n- Ein Wort suchen (s)\n- Ein Wort bearbeiten (b)\n- Ein Wort löschen (l)\n- Alle Wörter anzeigen (aa)\n- Programm beenden (y): ").lower()

        if eingabe == "e":
            mein_woerterbuch.eingabe()
        elif eingabe == "s":
            schlüssel = input("Geben Sie das deutsche Wort ein, das Sie suchen: ")
            mein_woerterbuch.anzeigen(schlüssel)
        elif eingabe == "b":
            schlüssel = input("Geben Sie das deutsche Wort ein, das Sie bearbeiten möchten: ")
            mein_woerterbuch.bearbeiten(schlüssel)
        elif eingabe == "l":
            schlüssel = input("Geben Sie das deutsche Wort ein, das Sie löschen möchten: ")
            mein_woerterbuch.loeschen(schlüssel)
        elif eingabe == "aa":
            mein_woerterbuch.alle_woerter_anzeigen()
        elif eingabe == "y":
            print("Programm wird beendet...")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

menu()
