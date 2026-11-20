# 🧮 Palestra Metodi Numerici & Intelligenza Artificiale in Python

[![Live Demo](https://img.shields.io/badge/Demo-GitHub%20Pages-brightgreen?logo=github)](https://palmucciarianna.github.io/metodi-num-algo/)
[![Python - Pyodide](https://img.shields.io/badge/Python-Pyodide%20v0.25.0-3776AB?logo=python&logoColor=white)](https://pyodide.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Supported-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Supported-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Supported-11557c)](https://matplotlib.org/)

Piattaforma web interattiva e archivio completo per lo studio, l'implementazione e la preparazione dell'esame di **Metodi Numerici per l'Intelligenza Artificiale** (Università di Bologna - Docenti: Prof.ssa Damiana Lazzaro [Modulo I] e Prof. Lorenzo Pellegrini [Modulo II]).

> 📚 **Materiali Ufficiali & Repository del Corso**:  
> Tutte le definizioni, notazioni, teoremi e criteri d'arresto sono conformi alle slide e dispense d'esame UniBo. I materiali completi sono consultabili anche su:  
> 👉 **[github.com/palmucciarianna/metodinumericiAI](https://github.com/palmucciarianna/metodinumericiAI)**

---

## 🚀 Come farlo funzionare

Non serve installare Python, né configurare ambienti virtuali o scaricare librerie sul proprio computer.

### 1. Online (Consigliato - Immediato)
L'applicazione è attiva su GitHub Pages ed è fruibile direttamente dal browser:  
👉 **[https://palmucciarianna.github.io/metodi-num-algo/](https://palmucciarianna.github.io/metodi-num-algo/)**

---

### 2. In Locale sul proprio computer
Se preferisci aprirlo offline:

1. Clona il repository:
   ```bash
   git clone https://github.com/palmucciarianna/metodi-num-algo.git
   cd metodi-num-algo
   ```

2. Avvia un server locale rapido:
   ```bash
   python3 -m http.server 8000
   ```
   Poi apri nel browser: `http://localhost:8000` (oppure fai doppio clic su `index.html`).

---

## ✨ Funzionalità della Piattaforma

1. **🌳 Albero Decisionale per $Ax=b$ (Mappa Concettuale Interattiva)**:
   - **Diagnostica rapida**: inserisci la forma della matrice ($m > n$ sovradeterminata o $m = n$ quadrata), la sparsità (densa vs sparsa) e le proprietà algebriche (SPD, dominanza diagonale, condizionamento) per ottenere all'istante l'algoritmo consigliato, la complessità in flops, la funzione SciPy corrispondente e le avvertenze di stabilità.
   - **Mappa completa a schede**: schema riassuntivo per Equazioni Normali (Cholesky), Fattorizzazione QR, Decomposizione SVD, Cholesky $LL^T$, Eliminazione di Gauss $PA=LU$, Jacobi, Gauss-Seidel, SOR e Gradiente Coniugato (CG).

2. **🧠 Modulo II: Reti Neurali & 22 Domande d'Esame Svolte**:
   - Schede di ripasso rapido ad alto rendimento con accordion e barra di ricerca istantanea.
   - Copre tutte le **22 domande aperte ufficiali** del Modulo II (Prof. Pellegrini):
     - Fondamenti e storia dell'IA (Turing, inverni dell'IA, 2011 DL revolution).
     - Neurone biologico vs artificiale, funzioni di attivazione (Sigmoide, Tanh, ReLU, Leaky ReLU).
     - Architettura MLP, CNN (convoluzione 2D, kernel, feature maps, pooling).
     - Loss functions (MSE, MAE, Binary Cross-Entropy, Categorical Cross-Entropy).
     - Addestramento, non-convessità della loss, backpropagation (con derivazione completa del caso MLP 1-1-1-1).
     - Ottimizzatori: Batch GD vs SGD vs Mini-Batch GD, Momentum, Learning Rate Scheduling (step, exponential, time-based), e algoritmi adattivi (Adagrad, RMSProp, Adam).

3. **🧪 Laboratori Didattici con 1-Click su Google Colab**:
   - Accesso istantaneo con GPU gratuita ai Jupyter Notebook ufficiali:
     - 🚀 `1_Classificazione_di_immagini_tramite_MLP.ipynb` (Multi-Layer Perceptron su dataset immagini).
     - 🚀 `2_Classificazione_di_immagini_con_Convolutional_Neural_Network.ipynb` (CNN con convoluzioni, pooling, dropout e metriche).
     - 🚀 `Simulazione_III.ipynb` (Simulazione prova d'esame al calcolatore con zeri, sistemi lineari, minimi quadrati e interpolazione).

4. **💾 Salvataggio Automatico (`localStorage`) & Tracciamento Progressi**:
   - Il codice digitato per ciascun esercizio viene salvato in tempo reale nel browser. Se chiudi la pagina o ricarichi, il tuo lavoro non viene perso.
   - Spunta verde `✓` nella sidebar quando un test viene superato con successo.
   - Barra di avanzamento percentuale globale (`0 / 21 completati`).
   - Tasti dedicati per ripristinare il template iniziale (`↺ Reset`) o azzerare tutti i progressi locali.

5. **💡 Suggerimenti (Hint) & Soluzioni Ufficiali**:
   - Pulsante `💡 Hint`: fornisce l'indizio matematico e la funzione NumPy/SciPy da usare.
   - Pulsante `👁️ Soluzione`: mostra il codice ufficiale verificato con tasto rapido per incollarlo nell'editor.

6. **📈 Grafici di Convergenza Automatici (`semilogy`)**:
   - Tracciamento della curva di convergenza dell'errore asintotico su scala semilogaritmica (`plt.semilogy`) per metodi di ricerca zeri, sistemi lineari iterativi (Jacobi, Gauss-Seidel, SOR) e metodi di discesa del gradiente.
   - Confronto grafico del fenomeno di Runge su nodi equispaziati per l'interpolazione polinomiale.

7. **⌨️ Scorciatoie da Tastiera & Ricerca Veloce**:
   - <kbd>Cmd</kbd> + <kbd>Invio</kbd> (Mac) o <kbd>Ctrl</kbd> + <kbd>Invio</kbd> (Windows/Linux) per eseguire e testare all'istante il codice.
   - <kbd>Esc</kbd> per chiudere qualsiasi modal aperto.
   - Barra di ricerca dinamica nella sidebar per filtrare gli esercizi per nome o parola chiave.

8. **📥 Esportazione Script (`.py`)**:
   - Scarica il codice dell'esercizio corrente formattato con header e test di verifica.
   - Scarica la raccolta unificata con tutti i 21 algoritmi pronti per l'esame.

9. **🌙 Tema Dark & ☀️ Tema Chiaro**:
   - Modalità scura completa basata sulla palette Dracula / Slate, alternabile con un clic e memorizzata nel browser.

---

## 📁 Struttura del Repository

```text
metodi-num-algo/
├── index.html              # Entry point per GitHub Pages (Web Application completa)
├── metodi-num-algo.html    # Applicativo web sorgente
├── README.md               # Documentazione completa del progetto
│
├── laboratori/             # Notebooks Jupyter dei laboratori didattici
│   ├── 1_Classificazione_di_immagini_tramite_MLP.ipynb
│   └── 2_Classificazione_di_immagini_con_Convolutional_Neural_Network.ipynb
│
├── simulazioni_esame/      # Prove d'esame pratiche simulate
│   └── Simulazione_III.ipynb
│
├── scripts_py/             # Script Python e scheletri con tutti gli algoritmi
│   ├── SolveTriangular.py  # Risoluzione forward/backward (Lsolve, Usolve)
│   ├── Pattern_25_26.py    # Pattern e condizioni d'arresto esame 2025/2026
│   ├── Scheletri_24_25.py  # Scheletri di implementazione
│   ├── Utilities_24_25.py  # Funzioni simboliche sympy per gradiente e Jacobiano
│   └── metodi_diego.py     # Implementazioni di riferimento
│
└── dispense_pdf/           # Slide e dispense ufficiali del corso
    ├── 1_Introduzione_AI.pdf
    ├── 2_MLP.pdf
    ├── 3_CNN.pdf
    ├── DomandeIA_25_26.pdf
    ├── Sistemi_Lineari_Metodi_Numerici_Diretti.pdf
    ├── Sistemi_Lineari_Metodi_Numerici_Iterativi.pdf
    ├── SoluzioneSistemiSovradeterminati.pdf
    ├── EquazioniNonLineari.pdf
    ├── InterpolazionePolinomiale.pdf
    ├── Condizionamento_e_stabilita.pdf
    ├── Norme_vettoriali_e_matriciali.pdf
    └── MappaConcettuale_SistemiLineari.pdf
```

---

## 🧰 Stack Tecnologico

- **Runtime Web**: [Pyodide](https://pyodide.org/) (Python 3.12 WebAssembly client-side)
- **Librerie Scientifiche**: NumPy, SciPy, Matplotlib
- **Formule Matematiche**: [KaTeX](https://katex.org/)
- **Editor di Codice**: CodeMirror 5 (tema Dracula con bracket matching)
- **Tecnologie Web**: HTML5, CSS3 Variables, JavaScript Vanilla (ES6+)

---

## 👥 Autori e Riconoscimenti

- **[Favour Osaretin Emuwahen](https://github.com/favess)** — Autore originale dell'applicativo e ideatore degli scheletri degli esercizi di metodi numerici.
- **[Arianna Palmucci](https://github.com/palmucciarianna)** — Pubblicazione su GitHub, deployment su GitHub Pages, espansione della piattaforma (albero decisionale, schede d'esame del Modulo II, integrazione Google Colab, auto-save in LocalStorage, grafici di convergenza semilogaritmici, sistema di suggerimenti e soluzioni, tema dark/light, ricerca e scorciatoie), organizzazione dei materiali didattici e documentazione.
