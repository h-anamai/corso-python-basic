# 🐍 Corso Python Basic

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![GitHub Release](https://img.shields.io/github/v/release/h-anamai/corso-python-basic?color=green)](https://github.com/h-anamai/corso-python-basic/releases)


Benvenuto al corso base di Python! Questo repository contiene una serie di notebook progettati per guidarti nei primi passi con il linguaggio Python, con esempi pratici ed esercitazioni.

Per domande e contenuti extra, unisciti ai nostri canali:

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/+gTwagH1r9kVjMjY0)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/gkjMTFSVc)

Visita il sito ufficiale del corso dove potrai anche ottenere il badge di completamento del corso!

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-online-brightgreen?style=for-the-badge&logo=github)](https://h-anamai.github.io/corso-python-basic/)



## 📚 Sommario

| Modulo                                                   | Descrizione                                          |
|----------------------------------------------------------|------------------------------------------------------|
| [00_sommario_corso.ipynb](00_sommario_corso.ipynb)       | Introduzione e panoramica del corso    <br/>         |
| [01_primi_passi.ipynb](01_sintassi_base.ipynb)           | Primi passi con il linguaggio                        |
| [02_sintassi_base.ipynb](02_sintassi_base.ipynb)         | Sintassi base: commenti, indentazione, variabili, tipi di dato, controllo del flusso, cicli  |          
| [03_strutture_dati.ipynb](03_strutture_dati.ipynb)       | Utilizzare le strutture dati più comuni              |
| [04_gestione_errori.ipynb](04_gestione_errori.ipynb)     | Come gestire gli errori                              |
| [05_funzioni_moduli.ipynb](05_funzioni_moduli.ipynb)     | Usare funzioni e moduli                              |
| [06_fileio.ipynb](06_fileio.ipynb)                       | Leggere e scrivere da file                           |
| [07_libreria_standard.ipynb](07_libreria_standard.ipynb) | Usare i moduli della libreria standard               |
| [08_librerie.ipynb](08_librerie_standard.ipynb)          | Usare moduli addizionali ed ambienti virtuali        |
| [09_oop.ipynb](09_oop.ipynb)                             | Programmazione Orientata agli Oggetti, concetti base |
| [10_testunit.ipynb](10_testunit.ipynb)                   | Progettare test unitari per i programmi              |
| [11_progetto.ipynb](11_progetto.ipynb)                   | Realizzazione di una semplice applicazione           |
| [appendix.ipynb](appendix.ipynb)                         | La storia di Python                                  |

## 🎯 Obiettivi del corso

- Imparare la sintassi base di Python
- Eseguire codice in un ambiente interattivo (Jupyter)
- Comprendere i concetti fondamentali della programmazione usando Python
- Usare la Programmazione Orientata agli Oggetti
- Progettare test unitari per i programmi
- Sviluppare script e semplici programmi

---

## ▶️ Come usare i notebook

Puoi aprire e utilizzare i notebook in diversi modi, a seconda delle tue preferenze e del tuo ambiente di lavoro. Se vuoi lavorare in locale occorre prima installare `pip`.

### ⚙️ Installare `pip`

`pip` è il gestore di pacchetti di Python e serve per installare librerie aggiuntive (come `notebook` o `jupyterlab`).  
In molte distribuzioni recenti di Python è già incluso, ma in caso contrario puoi installarlo così, aprendo un terminale:

```bash
pip --version
```

Se il comando restituisce un numero di versione, significa che `pip` è già installato.  
In alternativa, puoi provare con:

```bash
python -m pip --version
```

---

#### 🔹 Installazione su Linux / macOS

Se `pip` non è presente, puoi installarlo usando il comando:

```bash
python3 -m ensurepip --upgrade
```

oppure installa tramite **apt** (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3-pip
```

Su macOS con **Homebrew**:

```bash
brew install python3
```

(Homebrew installa Python e include `pip`).

---

#### 🔹 Installazione su Windows

1. Scarica l’installer ufficiale di Python da [python.org](https://www.python.org/downloads/).
2. Durante l’installazione, assicurati di selezionare l’opzione **“Add Python to PATH”**.
3. `pip` verrà installato automaticamente.
4. Se serve, puoi aggiornarlo con:

```bash
python -m pip install --upgrade pip
```

---

#### 🔹 Anaconda / Miniconda

Se utilizzi **Anaconda** o **Miniconda**, `pip` è già incluso.  
Puoi verificarlo con:

```bash
conda list pip
```

In alternativa, puoi installarlo/aggiornarlo con:

```bash
conda install pip
```

### ✅ Con Jupyter Notebook (installazione locale)

Se vuoi lavorare in locale, installa Jupyter e avvia il server:

```bash
pip install notebook
jupyter notebook
```

Dopo aver eseguito il comando, si aprirà una finestra nel browser da cui potrai navigare tra le cartelle e aprire i file `.ipynb`.

---

### ✅ Con JupyterLab (interfaccia avanzata)

JupyterLab offre un’interfaccia più moderna e completa rispetto a Jupyter Notebook:

```bash
pip install jupyterlab
jupyter lab
```

---

### ✅ Con VS Code

1. Installa [Visual Studio Code](https://code.visualstudio.com/).
2. Aggiungi l’estensione **Python** e l’estensione **Jupyter**.
3. Apri il progetto e clicca direttamente sui file `.ipynb` per eseguirli all’interno di VS Code.

---

### ✅ Con Google Colab (nessuna installazione richiesta)

Se non vuoi installare nulla, puoi aprire i notebook direttamente su [Google Colab](https://colab.research.google.com/):

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/h-anamai/corso-python-basic)

1. Vai su Colab e seleziona **File → Carica notebook**.
2. Oppure usa il badge qui sopra.
3. Avrai a disposizione un ambiente gratuito in cloud, già pronto per l’uso.

---

### ✅ Con Binder (esecuzione online dal repository)

Puoi anche eseguire i notebook online senza installazioni tramite [Binder](https://mybinder.org/):

[![Esegui su Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/h-anamai/corso-python-basic/HEAD)

Basta cliccare sul badge e attendere l’avvio dell’ambiente interattivo.

---

&copy; 2025 Hanamai. All rights reserved. | Built with precision for real-time data streaming excellence.
