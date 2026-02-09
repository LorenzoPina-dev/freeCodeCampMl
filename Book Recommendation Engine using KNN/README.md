# Sistema di Raccomandazione Libri tramite KNN

Questo progetto implementa un modello di apprendimento automatico per la raccomandazione di libri, basato sull'algoritmo K-Nearest Neighbors (KNN). Il sistema analizza le preferenze degli utenti per identificare titoli simili a quello cercato, utilizzando un approccio di filtraggio collaborativo.

## Struttura del Progetto

Il codice è organizzato nelle seguenti fasi principali:

1. **Importazione e Preparazione dei Dati**
   - Caricamento dei dataset `BX-Books.csv` e `BX-Book-Ratings.csv`.
   - Utilizzo di codifica ISO-8859-1 e delimitatori specifici per la corretta lettura dei file CSV.

2. **Filtraggio e Pulizia**
   - Per garantire la qualità dei suggerimenti, sono stati rimossi i dati meno significativi:
     - Esclusione di utenti con meno di 200 valutazioni totali.
     - Esclusione di libri con meno di 100 valutazioni totali.
   - Rimozione di duplicati basata sulla coppia titolo-utente.

3. **Ingegneria delle Caratteristiche**
   - Creazione di una matrice pivot con i titoli dei libri come indici e gli utenti come colonne.
   - Trasformazione della matrice in un formato sparso (Compressed Sparse Row - CSR) per ottimizzare le prestazioni computazionali e la gestione della memoria.

4. **Modellazione**
   - Implementazione dell'algoritmo `NearestNeighbors` della libreria Scikit-Learn.
   - Configurazione della metrica di distanza basata sulla similitudine del coseno (`cosine`) e utilizzo dell'algoritmo `brute` per il calcolo dei vicini.

5. **Funzione di Raccomandazione**
   - Sviluppo della funzione `get_recommends` che restituisce i 5 titoli più simili a un input dato, corredati dalla relativa distanza statistica.

## Requisiti

- Python 3
- Pandas
- NumPy
- Scikit-Learn
- SciPy

## Risultati

Il modello è stato validato con successo superando i test di precisione sulle raccomandazioni e sulle distanze attese, confermando l'efficacia dell'approccio KNN nel dominio del filtraggio collaborativo.