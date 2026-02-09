# Health Care Costs Prediction - Regression Analysis

## 1. Introduzione
Il presente progetto ha l'obiettivo di sviluppare un modello di Machine Learning basato su una rete neurale per la predizione dei costi sanitari individuali. Il dataset fornito contiene informazioni demografiche e biometriche (età, sesso, BMI, numero di figli, stato di fumatore e regione di residenza). La sfida principale consiste nel minimizzare il **Mean Absolute Error (MAE)** al di sotto della soglia di $3500.

## 2. Exploratory Data Analysis (EDA)
Una fase cruciale del progetto è stata l'analisi approfondita delle caratteristiche (feature) attraverso tecniche di visualizzazione avanzata:

* **Analisi Univariata:** È stata osservata una distribuzione asimmetrica delle spese mediche, con una forte concentrazione verso valori bassi e una coda lunga verso i costi elevati.
* **Analisi Bivariata e Multivariata:** Attraverso l'uso di scatter plot e box plot, è emersa una netta separazione dei costi basata sullo stato di fumatore.
* **Visualizzazione 3D:** L'impiego di grafici tridimensionali (Età, BMI, Smoker) ha permesso di identificare la natura non lineare del problema, evidenziando come i costi non aumentino semplicemente per somma di fattori, ma per interazione sinergica.

## 3. Feature Engineering e Preprocessing
L'analisi della **Matrice di Correlazione di Pearson** ha mostrato che, sebbene lo stato di fumatore abbia la correlazione più alta (0.79), l'impatto del BMI è condizionato dallo stato di fumo. 

Sulla base di queste osservazioni, sono state apportate le seguenti ottimizzazioni:
1.  **Mappatura Categorica:** Conversione di `sex` e `smoker` in valori binari e applicazione di **One-Hot Encoding** per la variabile `region`.
2.  **Normalizzazione:** Implementazione di un layer di normalizzazione per garantire che variabili con scale differenti (es. età vs spese) non influenzino negativamente la convergenza del modello.

## 4. Architettura del Modello
Il modello predittivo è basato su una rete neurale sequenziale (TensorFlow/Keras):
* **Input Layer:** Layer di normalizzazione adattato al dataset di training.
* **Hidden Layers:** Tre strati densi (128, 64, 32 neuroni) con funzione di attivazione **ReLU**, necessaria per modellare le relazioni non lineari identificate durante l'EDA.
* **Output Layer:** Un singolo neurone con attivazione lineare per la regressione dei costi.
* **Ottimizzazione:** Utilizzo dell'ottimizzatore **Adam** (learning rate 0.005) e funzione di perdita MAE.

## 5. Analisi dei Risultati e Residui
L'efficacia del modello è stata verificata tramite:
* **Prediction Error Plot:** Valutazione della vicinanza dei punti alla diagonale di predizione perfetta.
* **Analisi dei Residui:** Verifica della distribuzione degli errori. L'integrazione delle feature di interazione ha permesso di correggere la sottostima sistematica dei costi elevati precedentemente osservata nei casi "high-risk".

## 6. Conclusioni
Il progetto dimostra che l'accuratezza di un modello di regressione non dipende esclusivamente dalla complessità dell'algoritmo, ma dalla profonda comprensione della struttura dei dati. L'identificazione delle interazioni tra fumo, età e BMI è stata la chiave per superare i requisiti di performance richiesti.