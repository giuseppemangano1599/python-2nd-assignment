#########################################################################################################################
# Terzo assignment in itinere del corso "Programmazione e Analisi dati (A. A. 2023/24) - 622AA-23"                      #
# Codice scritto dallo studente Giuseppe Mangano - Matricola: 674125 - Università di Pisa (g.mangano3@studenti.unipi.it)#
#########################################################################################################################

# GUI di archivio.py
from archivio import *
import tkinter as tk
from tkinter import messagebox, simpledialog # quest'ultimo modulo è stato importato per rendere il codice più snello

class myApp:
    # costruttore
    def __init__(self, root):
        self.root = root
        self.archivio = Archivio()
        self.root.title("Registro Archivio Studenti")
        self.file = "archivio.txt"
        
        # lista studenti
        self.box_studenti = tk.Listbox(self.root, width = 100)
        self.box_studenti.grid(row = 0, column = 0, columnspan = 6, padx = 10, pady = 10, sticky = "nsew")

        # frame bottoni
        self.contenitore_bottoni = tk.Frame(self.root, relief = tk.RAISED, borderwidth = 1)
        self.contenitore_bottoni.grid(row = 1, column = 0, columnspan = 6, padx = 10, pady = 10, sticky = "nsew")

        # bottoni
        self.bottone_inserisci_studente = tk.Button(self.contenitore_bottoni, text = "Inserisci studente", background = "light green")
        self.bottone_inserisci_studente.pack(fill = tk.X, pady = 5)
        self.bottone_inserisci_studente.bind("<Button-1>", self.inserisci_studente)


        self.bottone_modifica_studente = tk.Button(self.contenitore_bottoni, text = "Modifica studente", background = "orange")
        self.bottone_modifica_studente.pack(fill = tk.X, pady = 5)
        self.bottone_modifica_studente.bind("<Button-1>", self.modifica_studente)


        self.bottone_elimina_studente = tk.Button(self.contenitore_bottoni, text = "Elimina studente", background = "red")
        self.bottone_elimina_studente.pack(fill = tk.X, pady = 5)
        self.bottone_elimina_studente.bind("<Button-1>", self.elimina_studente)


        self.bottone_inserisci_esame = tk.Button(self.contenitore_bottoni, text = "Inserisci esame", background = "light green")
        self.bottone_inserisci_esame.pack(fill = tk.X, pady = 5)
        self.bottone_inserisci_esame.bind("<Button-1>", self.inserisci_esame)


        self.bottone_modifica_esame = tk.Button(self.contenitore_bottoni, text = "Modifica esame", background = "orange")
        self.bottone_modifica_esame.pack(fill = tk.X, pady = 5)
        self.bottone_modifica_esame.bind("<Button-1>", self.modifica_esame)


        self.bottone_elimina_esame = tk.Button(self.contenitore_bottoni, text = "Elimina esame", background = "red")
        self.bottone_elimina_esame.pack(fill = tk.X, pady = 5)
        self.bottone_elimina_esame.bind("<Button-1>", self.elimina_esame)


        self.bottone_media = tk.Button(self.contenitore_bottoni, text = "Calcola media", background = "yellow")
        self.bottone_media.pack(fill = tk.X, pady = 5)
        self.bottone_media.bind("<Button-1>", self.media)


        self.bottone_salva_file = tk.Button(self.contenitore_bottoni, text = "Salva su file (.txt)", background = "light blue")
        self.bottone_salva_file.pack(fill = tk.X, pady = 5)
        self.bottone_salva_file.bind("<Button-1>", self.salva_file)


        self.bottone_carica_file = tk.Button(self.contenitore_bottoni, text = "Carica da file (.txt)", background = "white")
        self.bottone_carica_file.pack(fill = tk.X, pady = 5)
        self.bottone_carica_file.bind("<Button-1>", self.carica_file)


        self.bottone_esci = tk.Button(self.contenitore_bottoni, text = "Esci")
        self.bottone_esci.pack(fill = tk.X, pady = 5)
        self.bottone_esci.bind("<Button-1>", self.esci)


    # metodo che serve a ricaricare il box studenti ogni qual volta si effettua un'operazione sul registro
    def ricarica_box(self):
        self.box_studenti.delete(0, tk.END) #svuoto il box studenti
        for matricola in sorted(self.archivio.get_studenti()): # ordino gli studenti in ordine crescente per numero di matricola
            studente = self.archivio.studente(matricola)
            note = self.archivio.get_note(matricola)
            stringa = (studente.get_cognome() + " " + studente.get_nome() + " - Matricola: " + str(matricola)+ " - Esami: " + str(studente.get_listaesami()) + " - Note: " + note)
            self.box_studenti.insert(tk.END, stringa)


    # per ovvi motivi, i metodi della gui sono effettuano un richiamo ai metodi delle classi Studente e Archivio contenute in archivio.py
    def inserisci_studente(self, evento):
        while True:
            try:
                cognome = simpledialog.askstring("Inserimento cognome", "Inserisci il cognome dello studente:")
                if cognome is None:
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                    break # esco dal loop se l'utente annulla l'operazione
                
                nome = simpledialog.askstring("Inserimento nome", "Inserisci il nome dello studente:")
                if nome is None:
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                    break

                matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente:")
                if matricola is None:
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                    break

                studente = Studente(cognome, nome, matricola)

                note = simpledialog.askstring("Inserimento note", "Inserisci le note relative allo studente:")
                if note is None:
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                    break
                # f"{cognome} {nome} - Matricola: {matricola} - Note: {note}"
                if self.archivio.inserisci(studente, note) == True:
                    self.box_studenti.insert(tk.END, f"{cognome} {nome} - Matricola: {matricola} - Note: {note}")
                    messagebox.showinfo("Inserimento avvenuto con successo", f"Lo studente {cognome} {nome} è stato aggiunto con la matricola {matricola}.")
                    break  # esco dal loop se l'inserimento è avvenuto con successo
                else:
                    messagebox.showerror("Inserimento annullato", "Non è stato possibile inserire lo studente.\nRiprova.")
            except (ValueError,TypeError) as e:
                    messagebox.showerror("Inserimento errato", f"Non è stato possibile inserire lo studente.\n{e}")

    def modifica_studente(self, evento):
        while True:
            matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente che vuoi modificare:")
            if matricola is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break
            if self.archivio.elimina(matricola) == True:
                self.inserisci_studente(None) # passo di None come argomento "evento" fittizio sennò avviene un'eccezione
                self.ricarica_box()
                break
            else:
                messagebox.showerror("Modifica annullata", "Non è stato possibile modificare lo studente. Controlla se hai inserito correttamente la matricola e riprova.")
                break


    def elimina_studente(self, evento):
        while True:
            matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente che vuoi eliminare:")
            if matricola is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break
            studente = self.archivio.studente(matricola)
            if self.archivio.elimina(matricola) == True:
                self.ricarica_box()
                messagebox.showinfo("Eliminazione avvenuta con successo", f"Lo studente {studente.get_cognome()} {studente.get_nome()} è stato eliminato.")
                break 
            else:
                messagebox.showerror("Eliminazione annullata", "Non è stato possibile eliminare lo studente. Controlla se hai inserito correttamente la matricola.")
                break

    def inserisci_esame(self, evento):
        while True:
            matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente:")
            if matricola is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break
            if self.archivio.studente(matricola) == None:
                messagebox.showerror("Inserimento annullato.", "Non è stato possibile inserire l'esame. Controlla il voto o se hai inserito correttamente la matricola")
                break

            codice = simpledialog.askstring("Inserimento codice", "Inserisci il codice dell'esame che vuoi aggiungere:")
            if codice is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            voto = simpledialog.askinteger("Inserimento voto", "Inserisci il voto dell'esame:")
            if voto is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            if self.archivio.registra_esame(matricola, codice, voto) == True:
                self.ricarica_box()
                messagebox.showinfo("Inserimento avvenuto con successo", f"L'esame {codice} è stato aggiunto per la matricola {matricola} con la valutazione di {voto}.")
                break 
            else:
                messagebox.showerror("Inserimento annullato.", "Non è stato possibile inserire l'esame. Controlla il voto o se hai inserito correttamente la matricola.")
                break


    def modifica_esame(self, evento):
        while True:
            matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente:")
            if matricola is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            codice = simpledialog.askstring("Inserimento codice", "Inserisci il codice dell'esame che vuoi modificare:")
            if codice is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            voto = simpledialog.askinteger("Inserimento voto", "Inserisci il voto dell'esame:")
            if voto is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            if self.archivio.modifica_voto(matricola, codice, voto) == True:
                self.ricarica_box()
                messagebox.showinfo("Modifica avvenuta con successo", f"L'esame {codice} è stato modificato per la matricola {matricola} + con la valutazione di {voto}.") 
                break
            else:
                messagebox.showerror("Modifica annullata", "Non è stato possibile modificare l'esame. Controlla il voto (>= 18) o se hai inserito correttamente la matricola")
                break


    def elimina_esame(self, evento):
        while True:
            matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente:")
            if matricola is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            codice = simpledialog.askstring("Inserimento codice", "Inserisci il codice dell'esame che vuoi eliminare:")
            if codice is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            if self.archivio.cancella_esame(matricola, codice) == True:
                self.ricarica_box()
                messagebox.showinfo("Eliminazione avvenuta con successo", f"L'esame {codice} è stato eliminato per la matricola {matricola}.")
                break 
            else:
                messagebox.showerror("Eliminazione annullata", "Non è stato possibile eliminare l'esame. Controlla se lo studente ha sostenuto l'esame o se hai inserito correttamente la matricola")
                break


    def media(self, evento):
        while True:
            matricola = simpledialog.askinteger("Inserimento matricola", "Inserisci la matricola dello studente di cui vuoi calcolare la media:")
            if matricola is None:
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                break

            studente = self.archivio.studente(matricola)
            media = self.archivio.media(matricola)
            if media != None:
                messagebox.showinfo("Calcolo della media", f"Lo studente {studente.get_cognome()} {studente.get_nome()} ha la media del {media}.") 
                break
            else:
                messagebox.showerror("Errore media", "Si è verificato un errore durante il calcolo della media.")
                break


    def salva_file(self, evento):
        try:
            self.archivio.salva(self.file)
            messagebox.showinfo("Salvataggio archivio", "L'archivio degli studenti è stato salvato correttamente.")
        except Exception:
            messagebox.showerror("Errore salvataggio", "Si è verificato un errore durante il salvataggio dell'archivio.")


    def carica_file(self, evento):
        try:
            self.archivio.carica(self.file)
            self.ricarica_box()
            messagebox.showinfo("Caricamento archivio", "L'archivio degli studenti è stato caricato correttamente..")
        except Exception:
            messagebox.showerror("Errore caricamento", "Si è verificato un errore durante il caricamento dell'archivio.")


    def esci(self, evento):
        self.root.destroy()

root = tk.Tk()
app = myApp(root)
root.mainloop()