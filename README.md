#  Multi-Strategy Markov Meta-Learner (RPS Bot)

Questo algoritmo è un sistema di **Meta-Apprendimento** avanzato progettato per eccellere nel gioco della Morra Cinese (Rock Paper Scissors) contro avversari con diversi profili psicologici e statistici.

---

## Architettura Tecnica

### Modelli di Markov Multi-Ordine
Il bot non si limita a osservare l'ultima mossa, ma analizza pattern di lunghezza variabile (fino a `num_models`).
- **Modelli `opp`**: Analizzano la cronologia dell'avversario per prevedere la sua prossima mossa.
- **Modelli `my`**: Analizzano la nostra cronologia. Essenziale per sconfiggere bot "Mirror" o "Counter-bots" (come Abbey) che cercano di prevedere le nostre mosse.

### Il Sistema delle Triple Strategie (P0, P1, P2)
Per ogni modello di Markov, il bot genera tre diverse risposte tattiche:

1. **P0 (Direct Response)**: La contromossa logica alla predizione. Se prevediamo "Sasso", giochiamo "Carta".
2. **P1 (Counter-Counter)**: Il "Bluff". Batte la mossa che l'avversario userebbe per battere noi. Ideale contro bot che anticipano la nostra logica.
3. **P2 (Mirror/Tie-break)**: Gioca la mossa prevista dell'avversario. Utile per rompere loop di pareggi e mandare in corto circuito bot reattivi come Kris.

---

## Meccaniche di Ottimizzazione

### Exponential Score Decay
Il sistema utilizza un **decadimento esponenziale dei punteggi (`decay = 0.8`)**.
- **Perché**: Gli avversari cambiano strategia durante i 1000 round.
- **Effetto**: Le vittorie recenti valgono più di quelle passate, permettendo al bot di adattarsi ai cambi di pattern del nemico in pochissimi round.

### Selezione "Greedy" Adattiva
Il bot valuta costantemente tutti i modelli (fino a 24 combinazioni diverse con `num_models=4`) e seleziona istantaneamente quello con l'affidabilità più alta in quel preciso momento del match.

---

## Analisi delle Performance (Benchmark)

| Avversario | Vittorie (P1) | Sconfitte (P2) | Pareggi | Win Rate (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Quincy** | 992 | 3 | 5 | **99.70%** |
| **Kris** | 841 | 106 | 53 | **88.81%** |
| **Mrugesh** | 847 | 152 | 1 | **84.78%** |
| **Abbey** | 709 | 140 | 151 | **83.51%** |

---

## 🛠️ Note sulla Configurazione
Nel dizionario `parms`, il bot è configurato con:
- `num_models: 4`: Analisi di pattern fino all'ordine 3.
- `decay: 0.8`: Bilanciamento ottimale tra memoria storica e reattività immediata.

---
*Sviluppato come soluzione avanzata per la sfida Rock Paper Scissors di FreeCodeCamp. https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors*