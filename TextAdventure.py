# Modul
import time
import os

# Konstanten
ROOM_START = "start"
ROOM_SECOND = "second"
ROOM_THREE = "three"
ROOM_FOUR = "four"
ROOM_FINAL_CLIMBE = "final_climbe"
ROOM_FINAL_MAIN_ENTRANCE = "final_main_entrance"

# Variable
player_name = input("Spieler-Name: ")
player_life = 3
print("Verbleibende Leben: " + str(player_life))
room = ROOM_START
wrong_user_input = False
wrong_user_input_sideway = False
way_completed = False

# Instant Win
if player_name == "win":
    os.system("cls")
    print("WIN")
    exit(0)

# Chapter One
while player_life > 0:
    if room == ROOM_START:
        if not wrong_user_input:
            print("Langsam erwachst du aus einem langen Schlaf !")
            time.sleep(2)
            print("Es ist Nacht und du befindest dich mitten in einem dir unbekanten Waldes !")
            time.sleep(2)
            user_select = input("Wähle eine Richtung in die du gehen möchtest ! (Norden, Süden, Westen, Osten): ")

        if wrong_user_input:
            user_select = input("Ungültige Eingabe ! Bitte gib Norden, Süden, Westen oder Osten ein: ")

    # North
        if user_select.lower() == "norden":
            wrong_user_input = False
            print("Du Entscheidest dich dafür nach Norden zu gehen.")
            time.sleep(2)
            room = ROOM_SECOND
            time.sleep(3)

    # South
        elif user_select.lower() == "süden":
           wrong_user_input = False
           player_life -= 1
           print("Du Entscheidest dich dafür nach Süden zu gehen.")
           time.sleep(2)
           print("Nach einigen Schritten siehst du eine Dornen wand, die sich langsam aus dem Boden erhebt !")
           time.sleep(2)
           print("Bei dem Versuch sie zu überwinden verletzt du dich jedoch.")
           time.sleep(2)
           print("Du verlierst ein Leben ")
           print("Verbleibende Leben: " + str(player_life))
           time.sleep(2)
           print("Wähle einen anderen Weg.")
           time.sleep(2)

    # West
        elif user_select.lower() == "westen":
            wrong_user_input = False
            print("Du machst dich auf in Richtung Westen.")
            time.sleep(2)
            print("Nach einem langen Fußmarsch siehst du in der Ferne ein blau, pulsierendes Licht !")
            time.sleep(2)
            print("Langsam näherst du dich ihm...")
            time.sleep(2)
            print("Als du es ereicht hast, saugt es dich Plötzlich ein !!!")
            time.sleep(2)
            print("Du befindest dich wieder am Anfang, wähle einen anderen Weg.")
            time.sleep(2)

    # East
        elif user_select.lower() == "osten":
            wrong_user_input = False
            print("Du schaust in den Himmel richtung Osten.")
            time.sleep(2)
            print("Eine lauer Windhauch weht aus dieser Richtung zu dir und du machst dich auf den Weg.")
            time.sleep(2)
            print("Nach einigerzeit siehst du im Schimmer des Mondlichts auf einer kleinen Lichtung einen Springbrunnen !")
            time.sleep(2)
            choose = input("Möchtest du hingehen oder weiterlaufen ? (Hingehen oder Weiterlaufen): ")

        # Sideway
            while not way_completed:

                # Go There / Drink
                if choose.lower() == "hingehen":
                    print("Langsam näherst du dich dem Brunnen...")
                    time.sleep(3)
                    print("Dort angekommen schaust du in das Wasser... du hörst eine Stimme !")
                    time.sleep(2)
                    print("Trink von meiner Quelle und du erhälst die Kraft mehr zu Erreichen !")
                    time.sleep(2)
                    choose = input("Hörst du auf die Stimme oder möchtest du diesen Ort verlassen ? (Trinken oder Gehen): ")
                    time.sleep(2)

                # Sideway = Inner (Fountain)
                    while not way_completed:

                        # Strange Voice
                        if choose.lower() == "trinken":
                            way_completed = True
                            print("Durch die seltsamme Stimme in ihren Bann gezogen, Trinkst du aus dem Brunnen.")
                            time.sleep(2)
                            print("Du fühlst ein Pulsieren das deinen Körper durchläuft...")
                            player_life += 1
                            print("Deine Lebensenergie steigt.")
                            time.sleep(1)
                            print(str(player_name) + ", deine Aktuellen leben Betragen: " + str(player_life))
                            time.sleep(1)
                            room = ROOM_SECOND
                            time.sleep(2)

                        # Go Further
                        elif choose.lower() == "gehen":
                            way_completed = True
                            print("Nach kurzer zeit des Abwegens, hast du dich dazu Entschlossen weiter zu gehen. ")
                            time.sleep(2)
                            room = ROOM_SECOND
                            time.sleep(2)

                        # Wrong Input
                        else:
                            while choose.lower() != "trinken" and choose.lower() != "gehen":
                                choose = input("Ungültige Eingabe ! Bitte gib Trinken oder Gehen ein: ")

                # Keep Walking
                elif choose.lower() == "weiterlaufen":
                    way_completed = True
                    print("Du Entscheidest dich weiter zu gehen und lässt den Springbrunnen hinter dir.")
                    time.sleep(2)
                    room = ROOM_SECOND
                    time.sleep(2)

                # Wrong Input
                else:
                    while choose.lower() != "hingehen" and choose.lower() != "weiterlaufen":
                        choose = input("Ungültige Eingabe ! Bitte gib Hingehen oder Weiterlaufen ein: ")

        # Wrong Input
        else:
            wrong_user_input = True

# Chapter Two
    elif room == ROOM_SECOND:
        os.system("cls")
        print("Nach einem schier endlosen Marsch, gelangst du einem Scheideweg.")
        time.sleep(3)
        print("Beide Wege führen wohl zu einem Siedlung, das du in der Ferne zu erkennen vermagst...")
        time.sleep(2)
        print("Um dorthin zu gelangen muss man allerdings eine Prüfung bestehen !")
        time.sleep(3)
        print("Der linke Weg führt über einen Friedhof richtung Siedlung.")
        time.sleep(2)
        print("Der rechte Weg über eine riesige Halle, die einsam in der Landschaft steht.")
        time.sleep(3)
        user_select = input("Welcher Prüfung möchtest du dich stellen ? (Halle oder Friedhof): ")
        time.sleep(2)

        # Wrong Input
        if user_select.lower() != "halle" and user_select.lower() != "friedhof":
            print("Ungültige Eingabe ! Bitte gib Halle/halle oder Friedhof/friedhof ein.")

        # Hall
        if user_select.lower() == "halle":
            print("Die Halle soll es sein...")
            time.sleep(2)
            print("Mutigen schrittes begibst du dich in richtung des Eingangs.")
            time.sleep(5)
            print("Dort angekommen betrachtest du das imposante Bauwerk. ")
            time.sleep(3)
            print("Du stehst vor zwei riesigen Toren, als du dich ihnen näherst öffnen sie sich... ")
            time.sleep(2)
            print("Du ziehst deine Streitaxt und tritst ein !")
            time.sleep(3)
            print("Am ende der Halle siehst du eine riesenhafte Gestallt stehen.")
            time.sleep(2)
            print("Mein Name ist Heimdallr..., jeder dem es Begehrt weiter zu gehen muss sich mir im Kampf stellen.")
            time.sleep(2)
            print("Ohne dir auch nur etwas zeit zu lassen, stürmt er mit seinem Zweihänder direkt auf dich los !")
            choose = input("Wie Reagierst du ? (Ausweichen, Gegenangriff oder Parieren): ")
            time.sleep(2)

        # Wrong Input
            if choose.lower() != "ausweichen" and choose.lower() != "angreifen" and choose.lower() != "parieren":
                print("Ungültige Eingabe ! Bitte gib Ausweichen, Angreifen oder Parieren ein.")

            # Evade
            if choose.lower() == "ausweichen":
                print("Kurz bevor dich Heimdallr erreichen kann springst du zur seite und rollst dich ab.")
                time.sleep(2)
                print("Heimdallr nimmt die Energie des ersten Angriffs und nutzt diese für einen seithieb.")
                time.sleep(2)
                print("Dir gelingt es jedoch diesen abzuwehren.")
                time.sleep(2)
                print("Diesen moment der unachtsamkeit nutzt du aus und führst einen sauberen hieb auf seine Hände aus.")
                time.sleep(2)
                print("Dir gelingt es Heimdallr schwer zu Verwunden und ihn somit Kampfunfähig zu machen !")
                time.sleep(2)
                print("Du stehst nun vor ihm, weiter zu Kämpfen schein für ihn Unmöglich.")
                time.sleep(2)
                choose = input("Du hast nun die Wahl, willst du ihn Verschonen oder Niederstrecken ? (Verschonen oder Niederstrecken): ")
                time.sleep(3)

            # Sideway = Spare / Strike down
                # Spare
                if choose.lower() == "verschonen":
                    print("Du schulterst deine Streitaxt.")
                    time.sleep(1)
                    print("Heimdallr schaut dich an...")
                    time.sleep(2)
                    print("Du bist würdig deinen Weg weiter zu bestreiten, nimm dieses Horn an dich, es wird dir auf deinem Weg noch von nutzen sein.")
                    time.sleep(2)
                    print("Heimdallr verwandelt sich in eine Lichtgestallt und übergibt dir das Horn.")
                    time.sleep(2)
                    print("Du nimmst es an dich und gehst weiter deiner Wege.")
                    room = ROOM_THREE
                    time.sleep(2)

                # Strike down
                elif choose.lower() == "niederstrecken":
                    print("Du erhebst deine Streitaxt und setzt zu einem gezielten Schlag auf seinem Kopf an...")
                    time.sleep(2)
                    print("Während du zuschlägst hörst du plötzlich Kampfgeschrei !")
                    time.sleep(3)
                    print("Wie aus dem nichts erscheinen Plötzlich an allen seiten der Halle Tore.")
                    time.sleep(2)
                    print("Als sie sich öffnen stürmen aber Tausende von Kriegern hinaus dirket auf dich zu !")
                    time.sleep(2)
                    print("Der masse unterlegen, verlierst du den Kampf und somit auch dein Leben !!!")
                    time.sleep(2)
                    print("Deine Reise endet hier... Game Over !")
                    player_life -= 1000
                    time.sleep(1)
                    print(str(player_name) + ", Endergebniss Leben: " + str(player_life))
                    exit(0)

                # Wrong Input
                if choose.lower() != "verschonen" and choose.lower() != "niederstrecken":
                    print("Ungültige Eingabe ! Bitte gib Verschonen oder Niederstrecken ein.")

            # Attack
            if choose.lower() == "angreifen":
                print("Unbeeindruckt der plötzlichen attacke gegenüber, erwiderst du deinerseits den Angriff !")
                time.sleep(1)
                print("Auf halbem Weg treffen sich der Stahl eurer Waffen...")
                time.sleep(1)
                print("In einer Schlagkombo die so Kraftvoll ist, dass selbst die Luft anfängt zu beben, liefert ihr euch einen erbitterten Kampf !")
                time.sleep(5)
                print("Doch schnell übernimmst du die Oberhand und drängst ihn zurück.")
                time.sleep(2)
                print("Schlag auf Schlag verliert Heimdallr immer mehr seiner Deckung.")
                time.sleep(2)
                print("Mit einem gezielten und kraftvollen Schlag zerbrichst du seinen Zweihänder und gibst ihm einen Schnellen Tod !")
                time.sleep(2)
                print("Nach dem erbitterten Kampf kommt die Besinnung.")
                time.sleep(1)
                print("Du hast gewonnen. Du nimmst den Zweihänder und legst ihn Heimdallr in seine Hände und ehrst somit seinen Tod.")
                time.sleep(2)
                print("Gerade als du gehen wolltest, hörst du Heimdallrs stimme !")
                time.sleep(2)
                print("Du hast ehrenvoll Gekämpft, nimm dies als Zeichen meines Respekts, es wird dir einen Dienst erweisen.")
                time.sleep(2)
                print("Heimdallr erscheint dir als Lichtgestallt und überlässt dir ein Horn.")
                time.sleep(2)
                print("Dankbar nimmst du es an und ziehst deiner Wege.")
                room = ROOM_THREE
                time.sleep(2)

            # Parry
            if choose.lower() == "parieren":
                print("Es bleibt keine Zeit die beste möglichkeit ist die Verteidigung.")
                time.sleep(2)
                print("Als Heimdallr dich ereicht, versuchst du den Schlag zu parieren, jedoch ist es zu spät...")
                time.sleep(2)
                print("Du konntest dich nicht standhaft genug aufstellen, der Schlag trifft zwar nur den Griff deiner Streitaxt.")
                time.sleep(1)
                print("Aber mit so einer wucht das du quer durch die Halle fliegst !")
                time.sleep(2)
                print("Bei der Landung Verletzt du dich !")
                player_life -= 2
                time.sleep(1)
                print(str(player_name) + ", dein Aktuelles Leben Beträgt: " + str(player_life))
                time.sleep(2)
                print("Du Rappelst dich auf dir bleiben nur drei Möglichkeiten.")
                time.sleep(2)
                print("Entweder du versucht zu Fliehen, du versuchst bei seinen Nächsten Angriff ihn auszuschalten oder du nimmst dein Schicksal an.")
                time.sleep(2)
                choose = input("Triff deine Wahl ! (Flucht, Ausschalten oder Schicksal): ")
                time.sleep(2)

                # Escape
                if choose.lower() == "flucht":
                    print("Du siehst keine Hoffnung mehr diesen Kampf zu Gewinnen und veruchst zu Fliehen.")
                    time.sleep(2)
                    print("Kurz bevor du die Eingangstore erreichst, Schließen diese sich")
                    time.sleep(2)
                    print(" Heimdallr ruft dir lachend nach: Nur Feiglinge fliehen aus einem Kampf.")
                    time.sleep(2)
                    print("Du drehst dich um und Heimdallr steht vor dir.")
                    time.sleep(2)
                    print("Ohne jede chance Streckt er dich nieder !!!")
                    player_life -= 1000
                    time.sleep(1)
                    print("Du warst zu feige um als ein Krieger zu sterben. Game Over !")
                    time.sleep(1)
                    print(str(player_name) + ", Endergebniss Leben: " + str(player_life))
                    exit(0)

                # Only Chance
                if choose.lower() == "ausschalten":
                    print("Von dem harten Aufprall angeschlagen stehst du langsam auf.")
                    time.sleep(3)
                    print("Als du wieder stehst siehst du wie Heimdallr zum nächsten Angriff ansezt.")
                    time.sleep(2)
                    print("Duzeigst dich Angeschlagener als du bist und wartest auf den perfekten Momment.")
                    time.sleep(1)
                    print("Im bruchteil einer Sekunde weichst du seinem Angriff aus und nutzt deine Streitaxt wie eine Lanze !")
                    time.sleep(3)
                    print("Heimdallr der auf diesen Angriff nicht vorbereitet war schaft es nicht mehr auszuweichen.")
                    time.sleep(2)
                    print("Die Schneide deiner Axt zieht sich einmal Kommplett durch den Rumpf von Heimdallr.")
                    time.sleep(2)
                    print("Langsam gehst du in seine richtung.")
                    time.sleep(2)
                    print("Er versucht seinen Zweihänder zu erreichen, aber alleine wird er es nicht schaffen !")
                    time.sleep(2)
                    print("Aus Respekt vor dem Kampf hilfst du ihm.")
                    time.sleep(2)
                    print("Hab dank " + str(player_name) + ". Nimm dieses Horn, es wird dir auf deiner Reise noch einen Dienst erweisen.")
                    time.sleep(2)
                    print("Du nimmst das Horn an dich.")
                    time.sleep(1)
                    print("Kurz darauf siehst du wie Heimdallr sich in ein Lichthüllt und wie ein Schwarm winziger Glühwürmchen in der Nacht verschwindet.")
                    time.sleep(2)
                    print("Nachdem du deine Wunden versorgt hast, nimmst du deine Reise wieder auf.")
                    room = ROOM_THREE
                    time.sleep(3)

                # Fate
                if choose.lower() == "schicksal":
                    print("Als wahrer Krieger weist du das ein Gegenangriff sinnlos ist.")
                    time.sleep(2)
                    print("Ebenfalls würdest du nimals Fliehen !")
                    time.sleep(2)
                    print("Lamgsam richtest du dich auf.")
                    time.sleep(3)
                    print("Du stellst dich in voller Größe hin, stolz, Ehrenhaft und mit dir selbst im Einklang.")
                    time.sleep(2)
                    print("Deine Streitaxt festengriffes in den Händen, zeigst du Heimdallr das nicht weichen wirst und dein Schicksal Akzeptierst.")
                    time.sleep(2)
                    print("Heimdallr setzt zum nächsten Angriff an und stürmt auf dich los.")
                    time.sleep(3)
                    print("Kurz bevor seine Klinge deinen Hals Berühren kann Stopt er.")
                    time.sleep(2)
                    print("Du bist ein wahrhaftiger Krieger, voller Würde und Stolz.")
                    time.sleep(2)
                    print("Deine Prüfung hast du bestanden...")
                    time.sleep(1)
                    print("Nimm dieses Horn als zeichen meines Respekts und erfülle dein Schiksal.")
                    time.sleep(2)
                    print("Du nimmst das Horn entgegen und siehst wie Heimdallr mit dem Licht des Mondes eins wird.")
                    time.sleep(5)
                    print("Nachdem du deine Wunden versorgt hast setzt du deine Reise fort.")
                    room = ROOM_THREE
                    time.sleep(3)

                # Wrong Input
                if choose.lower() != "flucht" and choose.lower() != "ausschalten" and choose.lower() != "schicksal":
                    print("Ungültige Eingabe ! Bitte gib Flucht, Ausschalten oder Schicksal ein.")

        # Graveyard
        if user_select.lower() == "friedhof":
            print("Deine Wahl fällt auf den Friedhof.")
            time.sleep(5)
            print("Auf deinem Weg zu den Gittern die dir Zugang zum Friedhof gewehren, siehst du inmitten eines Meeres aus Gräbern die mit Steinen bedeckt sind auch ein Bauwerk.")
            time.sleep(5)
            print("An den Gittern angekommen, verschafst du dir Zugang zum Friedhof.")
            time.sleep(2)
            print("Langsam Wandelst du über den Gräbern hinweg zu dem Gebilde.")
            time.sleep(2)
            print("Jetzt wo du davor stehst siehst du, dass es sich um ein Mausoleum handelt.")
            time.sleep(2)
            print("Jedoch scheint es verschlossen zu sein !")
            time.sleep(2)
            print("Du könntest versuchen es Aufzubrechen, das Schloss zu knacken oder einen anderen Weg versuchen zu finden.")
            time.sleep(2)
            choose = input("Überlege deinen nächsten Schritt ! (Aufbrechen, Schloss oder Umschauen): ")
            time.sleep(2)

        # Wrong Input
            if choose.lower() != "aufbrechen" and choose.lower() != "schloss" and choose.lower() != "umschauen":
                print("Ungültige Eingabe ! Bitte gib Aufbrechen, Schloss oder Umschauen ein.")

            # Break open
            if choose.lower() == "aufbrechen":
                print("Deine Wahl fällt auf Aufbrechen.")
                time.sleep(1)
                print("Du schaust dir die Tür an und suchst nach einem schwachen Punkt.")
                time.sleep(3)
                print("In der mitte der Tür siehst du in der Maserung des Holz eine Verzweigung die der für einen gezielten Schlag perfekt erscheint.")
                time.sleep(2)
                print("Als du gerade deine Streitaxt zum Schlag ansetzt, spürst du wie der Boden anfängt zu beben.")
                time.sleep(2)
                print("Du schaust dich um und siehst wie die Steinhaufen der Gräber insich zusammen fallen.")
                time.sleep(2)
                print("Auf einmal siehst du dich in mitten einer Armee voller Draugr.")
                time.sleep(1)
                print("Tapfer versuchst du dich zur Flucht durch zu schlagen.")
                time.sleep(3)
                print("Jedoch vergebens, deine letzten Gedanken sind die das du mit dem Wissen stirbst das du bald auch ein Draugr sein wirst...")
                time.sleep(2)
                print("Von nunan wirst du als Draugr diesen Friedhof beschützen. Game Over !")
                player_life -= 1000
                time.sleep(1)
                print(str(player_name) + ", Endergebniss Leben: " + str(player_life))
                exit(0)

            # Lock
            if choose.lower() == "schloss":
                print("Du versuchst dein glück mit einem Ditrich.")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("...")
                time.sleep(1)
                print("Geschaft das Schloss ist offen.")
                time.sleep(2)
                print("Langsam ziehst du die Tür auf.")
                time.sleep(3)
                print("Der kleine Raum ist erleuchtet von Kerzen.")
                time.sleep(1)
                print("In mitten steht ein steinerner Sarg in dem viele Runen gemeiselt wurden und an manchen stellen auch mit Edelmetallen verziert wurde.")
                time.sleep(2)
                print("Darauf liegen einige Schätze, darunter Münzen, Edelsteine und viel mehr Beute aus vergangenen Raubzügen.")
                time.sleep(2)
                print("Doch ein Schmuckstück fällt ganz besonders auf...")
                time.sleep(1)
                print("Es handelt sich um ein Amulett, von dem eine dir nicht Erklärbare aura ausgeht.")
                time.sleep(3)
                choose = input("Möchtest du es an dich nehmen oder liegen lassen ? (Mitnehmen oder Belassen): ")
                time.sleep(2)

                # Take
                if choose.lower() == "mitnehmen":
                    print("Du nimmst das Amulett an dich.")
                    time.sleep(2)
                    print("Es wird Zeit deine Reise fort zu setzen, du ziehst weiter richtung Siedlung.")
                    room = ROOM_THREE
                    time.sleep(2)

                # Leave
                if choose.lower() == "belassen":
                    time.sleep(2)
                    print("Nach einer kurzen bedenk Zeit, beschließt du das Amulett an seinem Platz zu belassen.")
                    time.sleep(2)
                    print("Du setzt deine Reise in richtung der Siedlung fort.")
                    room = ROOM_THREE
                    time.sleep(2)

                # Wrong Input
                if choose.lower() != "mitnehmen" and choose.lower() != "belassen":
                    print("Ungültige Eingabe ! Bitte gib Mitnehmen oder Belassen ein.")

            # Look Around
            if choose.lower() == "umschauen":
                print("Du suchst lieber nach einem alternativ Weg um in das Mausoleum zu gelangen.")
                time.sleep(5)
                print("Du bist einmal um das Mausoleum herum gelaufen, doch war deine suche vergebens.")
                time.sleep(2)
                print("Dir bleibt wohl nur eine der anderen Möglichkeiten offen.")
                time.sleep(2)

# Chapter Three
    elif room == ROOM_THREE:
        os.system("cls")
        print("Nach einiger Zeit erreichst du die Siedlung.")
        time.sleep(3)
        print("Du bleibst am Eingang der Befestigungsanlagen stehen und Schaust dich um !")
        time.sleep(3)
        print("Die Straßen sind wie leer gefegt, keine einzige Seele ist zu hören, weder Mensch noch Tier.")
        time.sleep(3)
        print("Langsam Schreitest du weiter in die Siedlung hinein.")
        time.sleep(2)
        print("Auf deinem Weg siehst du verlassene Häuser, Gehege und Stallungen.")
        time.sleep(2)
        print("An einer Steinplatte bleibst du stehen, sie scheint estwas zu Verbergen.")
        time.sleep(2)
        print("Du bist dir nicht sicher ob du es alleine schaffen würdest und ob sich der Aufwand überhaupt lohnt.")
        time.sleep(2)
        choose = input("Möchtest du versuchen das Geheimnis zu lüften oder Weitergehen ? (Geheimnis oder Weitergehen): ")
        time.sleep(2)

        # Wrong Input
        if choose.lower() != "geheimnis" and choose.lower() != "weitergehen":
            print("Ungültige Eingabe ! Bitte gib Geheimnis oder Weitergehen ein.")

        # Secret = Sword
        if choose.lower() == "geheimnis":
            print("Du schaust dir die Steinplatte genauer an und entdeckst dabei eine kleine Schwachstelle.")
            time.sleep(2)
            print("Mit einem Gezielten schlag deiner Streitaxt könntest du sie bestimmt zerschmettern.")
            time.sleep(2)
            print("Aber deine Waffe wird mit großer Wahrscheinlichkeit Zerstört werden !")
            time.sleep(2)
            choose = input("Möchtest du das Risiko eingehen ? (Hieb oder Weiter): ")
            time.sleep(2)

        # Wrong Input
            if choose.lower() != "hieb" and choose.lower() != "weiter":
                print("Ungültige Eingabe ! Bitte gib Hieb oder Weiter ein.")

            # Cut
            if choose.lower() == "hieb":
                print("Deine Neugier überwiegt das Risiko deine Waffe zu verlieren.")
                time.sleep(2)
                print("Mit einem gezielten Hieb auf die Schwachstelle der Steinplatte bringst du sie zum bersten.")
                time.sleep(1)
                print("Deine Streitaxt allerdings auch.")
                time.sleep(1)
                print("Sie zerspringt in mehrere dutzend Teile.")
                time.sleep(5)
                print("Zögernd und nachdenklich ob dies eine gute entscheidung war, tritst du durch den freigelegten Weg in einen Keller ein.")
                time.sleep(2)
                print("Eine einzelne Fackel flackert am Bodenliegend, du hebst sie auf und schaust dich um.")
                time.sleep(3)
                print("Du siehst am ende des schmalen aber langen Raumes eine Schwertscheide an der Wand hängen.")
                time.sleep(2)
                print("Langsam läufst du darauf zu.")
                time.sleep(4)
                print("Als du an der Wand angekommen bist siehst du das die Schwertscheide leer ist...")
                time.sleep(2)
                choose = input("Möchtest du sie denoch an dich nehemn oder gehst du zurück ? (Nehmen oder Zurück): ")
                time.sleep(2)

                # Wrong Input
                if choose.lower() != "nehmen" and choose.lower() != "zurück":
                    print("Ungültige Eingabe ! Bitte gib Nehmen oder Zurück ein.")

                # Take = Sword
                if choose.lower() == "nehmen":
                    print("Troz das sich kein Schwert darin befindet nimmst du die Schwertscheide an dich.")
                    time.sleep(2)
                    print("Als du sie gerade angelegt hast, spürst du plötzlich eine dir Unbekannte macht.")
                    time.sleep(2)
                    print("Aus dem nichts erscheint Plötzlich ein Schwert in der Schwertscheide.")
                    time.sleep(2)
                    print("Du eillst nach drausen auf die Straße und ziehst deine Klinge.")
                    time.sleep(2)
                    print("Für einen kurzen Momment erstrahlt die Siedlung in einem Hellen schein.")
                    time.sleep(2)
                    print("Die Klinge ist von beeindruckender Schmiedefertigkeit.")
                    time.sleep(2)
                    print("Von nun an nennst du sie dein eigen und wirst deine Kämpfe mit ihr Bestreiten.")
                    time.sleep(2)
                    print("Gerade als du dein Schwert wieder wegsteckst stürtzen neben dir zwei Häuser ineinander.")
                    time.sleep(2)
                    print("Sie versperren einen Weg, dir bleibt nur der weg weiter der Straße entlang.")
                    room = ROOM_FOUR
                    time.sleep(2)

                # Return
                if choose.lower() == "zurück":
                    print("Enteuscht davon das deine Waffe zerstört ist und es sich nicht Lohnte, kehrst du zurück auf den weg.")
                    time.sleep(2)
                    print("Doch als du gerade weiter gehen willst siehst du in einer Gasse mehrere Waffen liegen.")
                    time.sleep(2)
                    print("Berauscht von dem Gedanken dir eine neue Waffe zuzulegen, rennst du in deren Richtung.")
                    time.sleep(2)
                    print("Doch als du gerade in die Gasse hinein gingst, hörst du wie Balken anfangen neben dir zu brechen.")
                    time.sleep(2)
                    print("Ohne jede Chance dem zu entgehen, wirst du von den anahenden Trümmern getötet.")
                    time.sleep(2)
                    player_life -= 1000
                    print("Deine Gier war zu groß. Game Over !")
                    time.sleep(1)
                    print(str(player_name) + ", Endergebniss Leben: " + str(player_life))
                    exit(0)



        # Alley
        if choose.lower() == "weitergehen":
            print("Das Risiko deine Waffe zu verlieren erscheint dir zu hoch.")
            time.sleep(3)
            print("Du betrachtest noch kurz die Steinplatte und gehst dann weiter.")
            time.sleep(2)
            print("Doch nur ein paar Meter weiter siehst du eine abzweigung in eine Gasse.")
            time.sleep(2)
            print("Als du dich ihr näherst, siehst du ein Arsenal an Waffen.")
            time.sleep(3)
            print("Du schaust dich um doch du entdeckst keine Waffe die dich Anspricht.")
            time.sleep(2)
            print("Gerade als du weitergehen wolltest, siehst du ein aufblitzen.")
            time.sleep(2)
            print("Es ist ein Speer, Goldbronzen glänzt er im Mondschein und an seiner Spitze ist ein rotes Tuch angebunden.")
            time.sleep(2)
            print("Je länger du sie Anstarrst, deste Machtvoller wirkt sie auf dich.")
            choose = input("Möchtest du sie dir Holen oder behälst du deine Waffe ? (Wechseln oder Behalten): ")
            time.sleep(2)

            # Wrong Input
            if choose.lower() != "wechseln" and choose.lower() != "behalten":
                print("Ungültige Eingabe ! Bitte gib Wechseln oder Behalten ein.")

            # Exchange = Spear
            if choose.lower() == "wechseln":
                print("Wie in Trance läufst du in seine Richtung.")
                time.sleep(5)
                print("Bei dem Speer angekommen nimmst du deine Streitaxt in deine Hände.")
                time.sleep(2)
                print("Du betrachtest sie und gedenkst jener Schlachten in der sie dich begleitet hat.")
                time.sleep(2)
                print("Gezeichnet eines jeden Kampfes, legst du sie nieder während du ihr dankst.")
                time.sleep(2)
                print("Langsam erhebst du dich.")
                time.sleep(4)
                print("Du greifst nach dem Speer.")
                time.sleep(1)
                print("Seine Energie erfüllt dich und gibt dir ein machtvolles Gefühl.")
                time.sleep(2)
                print("Von nunan nennst du sie dein Eigen und bestreitest deine Kämpfe mit ihr.")
                time.sleep(2)
                print("Du begibst dich langsam wieder zurück zu der Straße aus der du kamst.")
                time.sleep(3)
                print("Wie es scheint gerade auch noch rechtzeitig.")
                time.sleep(2)
                print("Kurz nachdem du die Straße ereicht hast stürzen hinter dir die beiden gegenüberliegenden Häuser ein !")
                time.sleep(2)
                print("Du legst deinen Speer über die Schulter und gehst weiter die Straße entlang.")
                room = ROOM_FOUR
                time.sleep(2)

            # Keep Current
            if choose.lower() == "behalten":
                print("Du nimmst deine Streitaxt in die Hände un betrachtest sie.")
                time.sleep(5)
                print("Du denkst an all die Schlachten, Kämpfe und Duelle die du mit ihr Bestritten hast.")
                time.sleep(2)
                print("Und du denkst an all die Schlachten die noch kommen werden.")
                time.sleep(2)
                print("Du entscheidest dich sie zu Behalten, sie war dir stehts ein treuer Begleiter.")
                time.sleep(2)
                print("Du willst gerade den Weg weitergehen, als du Hörst wie die beiden Häuser die neben der Gasse liegen, in sich zusammen stürzen und den Weg versperren.")
                time.sleep(3)
                print("Wissend dem sicheren Tod entgangen zu sein gehst du weiter der Straße entlang.")
                room = ROOM_FOUR
                time.sleep(2)


# Chapter Four
    elif room == ROOM_FOUR:
        os.system("cls")
        print("Nach einigen Minuten der Straße folgend, erreichst du den Hauptplatz der Siedlung.")
        time.sleep(2)
        print("Du siehst ebenfalls ein großes Gebäude, es ist das größte in der Siedlung.")
        time.sleep(2)
        print("Du läufst in seine richtung, auf den weg dorthin fällt dir ein kleiner Pfad auf der neben das Gebäude führt.")
        choose = input("Möchtest du den Pfad entlang gehen oder den Haupteingang nehmen ? (Pfad oder Haupteingang): ")
        time.sleep(2)

        # Wrong Input
        if choose.lower() != "pfad" and choose.lower() != "haupteingang":
            print("Ungültige Eingabe ! Bitte gib Pfad oder Haupteingang ein.")

        # Path
        if choose.lower() == "pfad":
            print("Du schaust dir den Pfad genauer an...")
            time.sleep(3)
            print("Während du ihm folgst, siehst du das er dich zu einem verweisten Gehege führt.")
            time.sleep(2)
            print("Dort angekommen siehst du einen Vorsprung, von dort aus du ein Fenster erreichen kannst.")
            time.sleep(2)
            print("Du könntest  versuchen auf den Vorsprung zu klettern und das Gebäude darüber betreten oder du begibst dich auf den Rückweg zum Haupteingang.")
            time.sleep(3)
            choose = input("Du könntest Klettern oder zurück gehen. (Klettern oder Rückweg): ")
            time.sleep(2)

            # Climbe
            if choose.lower() == "klettern":
                print("Dein Blick schweift umher auf der suche nach einer geeigneten möglichkeit auf den vorsprung zu kommen.")
                time.sleep(2)
                print("Du siehst einige Meter daneben eine Leiter liegen.")
                time.sleep(2)
                print("Du schaust sie dir genauer an und siehst das sie Unbeschädigt ist.")
                time.sleep(2)
                print("Langsam erklimmst du die Leiter.")
                time.sleep(4)
                print("Oben angekommen gehst du durch das Fenster")
                room = ROOM_FINAL_CLIMBE
                time.sleep(2)

            # Way Back
            if choose.lower() == "rückweg":
                print("Du begibst dich lieber wieder zurück zum Haupteingang.")
                time.sleep(5)
                choose = "haupteingang"
                time.sleep(2)

        # Main Entrance
        if choose.lower() == "haupteingang":
            print("Du gehst immerweiter auf den Haupteingang zu.")
            time.sleep(4)
            print("Als du die Türen ereichst hälst du kurz inne !")
            time.sleep(2)
            print("Du hörst eine Stimme... sie klingt... Aufgebracht.")
            time.sleep(2)
            print("Du weist nicht was dich erwartet !!!")
            time.sleep(2)
            choose = input("Möchtest du Unbewaffnet die Türen öffnen oder machst du die Kampfbereit ? (Unbewaffnet oder Kampfbereit): ")
            time.sleep(2)

            # Wrong Input
            if choose.lower() != "unbewaffnet" and choose.lower() != "kampfbereit":
                print("Ungültige Eingabe ! Bitte gib Unbewaffnet oder Kampfbereit ein.")

            # Unarmed
            if choose.lower() == "unbewaffnet":
                print("Du beschließt Unbewaffnet hinein zu gehen !")
                time.sleep(2)
                print("Langsam öffnest du die Tür.")
                time.sleep(5)
                print("Als diese offen stehen, erblickst du einen Mann der in einem großen Saal auf und ab Läuft.")
                time.sleep(2)
                print("Plötzlich bleibt er stehen und Blickt dich an.")
                time.sleep(2)
                print("Er fängt an breit zu Grinsen und sagt: Hallo mein Freund !")
                time.sleep(1)
                print("Bitte komm doch hinein.")
                room = ROOM_FINAL_MAIN_ENTRANCE
                time.sleep(2)


            # Battle Ready
            if choose.lower() == "kampfbereit":
                print("Die Situation bereitet dir Unbehagen und du ziehst deine Waffe !")
                time.sleep(2)
                print("Du Atmest tief durch.")
                time.sleep(4)
                print("Du tritst die Türen auf und Sprintest auf die Person zu.")
                time.sleep(3)
                print("Doch als du bei ihr angekommen bist und sie Attakierst...")
                time.sleep(1)
                print("Merkst du das es sich um ein Trugbildhandelt und du weist es ist zu Spät !")
                time.sleep(2)
                print("Die Türen fliegen zu, der Raum Verfinstert sich, ein Diabolische Lachen ertönt.")
                time.sleep(2)
                print("Plötzlich merkst du zwei Stiche im Rücken.")
                time.sleep(2)
                print("Langsam sackst du zu Boden und verblutest.")
                time.sleep(2)
                print("Mit deinen letzten Blicke siehst du Loki.")
                time.sleep(2)
                print("Versuch es doch das nächste mal etwas Diplomatischer feixte er.")
                player_life -= 1000
                time.sleep(1)
                print("Loki hat dich Überlistet. Game Over !")
                time.sleep(1)
                print(str(player_name) + ", Endergebniss Leben: " + str(player_life))
                exit(0)

# Chapter Five = Climbe
    elif room == ROOM_FINAL_CLIMBE:
        os.system("cls")
        print("Während du hineingehst, hörst du plötzlich ein lautes Lachen. Darauf folgts das an den seiten sich Feuerschalen entzünden.")
        time.sleep(2)
        print("Du siehst nun am Kopfende eine dunkle Kreatur, die sich langsam erhebt.")
        time.sleep(3)
        print("Nunden reisender... du bist also in meine Burg eingedrungen und nun ?")
        choose = input("Die Bedrohliche gestallt kommt langsamen schrittes immer näher, was wirst du tun ? (Flucht, Kampf oder Verhandeln): ")

        # Wrong Input
        if choose.lower() != "flucht" and choose.lower() != "kampf" and choose.lower() != "verhandeln":
            print("Ungültige Eingabe ! Bitte gib Flucht/flucht, Kampf/kampf oder Verhandeln/verhandeln ein.")

        # Flight
        if choose.lower() == "flucht":
            print("Bei dem Versuch zu fliehen, trifft dich eine rießige Axt die dich sofort Tötet !")
            time.sleep(2)
            player_life -= 100
            print("GAME OVER !!!")
            time.sleep(1)
            print("Endergebniss Leben: " + str(player_life))

        # Fight
        if choose.lower() == "kampf":
            print("Du entscheidest dich zu Kämpfen, was wohl auch deine einzige wirklich option ist.")
            time.sleep(2)
            print("Du ziehst deine Waffe und begibst dich in position.")
            time.sleep(2)
            choose = input("Was ist dein nächster schritt ? (Defensiv oder Offensiv): ")

            # Wrong Input
            if choose.lower() != "defensiv" and choose.lower() != "offensiv":
                print("Ungültige Eingabe ! Bitte gib Defensiv/defensiv oder Offensiv/offensiv ein.")

            # Defensive
            if choose.lower() == "defensive":
                print("Du nimmst eine defensive haltung an und wehrst somit erfolgreich seinen Angriff ab.")
                time.sleep(2)
                choose = input("Möchtest du einen Gegenangriff starten oder Abwarten ? (Gegenangriff oder Abwarten):  ")

                # Wrong Input
                if choose.lower() != "gegenangriff" and choose.lower() != "abwarten":
                    print("Ungültige Eingabe ! Bitte gib Gegenangriff/gegenangriff oder Abwarten/abwarten ein.")

                # Counterattack
                if choose.lower() == "gegenangriff":
                    print("Du holst zum gegenschlag aus, deine Waffe fängt an zu glühen, du spürst seine macht.")
                    time.sleep(2)
                    print("Mit einer hieb reihenfolge ungeahnter schnelligkeit gelingt es dir die Überhand zu geweinnen und den dämonischen Fürsten nieder zu strecken.")
                    time.sleep(2)
                    print("Congratulations, You Win !")
                    time.sleep(2)
                    print("Endergebniss Leben: " + str(player_life))

                # Wait
                if choose.lower() == "abwarten":
                    print("Dein zögern kostet dich das leben.")
                    time.sleep(2)
                    player_life -= 100
                    print("GAME OVER !!!")
                    time.sleep(1)
                    print("Endergebniss Leben: " + str(player_life))

            # Offensive
            if choose.lower() == "offensiv":
                print("Du ziehst deine Waffe und begibbst dich in Angriffs position.")
                time.sleep(2)
                print("Du spührst eine Macht die deine Waffe und ganzen Körper durchströmt.")
                time.sleep(2)
                print("Mit einer gewalltigen Kraft setzt du mit einem rießigen satz zum Angriff an und stürmst auf den dunklen fürsten an")
                time.sleep(3)
                print("Doch er kann diesen Angriff abwehren.")
                time.sleep(2)
                choose = input("Die Zeit steht wie still, was wirst du tun ? (Nochmals oder Ausweichen): ")

                # Wrong Input
                if choose.lower() != "nochmals" and choose.lower() != "ausweichen":
                    print("Ungültige Eingabe ! Bitte gib Nochmals/nochmals oder Ausweichen/ausweichen ein.")

                # Again
                if choose.lower() == "nochmals":
                    print("Du setzt erneut zum Angriff an, doch der Fürst wusste was du vor hast und Tötet dich mit einem Schlag !")
                    player_life -= 100
                    time.sleep(2)
                    print("GAME OVER !!!")
                    time.sleep(1)
                    print("Endergebniss Leben: " + str(player_life))

                # Doge
                if choose.lower() == "ausweichen":
                    print("Du weichst aus und dir geling es dadurch dem unerwarteten Angriff des Fürsten zu trozen.")
                    time.sleep(2)
                    print("Die kurze verwirrung des Fürsten nutzt du aus und durchbohrst seinen Körper mit deiner Waffe, mitten in sein Herz. ")
                    time.sleep(2)
                    print("Leblos fällt er zu Boden und der Sieg ist dir gewiss !")
                    time.sleep(3)
                    print("CONGRATULATIONS" + str(player_name) + "YOU WIN !")
                    time.sleep(2)
                    print("Endergebniss Leben: " + str(player_life))

        # Negotiating
        if choose.lower() == "verhandeln":
            print("Bei dem versuch mit der Dämonischen erscheinung zu verhandeln, kostet es dich leider deinen Kopf... !")
            player_life -= 100
            print("GAME OVER !!!")
            time.sleep(1)
            print("Endergebniss Leben: " + str(player_life))

# Chapter Five = Main Enterance
    elif room == ROOM_FINAL_MAIN_ENTRANCE:
        os.system("cls")
        print("Langsam öffnest du die tür und Trits ein, du siehst einen vorsprung von wo du eine besser übersicht bekommst.")
        time.sleep(5)
        print("Obenn angekommen bemerkst du ein paar gute Positionen für einen Angriff !")
        time.sleep(2)
        choose = input("Zum einen könntest du über einen Balken gehen und einen angriff von oben starten. Zum anderen könntest du einen Direkten angriff starten oder du suchst nach weitern möglichkeiten ! (Balken, Direkt oder Suchen):  ")

        # Wrong Input
        if choose.lower() != "balken" and choose.lower() != "direkt" and choose.lower() != "suchen":
            print("Ungültige Eingabe ! Bitte gib Balken/balken, Direkt/direkt oder Suchen/suchen ein.")

        # Joist
        if choose.lower() == "balken":
            print("Langsam schleichst du dich über den Balken, dabei stolperst du und fällst zu den Füßen des dämonen Fürsten.")
            time.sleep(2)
            print("Du hast keine chance, er erhebt seine Axt und streckt dich nieder !")
            player_life -= 100
            time.sleep(2)
            print("GAME OVER !!!")
            time.sleep(1)
            print("Endergebniss Leben: " + str(player_life))

        # Direct Attack
        if choose.lower() == "direkt":
            print("Du zückst deine Waffe und, mit einem mächtigen Sprung und Schrei greifst du den Fürsten an.")
            time.sleep(2)
            print("Voller desinteresse zerteilt er dich mit einem hieb seiner Axt !")
            player_life -= 100
            time.sleep(2)
            print("GAME OVER !!!")
            time.sleep(1)
            print("Endergebniss Leben: " + str(player_life))

        # Seek
        if choose.lower() == "suchen":
            print("Du schaust dich nach Alternativen um und entdeckst dabei ein seil das neben dir aufgewickelt wurde.")
            time.sleep(2)
            print("Du betrachtest das seil genauer un folgst ihm zu seinem ursprung.")
            time.sleep(3)
            print("Es scheint als gebe sich dir die Gelegenheit den fürsten ohne Kampf aus dem weg zu schaffen.")
            time.sleep(1)
            print("Am ende des Seiles hägt ein schwerer Käfig, darin befinden sich die übereste des Hofstaats. ")
            time.sleep(3)
            print("Du schneidest das seil durch und dr Käfig fällt hinunter. Der dämonen Fürst ist besiegt !")
            time.sleep(2)
            print("CONGRATULATIONS" + str(player_name) + "YOU WIN !")
            time.sleep(1)
            print("Endergebniss Leben: " + str(player_life))
