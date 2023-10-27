# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

def extraire_extension(nom_fichier):
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) > 1:
        return nom_fichier_split[-1]
    return None

def obtenir_definition_extension(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
    return None

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

"""definition_extensions_dict = {"doc": "Document Word",
                        "exe": "Executable",
                        "txt": "Document Texte",
                        "jpeg": "Image JPEG"}"""
# Version 1
for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = obtenir_definition_extension(ext, definition_extensions)
        # definition = definition_extensions_dict.get(ext.lower())
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier + " (" + definition + ")")

# Version 2
for fic in fichiers:
    if "." in fic:
        extension = fic.split(".")[-1]
        if extension.lower() not in [ext.lower() for ext, nom in definition_extensions]:
            print(f"{fic} (Extension inconnue)")
        for ext, nom in definition_extensions:
            if ext.lower() == extension.lower():
                print(f"{fic} ({nom})")
    else:
        print(f"{fic} (Aucune extension)")

