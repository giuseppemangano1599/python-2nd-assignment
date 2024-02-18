#########################################################################################################################
# Terzo assignment in itinere del corso "Programmazione e Analisi dati (A. A. 2023/24) - 622AA-23"                      #
# Codice scritto dallo studente Giuseppe Mangano - Matricola: 674125 - Università di Pisa (g.mangano3@studenti.unipi.it)#
#########################################################################################################################         

# i commenti dei docenti sono stati mantenuti per maggiore chiarezza del codice e sono quelli coi tripli doppi apici ("""),
# quelli miei sono contrassegnati dai commenti col cancelletto (#)

#CLASSE Studente

class Studente:

    """METODI da aggiungere oltre a quelli presenti:

    - Costrutture: metodo che inizializza lo studente con cognome, nome e matricola presi come argomenti e inizializza listaesami con lista vuota,
    controllando che i tipi dei parametri attuali abbiano il tipo corretto altrimenti solleva un'eccezione TypeError
    - Getters: metodi che restituiscono il valore di una variabile di istanza, es: get_cognome() --> restituisce il cognome
    - Setters: metodi che modificano il valore di una variabile di istanza, es: set_cognome(cognome) --> modifica il cognome
    controllare che i valori inseriti siano del tipo e del valore corretto altrimenti sollevare un'eccezione TypeError o ValueError"""
    
    # N.B. blocchi try except rimossi perché sono presenti in main.py

    # costruttore
    def __init__ (self, cognome, nome, matricola):

        """#STATO:
        cognome: cognome dello studente (stringa)
        nome: nome dello studente (stringa)
        matricola: numero di matricola (intero positivo)
        listaesami: lista di tuple (codice -- str, voto--int positivo >= 18 e <33)"""

        # controllo dei tipi
        if type(cognome) != str:
            raise TypeError("Il cognome deve essere una stringa.")

        if type(nome) != str:
            raise TypeError("Il nome deve essere una stringa.")
        
        if type(matricola) != int or matricola <= 0:
            raise ValueError("La matricola deve essere un intero positivo.") # fare due controlli su "matricola" sarebbe ridondante, meglio accorparli e restituire ValueError

        self.cognome = cognome
        self.nome = nome
        self.matricola = matricola
        self.listaesami = []
    
    # getters e setters
    def get_cognome(self):
        return self.cognome
    
    def set_cognome(self, cognome):
        if type(cognome) != str:
            raise TypeError("Il cognome deve essere una stringa.")

        self.cognome = cognome

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        if type(nome) != str:
            raise TypeError("Il nome deve essere una stringa.")

        self.nome = nome
    
    def get_matricola(self):
        return self.matricola
    
    def set_matricola(self, matricola):
        if type(matricola) != int or matricola < 0:
            raise TypeError("La matricola deve essere un intero positivo.")
        self.matricola = matricola

    def get_listaesami(self):
        return self.listaesami
    
    def set_listaesami(self, listaesami):
        if type(listaesami) != list:
            raise TypeError("La lista degli esami deve essere una lista di tuple.")
        if listaesami == []:
            self.listaesami = listaesami
        else:
            for esame in listaesami: # itero un controllo e vedo se ogni esame è una tupla di due elementi e controllo i tipi
                if type(esame) != tuple and len(esame) != 2:
                    raise TypeError("Gli elementi all'interno della lista degli esami devono essere tuple con due valori all'interno: codice e voto")
                
                codice = esame[0]
                voto = esame[1]
                
                if type(codice) != str:
                    raise TypeError("Il codice dell'esame deve essere una stringa.")
                if type(voto) != int:
                    raise TypeError("Il voto deve essere un intero.")
                if voto < 18 or voto > 32: 
                    raise ValueError("Il voto deve essere un intero positivo maggiore o uguale a 18 e minore di 33.")
            self.listaesami = listaesami


    """Restituisce il voto dell'esame con codice "codice" se presente
    :param codice: il codice dell'esame
    :return: il voto dell'esame se presente
    :return: None se l'esame non è presente"""

    def get_voto(self, codice):
        # la funzione dict() riconosce le liste di tuple e le trasforma in un dizionario con chiave il primo elemento della tupla (codice) e valore il secondo (voto),
        # accedere al voto così diventa più intuitivo perché si usa il metodo get(), anziché iterare per tutta la lista
        diz_esami = dict(self.listaesami)
        return diz_esami.get(codice, None) # None in questo caso è il valore predefinito per il metodo get() in caso l'esame non sia presente
        

    """Restituisce una stringa che rappresenta lo studente 
    esempio: Alessandro Bocci mat: 414805 esami: no
    esempio: Alessandro Bocci mat: 414805 esami: [('544MM', 23)]"""
    
    def __str__(self):
        # istruzione di ritorno scritta in questo modo per fattore stilistico
        # sennò la riga di codice veniva troppo lunga
        if self.listaesami != []:
            return (
                str(self.nome) + " " + str(self.cognome) +
                " mat: " + str(self.matricola) + " esami: " +
                str(self.listaesami)
                )
        else:
            return (
                str(self.nome) + " " + str(self.cognome) +
                " mat: " + str(self.matricola) + " esami: no"
                )


    """Restituisce True se self e altroStudente rappresentano lo stesso studente
    (stesso cognome, stesso nome, stessa matricola)"""

    def __eq__(self, altroStudente):
        # istruzione di ritorno scritta in questo modo per fattore stilistico
        # sennò la riga di codice veniva troppo lunga
        # concatenare tutte le uguaglianze restituirà un'unica risposta (True se sono lo stesso studente, False altrimenti)
        if type(altroStudente) != Studente:
            return False
        else:
            return (self.cognome == altroStudente.get_cognome()
                    and self.nome == altroStudente.get_nome()
                    and self.matricola == altroStudente.get_matricola()
                    )


    """Aggiunge un nuovo esame superato (codice, voto) alla lista esami
    :param codice: il codice dell'esame
    :param voto: il voto dell'esame
    :return: True se l'inserimento è andato a buon fine
    :return: False se si è verificato un errore (es. il codice è già presente)"""

    def registra_esame(self, codice, voto):
        if type(codice) != str or type(voto) != int or voto < 18  or voto > 32:
            return False # il codice dell'esame deve essere una stringa e il voto deve essere un intero positivo maggiore o uguale di 18 e minore di 33
        
        for esame in self.listaesami:
            if codice == esame[0]:
                return False # il codice è già presente
        self.listaesami.append((codice, voto))
        return True # l'inserimento è andato a buon fine


    """Modifica il voto dell'esame con codice "codice" con il nuovo voto "voto"
    :param codice: il codice dell'esame da modificare
    :param voto: il nuovo voto dell'esame
    :return: True se la modifica è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)"""

    def modifica_voto(self, codice, voto):
        if type(codice) != str or type(voto) != int or voto < 18 or voto > 32:
            return False # il codice dell'esame deve essere una stringa e il voto deve essere un intero positivo e minore di 33
    
        if self.cancella_esame(codice) == True:  # chiamata al metodo (cancella_esame) + verifica se la cancellazione è andata a buon fine
            self.listaesami.append((codice, voto))
            return True  # il voto è stato modificato correttamente
        else:
            return False # si è verificato un errore

    """Cancella l'esame con codice "codice"
    :param codice: il codice dell'esame da cancellare
    :return: True se la cancellazione è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)"""

    def cancella_esame(self, codice):
        if type(codice) != str:
            return False # il codice dell'esame deve essere una stringa
        for esame in self.listaesami:
            if codice == esame[0]: # verifico se il codice è presente
                self.listaesami.remove(esame) # è necessario rimuovere codice e voto insieme perché sono valori dentro una tupla
                # e quindi per definizione non è modificabile
                return True # l'esame è stato rimosso correttamente
        return False # il codice non è presente


    """Calcola la media dei voti negli esami sostenuti
    :return f: f è un valore float che fornisce la media dei voti negli esami sostenuti
    :return None: se lo studente non ha sostenuto esami"""

    def media(self):
        somma = 0 # variabile di accumulazione
        if self.listaesami == []:
            return None # lo studente non ha sostenuto esami
        for esame in self.listaesami:
            somma += esame[1]
        f = somma / len(self.listaesami) # formula della media
        return f

##############################################################################

# CLASSE Archivio
    
class Archivio:
    
    """METODI da aggiungere oltre a quelli presenti:
    - Costrutture: metodo che inizializza l'archivio con un dizionario vuoto"""
    
    # costruttore
    def __init__(self):
        """#STATO:
        stud: dizionario degli studenti con chiave la matricola e valore una coppia oggetto studente e note (stringa)"""

        self.stud = {}


    """Inserisce un nuovo studente nel dizionario stud 
    :param studente: oggetto studente da inserire
    :param note: stringa (opzionale)
    :return: True se l'inserimento è stato effettuato con successo,
    :return: False  se i parametri non hanno il tipo corretto o non sono corretti, oppure se la matricola è già presente"""

    def inserisci(self, studente, note=""):
        # verifico che lo studente sia effettivamente un oggetto della classe Studente,
        # se è gia presente e se le note sono di tipo stringa
        if type(studente) == Studente and studente.matricola not in self.stud and type(note) == str:
            self.stud[studente.matricola] = (studente, note)
            return True # l'inserimento è stato effettuato con successo
        else:
            return False # lo studente non è un oggetto della classe Studente oppure le note non sono di tipo stringa


    """Elimina lo studente con matricola "matricola"
    :param matricola: la matricola dello studente da eliminare
    :return: True se l'eliminazione è stata effettuata con successo,
    :return: False se la matricola non è presente"""


    def elimina(self, matricola):
        if matricola in self.stud: # controllo se la la chiave è presente nel dizionario (questo controllo si effettuerà spesso negli altri metodi)
            del self.stud[matricola]
            return True # l'eliminazione dello studente è stata effettuata con successo
        else:
            return False # lo studente non è presente nel dizionario stud 
    
    
    """Restituisce le note dello studente con matricola "matricola"
    :param matricola: la matricola dello studente di cui si vogliono le note
    :return: le note dello studente
    :return: None se la matricola non è presente"""
    

    def get_note(self, matricola):
        if matricola in self.stud:
            studente_info = self.stud.get(matricola)
            if len(studente_info) == 2: # controllo che i valori della matricola siano 2 (oggetto studente e note)
                return studente_info[1]  # restituisce le note (anche se la stringa è vuota)
        else:
            return None # la matricola non è presente nel dizionario stud


    """ Restituisce la lista degli studenti
    :return: la lista delle matricole degli studenti"""


    def get_studenti(self):
        matricole = self.stud.keys() # col metodo .keys() raggruppo tutte le matricole
        lista_stud = list(matricole) # e le converto in una lista
        return lista_stud


    """Modifica le note dello studente con matricola "matricola"
    :param matricola: la matricola dello studente da modificare
    :param nota: la nuova nota da inserire (stringa)
    :return: True se la modifica è stata effettuata con successo,
    :return: False se la matricola non è presente"""

    def modifica_note(self, matricola, nota):
        if matricola in self.stud:
            if type(nota) != str:
                return False # la nota non è una stringa
            else:
                self.stud[matricola] = (self.stud[matricola][0], nota) # riassegno i valori inserendo la nuova nota
                return True # la modifica è stata effettuata con successo
        else:
            return False # la matricola non è presente nel dizionario stud


    """Restituisce una stringa contenente tutti gli studenti nell'archivio separati dal carattere "a capo" --> "\n" """
    
    def __str__ (self):
        stringa_stud = "" # stringa vuota dove man mano si accumulano gli studenti
        for studente in self.stud.values(): # itero sui valori del dizionario perché le informazioni dello studente risiedono all'interno del primo valore della chiave
            stringa_stud += str(studente[0]) + "\n" # nel main non è richiesto di inserire le note (studente[1])
        return stringa_stud


    """Restituisce lo studente con matricola "matricola"
    :param matricola: la matricola dello studente da estrarre
    :return s: l'oggetto studente'
    :return None: se lo studente non è presente nell'archivio"""

    def studente(self, matricola):
        if matricola in self.stud:
            s = self.stud[matricola][0] # assegno ad s l'oggetto studente accedendo direttamente al primo valore associato alla chiave
            return s
        else:
            return None # la studente non è presente nel dizionario stud

    """Aggiunge un nuovo esame superato (codice, voto) alla lista esami dello studente con matricola "matricola" 
    :param matricola: la matricola dello studente
    :param codice: il codice dell'esame
    :param voto: il voto dell'esame
    :return: True se l'inserimento è andato a buon fine
    :return: False se si è verificato un errore (es. il codice è già presente)"""

    def registra_esame(self, matricola, codice, voto):
        if matricola in self.stud:
            studente_oggetto = self.studente(matricola) # chiamata alla funzione "studente" della classe Archivio
            # così posso richiamare il metodo già esistente della classe Studente (i controlli li effettua quest'ultimo)
            return studente_oggetto.registra_esame(codice, voto) # se l'inserimento va a buon fine, la chiamata al metodo restituirà True
        else:
            return False # la matricola non è presente nel dizionario stud           


    """Modifica il voto dell'esame con codice "codice" con il nuovo voto "voto" dello studente con matricola "matricola"
    :param matricola: la matricola dello studente
    :param codice: il codice dell'esame da modificare
    :param voto: il nuovo voto dell'esame
    :return: True se la modifica è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)"""

    def modifica_voto(self, matricola, codice, voto): # stesso approccio adottato per il metodo precedente
        if matricola in self.stud:
            studente_oggetto = self.studente(matricola) # chiamata al metodo "studente" della classe Archivio
            # così posso richiamare il metodo già esistente della classe Studente (i controlli li effettua quest'ultimo)
            return studente_oggetto.modifica_voto(codice, voto) # se la modifica va a buon fine, la chiamata al metodo restituirà True
        else:
            return False # la matricola non è presente nel dizionario stud    


    """Cancella l'esame con codice "codice" allo studente con matricola "matricola"
    :param matricola: la matricola dello studente
    :param codice: il codice dell'esame da cancellare
    :return: True se la cancellazione è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)"""

    def cancella_esame(self, matricola, codice): # stesso approccio adottato per il metodo precedente
        if matricola in self.stud:
            studente_oggetto = self.studente(matricola) # chiamata alla funzione "studente" della classe Archivio
            # così posso richiamare il metodo già esistente della classe Studente (i controlli li effettua quest'ultimo)
            return studente_oggetto.cancella_esame(codice) # se la cancellazione va a buon fine, la chiamata al metodo restituirà True
        else:
            return False # la matricola non è presente nel dizionario stud 


    """Restituisce la media dello studente con matricola "matricola"
    :param stud: il dizionario degli studenti
    :param matricola: la matricola dello studente
    :return f: f è un valore float che fornisce la media dei voti negli esami sostenuti
    :return None: se lo studente non è presente"""

    def media(self, matricola): # stesso approccio adottato per il metodo precedente
        if matricola in self.stud:
            studente_oggetto = self.studente(matricola) # chiamata al metodo "studente" della classe Archivio
            # così posso richiamare il metodo già esistente della classe Studente (i controlli li effettua quest'ultimo)
            return studente_oggetto.media() # se il caldolo della media va a buon fine, la chiamata al metodo restituirà f
        else:
            return None # la matricola non è presente nel dizionario stud 


    """Crea la lista degli studenti che hanno superato l'insegnamento "codice" con
    valutazione uguale o superiore alla soglia.
    :param codice: il codice dell'insegnamento di interesse
    :param soglia: la soglia di voto minima (>=) per essere compresi nella lista finale
    :return lista: la lista degli studenti promossi con voto >= soglia"""

    def lista_studenti_promossi(self, codice, soglia = 18):
        if type(codice) != str:
            return False
        else:
            lista = []
            for matricola, (studente, note) in self.stud.items(): # itero direttamente sugli elementi del dizionario
                valutazione = studente.get_voto(codice) # chiamata al metodo (get_voto) della classe Studente
                if valutazione != None and valutazione >= soglia: # verifico che la valutazione sia esistente e maggiore o uguale alla soglia
                    lista.append(matricola) # aggiungo lo studente alla lista
            return lista

    
    """Conta quanti studenti hanno superato l'insegnamento "codice" con
    valutazione uguale o superiore alla soglia.
    :param codice: il codice dell'insegnamento di interesse
    :param soglia: la soglia di voto minima (>=) per essere compresi nel computo
    :return n: il numero degli studenti promossi con voto >= soglia"""

    def conta_studenti_promossi(self, codice, soglia = 18):
        n = len(self.lista_studenti_promossi(codice, soglia)) # chiamata al precedente metodo
        return n

    """Crea la lista degli studenti che hanno una media superiore alla soglia
    :param soglia: la soglia di media minima (>=) per essere compresi nella lista finale
    :return lista: la lista degli studenti promossi con media >= soglia"""

    def lista_studenti_media(self, soglia = 18):
        lista = []
        for matricola, (studente, note) in self.stud.items(): # itero direttamente sugli elementi del dizionario
            media = studente.media() # chiamata al metodo (media) della classe Studente
            if media != None and media >= soglia: # verifico che la media sia esistente e maggiore o uguale alla soglia
                lista.append(matricola)
        return lista


    """Salva l'archivio in un file di nome nomefile con un formato a piacere e gestendo eventuali eccezioni
    :param nomefile: il nome del file in cui salvare l'archivio
    :return: True se il salvataggio è andato a buon fine
    :return: False se si è verificato un errore"""

    def salva(self, nomefile):
        try:
            with open(nomefile, "w") as f:
                for matricola, (studente, note) in self.stud.items(): # itero direttamente sugli elementi del dizionario
                    lista_esami = str(studente.get_listaesami()) # chiamata al metodo (get_listaesami) della classe Studente
                    linea = studente.cognome + ":" + studente.nome + ":" + str(studente.matricola) + ":" + lista_esami + ":" + note + "\n" # formattazione degli elementi della stringa con ":"
                    f.write(linea) # inserisco la linea corrispondente allo studente nel file
                return True # il salvataggio è andato a buon fine
        except(IOError):
            return False # eccezione sollevata in caso di errore di salvataggio del file
        except(ValueError):
            return False # eccezione sollevata nel caso in cui i dati non siano formattati correttamente per la conversione in stringa


    """Carica l'archivio da un file di nome nomefile con un formato a piacere e gestendo eventuali eccezioni
    :param nomefile: il nome del file da cui caricare l'archivio
    :return: True se il caricamento è andato a buon fine
    :return: False se si è verificato un errore"""
    
    def carica(self, nomefile):
        try:
            with open(nomefile, "r") as f:
                for linea in f:
                    info_studente = linea.strip().split(":") # divido la linea in base ai due punti (in base alla formattazione utilizzata dal metodo salva)
                    # estraggo le informazioni dallo split
                    cognome = info_studente[0]
                    nome = info_studente[1]
                    matricola = int(info_studente[2])

                    lista_esami = eval(info_studente[3]) # pur essendo un approccio rischioso, la funzione eval() riconosce la stringa info_studente[3] come una lista di tuple e la converte,
                    # soluzione approcciata per immediatezza anche se poco sicura

                    note = info_studente[4]
                    studente = Studente(cognome, nome, matricola) # creo un nuovo oggetto Studente con le informazioni estratte e lo inserisco nell'archivio
                    studente.set_listaesami(lista_esami)
                    self.inserisci(studente, note)
            return True # il caricamento è andato a buon fine
        except(IOError): 
            return False # eccezione sollevata in caso di errore di caricamento del file
        except(ValueError): 
            return False # eccezione sollevata nel caso in cui i dati non abbiano i tipi corretti