# SMS Spam Detection: Professional NLP Pipeline

Questo progetto implementa un classificatore binario ad alte prestazioni per identificare messaggi SMS come **"ham"** (legittimi) o **"spam"**.


## 1. Strategie di Modellazione e Architettura

Per risolvere il task, è stata scelta un'architettura basata su **Deep Learning Ricorrente (RNN)**, preferita ai modelli statistici classici per la sua capacità di catturare dipendenze semantiche a lungo raggio.

### Componenti della Rete Neutrale:
1. **Input Layer (String-Safe):** Utilizzo di `tf.string` per accettare testo grezzo direttamente, eliminando la necessità di preprocessing esterno e rendendo il modello autonomo (Self-Contained).
2. **TextVectorization Layer:** Integrazione della tokenizzazione e vettorizzazione direttamente nel grafo del modello. Questo garantisce che la mappatura parola-indice sia identica tra fase di training e produzione.
3. **Embedding Layer (64 dim):** Trasformazione degli indici delle parole in vettori densi in uno spazio continuo, permettendo al modello di apprendere relazioni di similarità tra termini.
4. **Bidirectional LSTM (64 unità):** L'uso della bidirezionalità permette alla rete di leggere il messaggio in entrambe le direzioni, fondamentale per comprendere il contesto di SMS brevi e informali.
5. **Regularization Stack:** Inserimento di un layer di **Dropout (0.5)** per prevenire l'overfitting, garantendo che il modello generalizzi bene su messaggi mai visti prima.

## 2. Pipeline di Addestramento e Ottimizzazione

La strategia di training è stata impostata per massimizzare l'efficienza computazionale e la stabilità del modello:

1. **Performance Pipeline (tf.data):** Utilizzo di `prefetch` e `autotune` per caricare i dati in modo asincrono, accelerando i tempi di addestramento.
2. **Dynamic Learning Rate:** Implementazione di `ReduceLROnPlateau`. Se la perdita di validazione non migliora, il tasso di apprendimento viene ridotto automaticamente per "affinare" i pesi.
3. **Early Stopping:** Monitoraggio della `val_loss` con ripristino dei migliori pesi trovati per evitare che il modello impari il rumore del set di training.

## 3. Inferenza in Produzione (MLOps Oriented)

A differenza degli approcci accademici standard, l'inferenza è stata ottimizzata per scenari reali:

1. **Low-Latency Inference:** Invece di `.predict()`, viene utilizzata la chiamata diretta al modello (`model(tensor, training=False)`). Questo riduce l'overhead per l'inferenza su singolo messaggio, rendendo il sistema adatto a integrazioni in tempo reale.
2. **Type Safety:** La gestione esplicita dei tensori di stringhe previene errori di compatibilità comuni nei deployment su ambienti diversi come Docker o servizi Cloud.

## 4. Risultati e Metriche

Il modello viene valutato su tre metriche chiave, essenziali per un filtro spam professionale:
* **Accuracy:** Capacità generale di classificazione corretta.
* **Precision:** Cruciale per minimizzare i "Falsi Positivi" (evitare che messaggi importanti finiscano in spam).
* **Recall:** Capacità di intercettare il maggior numero possibile di messaggi spam reali.

---
**Sviluppato con rigore metodologico per la sfida FreeCodeCamp "SMS Text Classification".**