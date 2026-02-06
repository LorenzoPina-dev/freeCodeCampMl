import random

def update_model(history, model, order, last_move):
    if len(history) > order:
        key = "".join(history[-(order + 1):-1])
        if key not in model:
            model[key] = {'R': 0, 'P': 0, 'S': 0}
        model[key][last_move] += 1

def get_pred(history, model, order):
    if len(history) < order: return random.choice(["R", "P", "S"])
    key = "".join(history[-order:])
    if key in model:
        return max(model[key], key=model[key].get)
    return random.choice(["R", "P", "S"])

'''
def player(prev_play, opponent_history=[], parms={'models': {}, 'scores': {}, 'my_history': [], 'num_models':4, 'decay': 0.8 }):
    # 1. Inizializzazione Dinamica (Conteggio da 1)
    if not prev_play:
        opponent_history.clear()
        parms['my_history'] = []
        # Creiamo 3 varianti per ogni modello: P0, P1, P2
        parms['models'] = {f'{p}_m{i}_{v}': {} for p in ['opp', 'my'] for i in range(1, parms['num_models']) for v in ['P0', 'P1', 'P2']}
        parms['scores'] = {k: 0.0 for k in parms['models'].keys()}
        parms['last_preds'] = {}
        return "R"

    opponent_history.append(prev_play)

    # 2. Update Punteggi con Decay 
    if 'last_preds' in parms:
        for name, pred in parms['last_preds'].items():
            parms['scores'][name] *= parms['decay']
            if pred == prev_play:
                parms['scores'][name] += 1
            else:
                parms['scores'][name] -= 1

    # 3. Training
    for i in range(1, parms['num_models']):
        update_model(opponent_history, parms['models'][f'opp_m{i}_P0'], i, prev_play)
        if len(parms['my_history']) > 1:
            update_model(parms['my_history'], parms['models'][f'my_m{i}_P0'], i, parms['my_history'][-1])

    # 4. Generazione Strategie (P0, P1, P2)
    beat = {"R": "P", "P": "S", "S": "R"}
    preds = {}
    
    for i in range(1, parms['num_models']):
        # Predizione base dell'avversario
        opp_move = get_pred(opponent_history, parms['models'][f'opp_m{i}_P0'], i)
        my_move = get_pred(parms['my_history'], parms['models'][f'my_m{i}_P0'], i)
        
        # Varianti di risposta per modelli OPP
        preds[f'opp_m{i}_P0'] = beat[opp_move]        # Batte la sua mossa predetta
        preds[f'opp_m{i}_P1'] = beat[beat[opp_move]]  # Batte la mossa che batte la sua
        preds[f'opp_m{i}_P2'] = opp_move              # Gioca quello che farà lui (Tie-break)
        
        # Varianti di risposta per modelli MY (Anti-Abbey)
        preds[f'my_m{i}_P0'] = beat[beat[my_move]]    # Triple bluff standard
        preds[f'my_m{i}_P1'] = beat[my_move]          # Bluff semplice
        preds[f'my_m{i}_P2'] = my_move                # Quello che lui si aspetta

    # 5. Selezione del modello migliore (Greedy con Decay)
    best_model = max(parms['scores'], key=parms['scores'].get)
    my_next_move = preds[best_model]

    # 6. Registriamo cosa "prevediamo" che l'avversario faccia per ogni strategia
    # Serve per dare i punti nel prossimo round
    parms['last_preds'] = {}
    lose_to = {"P": "R", "S": "P", "R": "S"}
    for name, my_pred_move in preds.items():
        parms['last_preds'][name] = lose_to[my_pred_move]

    parms['my_history'].append(my_next_move)
    return my_next_move
'''



import random
import math
def update_model(history, model, order, last_move):
    if len(history) > order:
        key = "".join(history[-(order + 1):-1])
        if key not in model:
            model[key] = {'R': 0, 'P': 0, 'S': 0}
        model[key][last_move] += 1

def get_pred(history, model, order):
    if len(history) < order: return random.choice(["R", "P", "S"])
    key = "".join(history[-order:])
    if key in model:
        return max(model[key], key=model[key].get)
    return random.choice(["R", "P", "S"])

def player(prev_play, opponent_history=[], parms={'weights': {}, 'my_history': []}):
    # 1. SETUP NEURALE (Inizializzazione una sola volta)
    if not prev_play:
        opponent_history.clear()
        parms['my_history'] = []
        parms['orders'] = range(1, 6) # Ordini da 1 a 5
        parms['strategies'] = ['P0', 'P1', 'P2']
        # Definiamo le Azioni (i nostri "neuroni" di output)
        parms['actions'] = [f'{p}_m{i}_{s}' for p in ['opp', 'my'] for i in parms['orders'] for s in parms['strategies']]
        
        # Pesi della Rete (Inizializzati a 0.0)
        parms['weights'] = {a: 0.0 for a in parms['actions']}
        parms['models'] = {f'{p}_m{i}': {} for p in ['opp', 'my'] for i in parms['orders']}
        parms['last_preds'] = {}
        parms['last_action'] = None
        return "R"

    # 2. LA COMPONENTE REINFORCEMENT LEARNING (Aggiornamento Pesi)
    # Qui l'agente riceve il feedback dal mondo e aggiorna la sua "conoscenza"
    if parms['last_action'] is not None:
        beat_map = {"R": "P", "P": "S", "S": "R"}
        
        for name, pred in parms['last_preds'].items():
            # Calcolo della Ricompensa (Reward)
            if pred == prev_play:
                reward = 1.0  # Il modello aveva previsto bene l'avversario
            elif beat_map[prev_play] == pred:
                reward = -2.0 # Il modello ha portato a una sconfitta (Penalità)
            else:
                reward = -0.5 # Pareggio
            
            # Regola di Apprendimento (Delta Rule / Perceptron Learning)
            # Alpha è il Learning Rate: 0.3 è veloce per adattarsi a Kris
            alpha = 0.3
            parms['weights'][name] += alpha * (reward - parms['weights'][name])
            
            # Decadimento dei pesi (Weight Decay / L2 Regularization)
            # Impedisce ai pesi di "fossilizzarsi" su un bot vecchio (es. Quincy -> Kris)
            parms['weights'][name] *= 0.9

    opponent_history.append(prev_play)

    # 3. I SENSORI (Markov Models)
    for i in parms['orders']:
        update_model(opponent_history, parms['models'][f'opp_m{i}'], i, prev_play)
        if len(parms['my_history']) > 1:
            update_model(parms['my_history'], parms['models'][f'my_m{i}'], i, parms['my_history'][-1])

    # 4. LA COMPONENTE RETE NEURALE (Feed-Forward e Predizione)
    beat = {"R": "P", "P": "S", "S": "R"}
    lose = {"P": "R", "S": "P", "R": "S"}
    preds = {}
    potential_opp_moves = {}

    for i in parms['orders']:
        o_m = get_pred(opponent_history, parms['models'][f'opp_m{i}'], i)
        m_m = get_pred(parms['my_history'], parms['models'][f'my_m{i}'], i)
        
        # Generazione input per i neuroni (Strategie P0, P1, P2)
        preds[f'opp_m{i}_P0'], potential_opp_moves[f'opp_m{i}_P0'] = beat[o_m], o_m
        preds[f'opp_m{i}_P1'], potential_opp_moves[f'opp_m{i}_P1'] = beat[beat[o_m]], beat[o_m]
        preds[f'opp_m{i}_P2'], potential_opp_moves[f'opp_m{i}_P2'] = o_m, lose[o_m]
        
        preds[f'my_m{i}_P0'], potential_opp_moves[f'my_m{i}_P0'] = beat[beat[m_m]], beat[m_m]
        preds[f'my_m{i}_P1'], potential_opp_moves[f'my_m{i}_P1'] = beat[m_m], m_m
        preds[f'my_m{i}_P2'], potential_opp_moves[f'my_m{i}_P2'] = m_m, lose[m_m]

    # 5. FUNZIONE DI ATTIVAZIONE (Softmax Action Selection)
    # Trasformiamo i pesi in probabilità esponenziali
    # Temperature (T=0.5): più è bassa, più il bot è "sicuro"; più è alta, più è "folle"
    T = 0.5
    exp_w = {a: math.exp(parms['weights'][a] / T) for a in parms['actions']}
    total_w = sum(exp_w.values())
    
    # Selezione probabilistica (Stochastic Policy)
    r = random.uniform(0, total_w)
    upto = 0
    selected_action = parms['actions'][0]
    for a, w in exp_w.items():
        upto += w
        if upto >= r:
            selected_action = a
            break

    my_next_move = preds[selected_action]
    parms['last_action'] = selected_action
    parms['last_preds'] = potential_opp_moves
    parms['my_history'].append(my_next_move)
    
    return my_next_move