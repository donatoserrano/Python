###LISTA DELLA SPESA INTERATTIVA###
shopping_list = {}

#Funzione per eliminare oggetti
def delete_item(list):
    print("Digita l'oggetto da eliminare.")
    to_delete = input()
    if(to_delete in list.keys()):
        list.pop(to_delete)

#Funzione per aggiungere altri oggetti
def add_item(list):
    new_choice = None
    print("Digita l'oggetto e la quantità da aggiungere.")
    item_to_add = input().strip().lower()
    item_quantity = int(input().strip())
    if not item_to_add:
        print("Errore, non hai inserito nessuna parola.")
    elif item_quantity == 0 or item_quantity == None:
        print("Non hai inserito una quantità adatta, riprova")
    elif item_to_add in list.keys():
        print("Oggetto già presente, se vuoi modificarne la quantità, digita 'si'")
        new_choice = input().strip().lower()
        if new_choice == "si": 
            list[item_to_add] = item_quantity
    else: 
        list[item_to_add] = item_quantity


user_word = None

#scrittura lista della spesa
print("Scrivi la tua lista della spesa, premendo invio per ogni elemento e quantità. Una volta finita, digita 'stop'")
while user_word != "stop":
    user_word = input("Oggetto: ").strip().lower()
    if user_word == "stop":
        break
    user_quantity = int(input("Quantità: ").strip())
    if not user_word:
        print("Non hai inserito nessuna parola, riprova.")
        break
    elif user_quantity == None or user_quantity == 0:
        print("Non hai inserito una quantità adatta, riprova")
        break
    elif user_word in shopping_list.keys():
        print("Oggetto già presente, se vuoi modificarne la quantità, digita 'si'")
        user_choice = input().strip().lower()
        if(user_choice == 'si'):
            print("Inserisci la nuova quantità.")
            shopping_list[user_word] = int(input().strip())
            print("Quantità modificata.")
    else:
        shopping_list[user_word] = user_quantity
        print("Oggetto aggiunto!")
print("")
#stampa lista completa
print("Questa è la tua lista della spesa:")
for item, quantity in shopping_list.items():
    print(f"{item}: {quantity} pezzi")
print("Se vuoi eliminare qualcosa digita '1', se vuoi aggiungere qualcos'altro o modificare una quantità digita '2', altrimenti digita '0'")
user_choice = int(input().strip())
if user_choice == 1:
    delete_item(shopping_list)
    print("Questa è la tua lista della spesa modificata:")
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity} pezzi")
elif user_choice == 2:
    add_item(shopping_list)
    print("Questa è la tua lista della spesa modificata:")
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity} pezzi")