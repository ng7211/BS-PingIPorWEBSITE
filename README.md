Python-Skript try_host.py [-h|-s <sec>] <hostname>|<IP-Address>
Anforderungen:
• Das Skript soll einen Hostnamen oder eine IP-Adresse als Befehlszeilenargument entgegennehmen.
• Das Skript soll die Option -h unterstützen, die eine Hilfenachricht ausgibt.
• Das Skript soll die Option -s <sec> unterstützen, die das Intervall zwischen den Pings in Sekunden angibt. Standardmäßig soll das Intervall 3 Sekunden betragen.
• Das Skript soll den Host in regelmäßigen Abständen pingen und den Host sowie Status (OK
oder FAILED) ausgeben.
• Das Skript soll eine Fehlermeldung ausgeben, wenn keine gültigen Argumente übergeben werden.
Das Skript unterstützt folgende Optionen (es darf aber nur eine Option gleichzeitig angegeben
werden):
• -h : Nur Ausgabe der „Usage Message"
• -s <sec> : Der ping wird zyklisch alle <sec> Sekunden ausgeführt.
Fehlt die -s Option, wird der ping alle 3 Sekunden ausgeführt.
Beispiel: Der Aufruf
python3 t r y _hos t . py −s 5 google . de
erzeugt alle 5 Sekunden eine Ausgabe der Art:
google . de OK
falls der Host google.de erreichbar ist, anderenfalls
google . de FAILED
