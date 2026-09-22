"""
Diagnostic de l'environnement Python du cours.

Usage :
    python check_env.py

Le script ne modifie rien. Il verifie, dans l'ordre, ce dont le cours a besoin
et affiche pour chaque echec la cause probable et l'action a tenter.

A la fin, il affiche ENVIRONNEMENT OK, ou la liste de ce qui manque.

Script généré par IA.
"""

import importlib
import os
import platform
import shutil
import subprocess
import sys
import tempfile

OK = "[ OK ]"
KO = "[ !! ]"
WARN = "[ ?? ]"

problems = []
warnings_ = []


def title(text):
    print()
    print(text)
    print("-" * len(text))


def fail(msg, fix):
    print(f"{KO} {msg}")
    print(f"       -> {fix}")
    problems.append(msg)


def warn(msg, fix):
    print(f"{WARN} {msg}")
    print(f"       -> {fix}")
    warnings_.append(msg)


def good(msg):
    print(f"{OK} {msg}")


# ----------------------------------------------------------------------
title("1. Interpreteur Python")

v = sys.version_info
print(f"       version   : {sys.version.split()[0]}")
print(f"       executable: {sys.executable}")
print(f"       systeme   : {platform.system()} {platform.release()} ({platform.machine()})")

if v < (3, 9):
    fail(
        f"Python {v.major}.{v.minor} est trop ancien pour ce cours.",
        "Installez Python 3.11 ou 3.12 depuis https://www.python.org/downloads/",
    )
elif v >= (3, 14):
    warn(
        f"Python {v.major}.{v.minor} est tres recent ; certaines bibliotheques "
        "n'ont pas encore de version compatible.",
        "Si une installation echoue, installez Python 3.12 a cote.",
    )
else:
    good(f"Python {v.major}.{v.minor} convient.")

# ----------------------------------------------------------------------
title("2. Environnement virtuel")

in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
if in_venv:
    good(f"Vous travaillez dans un environnement virtuel : {sys.prefix}")
else:
    warn(
        "Vous utilisez le Python systeme, pas un environnement virtuel.",
        "Creez-en un :  python -m venv .venv   puis activez-le "
        "(.venv\\Scripts\\activate sous Windows, source .venv/bin/activate sinon)",
    )

# ----------------------------------------------------------------------
title("3. Gestionnaire de paquets (pip)")

try:
    import pip  # noqa: F401

    out = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        capture_output=True, text=True, timeout=60,
    )
    if out.returncode == 0:
        good(out.stdout.strip())
    else:
        fail("pip repond mais renvoie une erreur.", "Essayez : python -m ensurepip --upgrade")
except Exception as e:
    fail(f"pip est introuvable ({type(e).__name__}).", "Essayez : python -m ensurepip --upgrade")

# ----------------------------------------------------------------------
title("4. Acces reseau aux depots de paquets")

proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
if proxy:
    print(f"       un proxy est configure : {proxy}")

try:
    import urllib.request

    urllib.request.urlopen("https://pypi.org/simple/", timeout=20).read(64)
    good("pypi.org est joignable, l'installation de paquets devrait fonctionner.")
except Exception as e:
    fail(
        f"pypi.org est injoignable ({type(e).__name__}).",
        "Reseau d'entreprise avec proxy ou pare-feu. Essayez le partage de connexion "
        "de votre telephone, ou signalez-le en debut de seance : un plan B existe.",
    )

# ----------------------------------------------------------------------
title("5. Bibliotheques du cours")

REQUIRED = [
    ("numpy", "calcul sur tableaux, seances 1 a 4"),
    ("pandas", "manipulation de donnees, seance 2"),
    ("matplotlib", "graphiques, seance 2"),
    ("sklearn", "machine learning, seance 3"),
]
OPTIONAL = [
    ("seaborn", "graphiques statistiques, seance 2"),
    ("torch", "deep learning, seance 4"),
    ("jupyterlab", "environnement de notebooks (VS Code convient aussi)"),
]

for name, usage in REQUIRED:
    try:
        m = importlib.import_module(name)
        good(f"{name:<12} {getattr(m, '__version__', '?'):<10} ({usage})")
    except ImportError:
        fail(
            f"{name} est absent ({usage}).",
            "Installez tout d'un coup :  pip install -r requirements.txt",
        )

for name, usage in OPTIONAL:
    try:
        m = importlib.import_module(name)
        good(f"{name:<12} {getattr(m, '__version__', '?'):<10} ({usage})")
    except ImportError:
        warn(f"{name} est absent ({usage}).", "Non bloquant aujourd'hui. pip install " + name)

# ----------------------------------------------------------------------
title("6. Git")

git = shutil.which("git")
if git:
    try:
        out = subprocess.run([git, "--version"], capture_output=True, text=True, timeout=30)
        good(out.stdout.strip())
    except Exception:
        good(f"git trouve : {git}")
else:
    warn(
        "git est introuvable.",
        "Necessaire seulement a partir de la seance 3. "
        "https://git-scm.com/downloads",
    )

# ----------------------------------------------------------------------
title("7. Ecriture de fichiers")

try:
    with tempfile.NamedTemporaryFile(dir=".", suffix=".tmp", delete=True) as f:
        f.write(b"test")
    good("Vous pouvez ecrire des fichiers dans ce dossier.")
except Exception as e:
    fail(
        f"Impossible d'ecrire ici ({type(e).__name__}).",
        "Antivirus ou dossier protege (OneDrive, Documents d'entreprise). "
        "Deplacez le dossier du cours ailleurs, par exemple a la racine de votre disque.",
    )

# ----------------------------------------------------------------------
title("8. Donnees du cours")

import pathlib

csv = pathlib.Path(__file__).parent / "data" / "ai4i2020.csv"
if csv.exists():
    good(f"data/ai4i2020.csv present ({csv.stat().st_size // 1024} Ko).")
else:
    warn(
        "data/ai4i2020.csv est absent.",
        "Generez-le :  python data/make_dataset.py",
    )

# ----------------------------------------------------------------------
print()
print("=" * 62)
if problems:
    print(f"{len(problems)} PROBLEME(S) BLOQUANT(S) :")
    for p in problems:
        print(f"  - {p}")
    print()
    print("Ne passez pas plus de 30 minutes dessus. Signalez-le en debut de")
    print("seance : un plan B est prevu et vous ne perdrez pas le cours.")
elif warnings_:
    print("ENVIRONNEMENT OK (avec quelques avertissements non bloquants)")
    for w in warnings_:
        print(f"  - {w}")
else:
    print("ENVIRONNEMENT OK")
print("=" * 62)

sys.exit(1 if problems else 0)
