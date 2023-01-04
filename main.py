import tweepy
from Historic_Crypto import LiveCryptoData
from Historic_Crypto import HistoricalData
import emoji

API_KEY = 'XXXXXXXX'
API_SECRET = 'XXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXX'

#Connection
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN,
                                ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Récupération des valeurs
new = LiveCryptoData('ETH-USD').return_data()
a = new.values
prix_recent = a[0][-2]


#Récupère les dernières valeurs journalières précédentes
precedent = HistoricalData('ETH-USD', 86400,
                           '2023-01-01-00-00').retrieve_data()


#récupération des valeurs précédentes
valeur_precedente = precedent.values
prix_hier = valeur_precedente[-1][-3]

#Calculer les taux de change du prix / volume
''' Calculer les variations de prix avec les variables'''

#Pour le prix unitaire
taux_d_evolution_float = (
    (float(prix_recent) - float(prix_hier)) / float(prix_hier)) * 100
taux = round(taux_d_evolution_float, 2)

#Arrondir le volume
c = float(a[0][2])
c = int(c)

#Pour le volume
volumeactuel = c
volumehier = float(valeur_precedente[-1][-1])
volumehier = int(volumehier)
taux_ev_vol = ((c - volumehier) / volumehier) * 100

#Arrondir le prix à l'unité
b = float(a[0][-2])
b = int(b)

###Envoyer sur  Twitter Positif ou négatif
if taux <= 0.0000:
    if taux_ev_vol <= 0.00000:
        api.update_status(
            emoji.emojize("$ETH PRICE : $" + str(b) + "\n" + "Change 24h : " +
                          str(taux) + "% :chart_decreasing:" +
                          "\n24h Trading Volume : $" + str(c) + "\nChange : " +
                          str(int(taux_ev_vol)) + "% :chart_decreasing: \n" +
                          "#ethereum #ETH"
                          ))

    else:
        api.update_status(
            emoji.emojize("$ETH PRICE : $" + str(b) + "\nChange 24h : " +
                          str(taux) + "% :chart_decreasing:" +
                          "\n24h Trading Volume : $" + str(c) +
                          "\nChange : +" + str(int(taux_ev_vol)) +
                          "% :chart_increasing:\n" + "#ethereum #ETH" ))

else:
    if taux_ev_vol <= 0.00000:
        api.update_status(
            emoji.emojize("$ETH PRICE : $" + str(b) + "\n Change 24h : +" +
                          str(taux) + " % :chart_increasing:" +
                          "\n24h Trading Volume : $" + str(c) + "\nChange : " +
                          str(int(taux_ev_vol)) + "% :chart_increasing:\n" +
                          "#ethereum #ETH" ))

    else:
        api.update_status(
            emoji.emojize("$ETH PRICE : $" + str(b) + "\nChange 24h :+" +
                          str(taux) + "% :chart_increasing:" +
                          "\n24h Trading Volume : $" + str(c) +
                          "\nChange : +" + str(int(taux_ev_vol)) +
                          "% :chart_increasing:\n" + "#ethereum #ETH"))
