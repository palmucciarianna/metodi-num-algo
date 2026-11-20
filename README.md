# 🧮 Palestra Metodi Numerici in Python

[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-brightgreen?logo=github)](https://palmucciarianna.github.io/metodi-num-algo/)
[![Python - Pyodide](https://img.shields.io/badge/Python-Pyodide%20v0.25.0-3776AB?logo=python&logoColor=white)](https://pyodide.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Supported-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Supported-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Supported-11557c)](https://matplotlib.org/)
[![CodeMirror](https://img.shields.io/badge/Editor-CodeMirror-orange)](https://codemirror.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un ambiente interattivo web completo e leggero per esercitarsi, implementare e verificare algoritmi di **Metodi Numerici per l'Intelligenza Artificiale e il Calcolo Scientifico**, direttamente nel browser senza alcuna installazione richiesta.

---

## 🌟 Caratteristiche Principali

- ⚡ **100% Client-Side con WebAssembly**: Esecuzione reale di Python nel browser tramite **Pyodide**, con librerie scientifiche pronte all'uso (**NumPy**, **SciPy**, **Matplotlib**). Nessun server backend o installazione locale di Python necessari.
- 💻 **Editor Professionale**: Integrato con **CodeMirror** (tema Dracula), supporto all'indentazione (4 spazi), evidenziazione della sintassi e gestione dello stato per ogni esercizio.
- 🧪 **Autovalutazione Istantanea**: Ogni algoritmo include uno scheletro guidato (`# to do`) e una suite di test automatici con asserzioni numeriche per verificare immediatamente la correttezza della soluzione implementata.
- 📊 **Visualizzazione Grafica**: Pannello dedicato e ridimensionabile per visualizzare i grafici generati con **Matplotlib** in tempo reale con espansione automatica.
- 🖥️ **Terminale Interattivo**: Console ridimensionabile con visualizzazione chiara dell'output standard (`stdout`), messaggi di sistema ed errori (`stderr`).

---

## 📚 Algoritmi Inclusi

L'applicazione include esercizi guidati suddivisi nelle principali aree del calcolo numerico:

### 1. Zeri di Funzione
- **Metodo di Bisezione**: Ricerca dello zero su intervallo $[a, b]$ con verifica del teorema di esistenza degli zeri e calcolo teorico delle iterazioni.
- **Falsa Posizione (Regula Falsi)**: Algoritmo basato sulla retta secante con controllo di convergenza su residuo e scarto.
- **Metodo delle Corde**: Iterazione funzionale con coefficiente angolare costante.
- **Metodo di Newton**: Metodo delle tangenti ad ordine di convergenza quadratico tramite derivata prima analitica.
- **Newton Modificato**: Adattamento per zeri a molteplicità $m > 1$.
- **Metodo delle Secanti**: Approssimazione discreta della derivata a due punti iniziali.
- **Stima dell'Ordine di Convergenza**: Calcolo asintotico dell'ordine di convergenza $p$ a partire dalle iterazioni.

### 2. Sistemi di Equazioni Non Lineari
- **Newton-Raphson per Sistemi**: Risoluzione iterativa multidimensionale con calcolo della matrice Jacobiana ad ogni iterazione.
- **Newton-Raphson a Jacobiana Costante (Corde)**: Riduzione dell'onere computazionale valutando la Jacobiana unicamente al primo passo.
- **Newton-Shamanskii**: Aggiornamento periodico della matrice Jacobiana ogni $k$ iterazioni.

### 3. Sistemi Lineari (Metodi Iterativi)
- **Metodo di Jacobi**: Decomposizione $A = D - E - F$, calcolo del raggio spettrale $\rho(T_J)$ e soluzione iterativa.
- **Metodo di Gauss-Seidel**: Iterazione con matrice di iterazione triangolare inferiore e raggio spettrale $\rho(T_{GS})$.
- **Gauss-Seidel SOR (Successive Over-Relaxation)**: Accelerazione della convergenza tramite parametro di rilassamento $\omega$.

### 4. Ottimizzazione & Metodi del Gradiente
- **Steepest Descent (Metodo del Gradiente)**: Ricerca lungo la direzione di massima discesa per matrici simmetriche e definite positive con step-size ottimale $\alpha_k$.
- **Gradiente Coniugato (Conjugate Gradient)**: Ottimizzazione lungo direzioni $A$-ortogonali (coniugate) per convergenza rapida.

### 5. Problemi ai Minimi Quadrati (Least Squares)
- **Equazioni Normali**: Risoluzione di $A^T A x = A^T b$ mediante fattorizzazione di Cholesky ($L L^T$).
- **Fattorizzazione QR**: Risoluzione stabile tramite decomposizione $A = Q R$ e sistema triangolare superiore.
- **Decomposizione a Valori Singolari (SVD)**: Risoluzione ai minimi quadrati con pseudoinversa di Moore-Penrose e soglia numerica sui valori singolari.

### 6. Interpolazione Polinomiale
- **Polinomi Base di Lagrange**: Calcolo dei polinomi fondamentali $L_j(x)$ sui nodi assegnati.
- **Valutazione Interpolante di Lagrange**: Costruzione e valutazione della combinazione lineare polinomiale sui nodi di valutazione.

### 7. Playground & Utility
- **Playground Proprietà Matrici**: Spazio libero per analizzare proprietà matriciali essenziali (simmetria, definita positività, dominanza diagonale stretta, condizionamento, autovalori).

---

## 🚀 Come Utilizzare la Palestra

Non è necessario installare Python, compilatori o pacchetti pip. È sufficiente un qualsiasi browser web moderno (Chrome, Firefox, Safari, Edge).

### Metodo 1: Apertura Diretta
1. Clona o scarica il repository:
   ```bash
   git clone https://github.com/palmucciarianna/metodi-num-algo.git
   cd metodi-num-algo
   ```
2. Fai doppio clic su `metodi-num-algo.html` o aprilo con il tuo browser preferito.

### Metodo 2: Server Locale (Consigliato)
Per evitare eventuali restrizioni dei browser sui file locali (`file://`):
```bash
# Avvio di un server HTTP locale con Python
python3 -m http.server 8000
```
Apri il browser all'indirizzo:
```text
http://localhost:8000/metodi-num-algo.html
```

### Metodo 3: GitHub Pages (Live Demo)
L'applicazione è accessibile online direttamente dal browser, senza installare nulla:
🔗 **[https://palmucciarianna.github.io/metodi-num-algo/](https://palmucciarianna.github.io/metodi-num-algo/)**

---

## 🛠️ Guida all'Uso degli Esercizi

1. **Seleziona un esercizio** dal menu laterale a sinistra.
2. Esamina il template di codice fornito e individua i placeholder `# to do`.
3. Implementa i passaggi matematici richiesti.
4. Clicca sul pulsante verde **▶ Valuta Codice (Run)** in alto a destra.
5. Leggi il riscontro nel terminale:
   - Se l'implementazione supera tutti i controlli:
     ```text
     ✓ [Nome Metodo] corretto!
     ⭐⭐⭐ VALUTAZIONE COMPLETATA CON SUCCESSO! ⭐⭐⭐
     ```
   - In caso di errore o divergenza, il terminale mostrerà l'eccezione o l'asserzione fallita per guidarti nella correzione.

---

## 🗂️ Struttura del Repository

```text
metodi-num-algo/
├── index.html              # Entry point per GitHub Pages (Web application)
├── metodi-num-algo.html    # Web application completa (UI, motore Pyodide, esercizi e test)
└── README.md               # Documentazione e guida al progetto
```

---

## 🧰 Tecnologie Utilizzate

- **Motore di Esecuzione**: [Pyodide](https://pyodide.org/) (Python 3.12 compilato in WebAssembly)
- **Librerie Numeriche e Grafiche**: NumPy, SciPy, Matplotlib
- **Editor di Codice**: [CodeMirror](https://codemirror.net/) con syntax highlighting per Python e tema Dracula
- **Frontend**: HTML5, CSS3 responsive (Flexbox, pannelli ridimensionabili), JavaScript ES6+

---

## 👩‍💻 Autore

Realizzato per lo studio e la pratica di **Metodi Numerici per l'Intelligenza Artificiale** (Università di Bologna).
