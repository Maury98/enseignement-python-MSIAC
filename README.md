# Développement Python pour l'apprentissage

**Mastère spécialisé IA de confiance** — 12h — 1 ECTS
Enseignant : Arnaud Maury

---

## Installation

### 1. Python

Il vous faut **Python 3.11 ou 3.12**. Vérifiez ce que vous avez :

```bash
python --version      # ou python3 --version sous macOS et Linux
```

Si la commande échoue ou affiche une version inférieure à 3.9, installez Python depuis [python.org/downloads](https://www.python.org/downloads/).

> **Windows :** à l'installation, cochez **« Add Python to PATH »** sur le premier écran. C'est l'erreur la plus fréquente, et elle oblige à tout recommencer.

### 2. Visual Studio Code

Téléchargez [code.visualstudio.com](https://code.visualstudio.com/), puis installez l'extension **Python** de Microsoft (icône Extensions dans la barre latérale, chercher « Python »).

### 3. Git

Soit dans le terminal si vous êtes sur Linux ou Mac, soit dans VSCode si vous êtes sur Windows.

### 4. Ce dépôt

```bash
git clone <URL-du-dépôt>
cd cours-python-ml
```

### 5. L'environnement virtuel

Un environnement virtuel isole les bibliothèques de ce cours du reste de votre machine. Ce n'est pas une coquetterie de développeur : c'est ce qui rend votre travail reproductible, donc auditable.

```bash
python -m venv .venv
```

Puis activez-le. **À refaire à chaque fois que vous ouvrez un terminal.**

| Système | Commande |
| --- | --- |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| macOS, Linux | `source .venv/bin/activate` |

Vous saurez que c'est actif quand votre invite de commande commence par `(.venv)`.

### 6. Les bibliothèques

```bash
pip install -r requirements.txt
```

Comptez 2 à 5 minutes. PyTorch est volumineux (environ 200 Mo) ; si l'installation échoue ou traîne, vous pouvez l'installer juste avant la séance 4.

### 7. Vérification

```bash
python check_env.py
```

Le script teste tout ce dont le cours a besoin et affiche, pour chaque échec, la cause probable et l'action à tenter. Il se termine par `ENVIRONNEMENT OK` ou par la liste de ce qui manque.

---

## Une erreur récurente

Vous installez pandas, et Python répond `ModuleNotFoundError: No module named 'pandas'`.

Souvent, cela veut dire que Visual Studio Code n'utilise pas l'interpréteur de votre environnement virtuel.

**La correction :** `Ctrl+Shift+P` (`Cmd+Shift+P` sur Mac), tapez `Python: Select Interpreter`, et choisissez celui dont le chemin contient `.venv`.

---

## Ressources

| Sujet | Lien |
| --- | --- |
| Guide utilisateur scikit-learn | [scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html) |
| Tutoriels PyTorch | [pytorch.org/tutorials](https://pytorch.org/tutorials/) |
| Documentation numpy | [numpy.org/doc/stable](https://numpy.org/doc/stable/) |
| Documentation pandas | [pandas.pydata.org/docs](https://pandas.pydata.org/docs/) |
| Documentation du précédent enseignant | [Notion](https://app.notion.com/p/D-veloppement-Python-pour-l-apprentissage-87795d0e218f8238a657811be6a6cc96) |

Le guide utilisateur de scikit-learn est le meilleur document pédagogique du domaine. Prenez l'habitude d'y aller avant de chercher ailleurs.
