# 🧮 Palestra Metodi Numerici in Python

[![Live Demo](https://img.shields.io/badge/Demo-GitHub%20Pages-brightgreen?logo=github)](https://palmucciarianna.github.io/metodi-num-algo/)
[![Python - Pyodide](https://img.shields.io/badge/Python-Pyodide%20v0.25.0-3776AB?logo=python&logoColor=white)](https://pyodide.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Supported-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Supported-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Supported-11557c)](https://matplotlib.org/)

Ambiente web interattivo per implementare, testare e verificare gli algoritmi di **Metodi Numerici per l'Intelligenza Artificiale e il Calcolo Scientifico**, direttamente nel browser senza alcuna installazione.

> 📚 **Materiali del Corso & Laboratori Didattici**:  
> Le formule, le notazioni e i criteri d'arresto seguono fedelmente le **slide della docente** (UniBo). I materiali didattici completi, dispense e prossimamente la sezione con i **laboratori d'esame guidati** saranno raccolti nel repository dedicato:  
> 👉 **[github.com/palmucciarianna/metodinumericiAI](https://github.com/palmucciarianna/metodinumericiAI)**

---

## 🚀 Come farlo funzionare

Non occorre installare Python, né configurare ambienti virtuali o scaricare librerie.

### 1. Online (Consigliato - Immediato)
L'applicazione è pubblicata su GitHub Pages ed è utilizzabile direttamente dal browser:
👉 **[https://palmucciarianna.github.io/metodi-num-algo/](https://palmucciarianna.github.io/metodi-num-algo/)**

---

### 2. In Locale sul proprio computer
Se preferisci aprirlo offline o lavorarci in locale:

1. Clona il repository:
   ```bash
   git clone https://github.com/palmucciarianna/metodi-num-algo.git
   cd metodi-num-algo
   ```

2. Puoi aprirlo in due modi:
   - **Opzione A (Server locale - Consigliata)**:
     ```bash
     python3 -m http.server 8000
     ```
     Poi apri nel browser l'indirizzo: `http://localhost:8000`
   - **Opzione B (Apertura diretta)**:
     Fai doppio clic su `index.html` (oppure su `metodi-num-algo.html`) per aprirlo direttamente con il tuo browser (Chrome, Firefox, Safari, Edge).

---

### 3. Come svolgere gli esercizi nell'app

1. **Seleziona un esercizio** dal menu laterale a sinistra.
2. **Completa il codice**: sostituisci i placeholder `# to do` con le istruzioni matematiche dell'algoritmo.
3. **Esegui e Valuta**: premi il pulsante **▶ Valuta Codice (Run)** in alto a destra (oppure usa la combinazione da tastiera).
4. **Verifica il risultato nel Terminale**:
   - ✅ Se l'algoritmo è corretto, comparirà il messaggio di conferma:
     ```text
     ✓ [Nome Algoritmo] corretto!
     ⭐⭐⭐ VALUTAZIONE COMPLETATA CON SUCCESSO! ⭐⭐⭐
     ```
   - ❌ Se il test fallisce o genera errori, la console indicherà l'asserzione o l'errore esatto per aiutarti a correggere il codice.
5. **Grafici**: se l'esercizio o il tuo codice genera grafici con `matplotlib.pyplot`, il pannello dedicato in basso si espanderà automaticamente mostrando la figura.

---

## 📦 Cosa include nello specifico

### Funzionalità dell'Ambiente

- **📖 Mini Guida & Formulario Teorico Integrato**: pulsante interattivo `📖 Teoria & Formule` nell'header che apre un pannello dedicato con il modello matematico, teoremi, formule, criteri d'arresto e guida ai passaggi `# to do` per tutti i 21 algoritmi (ispirato alle slide del corso UniBo).
- **Motore Python in WebAssembly (Pyodide)**: esecuzione 100% client-side di codice Python con librerie scientifiche reali (**NumPy**, **SciPy**, **Matplotlib**). Nessun dato o codice viene inviato a server esterni.
- **Editor CodeMirror**: sintassi evidenziata con tema Dracula, supporto a tabulazioni e indentazioni corrette per Python, e mantenimento dello stato separato per ogni esercizio.
- **Test di Valutazione Automatici**: ogni esercizio è accompagnato da test rigorosi su casi noti con tolleranze numeriche prestabilite.
- **Terminale Interattivo**: console ridimensionabile (con controlli `+`, `-`, reset `↺` e trascinamento del bordo) con output separato per print ed errori.
- **Pannello Grafici Matplotlib**: visualizzazione responsive dei grafici con pulsante di pulizia e ridimensionamento.

---

### Elenco Dettagliato degli Algoritmi ed Esercizi

#### 1. Zeri di Funzione
- **Metodo di Bisezione**: implementazione dell'algoritmo di bisezione su intervallo $[a, b]$, con stima a priori del numero massimo di iterazioni necessarie in base alla tolleranza.
- **Falsa Posizione (Regula Falsi)**: metodo di interpolazione lineare (corda) con criteri di arresto su scarto assoluto/relativo e residuo.
- **Metodo delle Corde**: iterazione con coefficiente angolare costante per ridurre il costo computazionale ad ogni passo.
- **Metodo di Newton (delle Tangenti)**: iterazione a convergenza quadratica mediante valutazione analitica di funzione e derivata prima.
- **Newton Modificato**: variante per radici con molteplicità nota $m > 1$ per preservare la convergenza di secondo ordine.
- **Metodo delle Secanti**: variante di Newton che approssima la derivata prima mediante rapporto incrementale su due iterati precedenti.
- **Stima dell'Ordine di Convergenza**: stima asintotica sperimentale dell'ordine di convergenza $p$ a partire dal vettore degli iterati $x_k$.

#### 2. Sistemi di Equazioni Non Lineari
- **Newton-Raphson per Sistemi**: risoluzione di sistemi non lineari $F(x) = 0$ con calcolo e inversione/risoluzione del sistema lineare con matrice Jacobiana $J(x_k)$ ad ogni iterazione.
- **Newton-Raphson a Jacobiana Costante (Corde)**: calcolo della matrice Jacobiana unicamente alla prima iterazione $J(x_0)$ per abbattere il costo computazionale per iterazione.
- **Newton-Shamanskii**: compromesso efficiente in cui la matrice Jacobiana viene ricalcolata solo ogni $k$ iterazioni (parametro `update`).

#### 3. Sistemi Lineari (Metodi Iterativi)
- **Metodo di Jacobi**: decomposizione della matrice $A = D - E - F$, costruzione della matrice di iterazione $T_J$, calcolo del raggio spettrale $\rho(T_J)$ e iterazione di punto fisso.
- **Metodo di Gauss-Seidel**: iterazione con matrice triangolare inferiore $M = D - E$, calcolo del raggio spettrale $\rho(T_{GS})$ e convergenza più rapida rispetto a Jacobi.
- **Gauss-Seidel SOR (Successive Over-Relaxation)**: accelerazione della convergenza tramite fattore di rilassamento $\omega \in (0, 2)$, con raggio spettrale $\rho(T_\omega)$.

#### 4. Ottimizzazione & Metodi del Gradiente
- **Steepest Descent (Metodo del Gradiente)**: ricerca del minimo per forme quadratiche con matrice simmetrica e definita positiva lungo la direzione dell'antigradiente (residuo), con calcolo analitico dello step-size ottimale $\alpha_k$.
- **Gradiente Coniugato (Conjugate Gradient)**: algoritmo iterativo per matrici simmetriche e definite positive basato su direzioni $A$-coniugate e coefficiente di aggiornamento $\beta_k / \gamma_k$.

#### 5. Minimi Quadrati (Least Squares)
- **Equazioni Normali**: risoluzione del problema ai minimi quadrati $\min \|Ax - b\|_2$ tramite il sistema $A^T A x = A^T b$, risolto stabilmente mediante fattorizzazione di Cholesky ($L L^T$).
- **Fattorizzazione QR**: approccio ortogonale stabile $A = Q R$, calcolo del vettore proiettato e risoluzione del sistema triangolare superiore.
- **Decomposizione SVD**: decomposizione ai valori singolari $A = U \Sigma V^T$, gestione del rango numerico con soglia di troncamento e calcolo della soluzione di norma minima e del residuo.

#### 6. Interpolazione Polinomiale
- **Polinomi Fondamentali di Lagrange**: calcolo dei coefficienti polinomiali della base di Lagrange $L_j(x)$ associata a un insieme di nodi.
- **Valutazione Interpolante**: costruzione della matrice di interpolazione di Lagrange e valutazione del polinomio interpolatore $P(x)$ su nodi densi di valutazione.

#### 7. Playground & Utility
- **Analisi Proprietà Matrici**: ambiente di calcolo libero con NumPy e SciPy per analizzare matrici di test (verifica simmetria, dominanza diagonale stretta, calcolo autovalori, raggio spettrale, numero di condizionamento).

---

## 🗂️ Struttura dei File

```text
metodi-num-algo/
├── index.html              # Entry point per GitHub Pages (Web Application completa)
├── metodi-num-algo.html    # File applicativo sorgente
└── README.md               # Questa documentazione
```

---

## 🧰 Stack Tecnologico

- **Runtime Web**: [Pyodide](https://pyodide.org/) (Python 3.12 WebAssembly)
- **Librerie Scientifiche**: NumPy, SciPy, Matplotlib
- **Editor**: CodeMirror 5 (tema Dracula)
- **Tecnologie Web**: HTML5, CSS3, JavaScript Vanilla (ES6+)

---

## 👥 Autori e Riconoscimenti

- **[Favour Osaretin Emuwahen](https://github.com/favess)** — Autore originale dell'applicativo e ideatore degli scheletri degli esercizi di metodi numerici.
- **[Arianna Palmucci](https://github.com/palmucciarianna)** — Pubblicazione su GitHub, deployment su GitHub Pages, ottimizzazione e miglioramenti dell'interfaccia (gestione e ridimensionamento pannelli console/grafici, layout responsive), documentazione e manutenzione.
