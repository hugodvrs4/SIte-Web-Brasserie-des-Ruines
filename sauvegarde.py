import os
import zipfile
from datetime import datetime

# 🔧 À personnaliser : ton dossier de projet (ex : "C:\\Users\\Nono\\Documents\\MonSite")
DOSSIER_SITE = r"C:\Users\devri\OneDrive - Haute Ecole en Hainaut\Q2\Développement Web\Projet"

# 🔧 Dossier où seront stockées les sauvegardes
DOSSIER_SAUVEGARDE = r"C:\Users\devri\OneDrive - Haute Ecole en Hainaut\Q2\Développement Web\Projet\sauvegardes"

if not os.path.exists(DOSSIER_SITE):
    print(f"❌ Le dossier source n'existe pas : {DOSSIER_SITE}")
    exit()

# Crée le dossier de sauvegarde si besoin
os.makedirs(DOSSIER_SAUVEGARDE, exist_ok=True)

# Préparer la sauvegarde
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nom_archive = f"sauvegarde_{timestamp}.zip"
chemin_archive = os.path.join(DOSSIER_SAUVEGARDE, nom_archive)

print("📦 Création de la sauvegarde...")

# Création du .zip
with zipfile.ZipFile(chemin_archive, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for dossier_racine, _, fichiers in os.walk(DOSSIER_SITE):
        for fichier in fichiers:
            chemin_complet = os.path.join(dossier_racine, fichier)
            chemin_relatif = os.path.relpath(chemin_complet, DOSSIER_SITE)
            zipf.write(chemin_complet, chemin_relatif)

print(f"✅ Sauvegarde terminée : {chemin_archive}")