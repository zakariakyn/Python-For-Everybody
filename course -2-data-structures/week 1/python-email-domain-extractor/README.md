# Email Domain Extractor (Python)

Un script utilitaire léger en Python permettant d'extraire automatiquement le nom de domaine d'une adresse email contenue dans une chaîne de texte (en-tête de log, message, etc.).

Projet réalisé dans le cadre de l'apprentissage avec les ressources **Python for Everybody (PY4E)**.

---

## 📌 Fonctionnalités

- Extraction basée sur les méthodes natives de chaîne de caractères (`find()` et slicing).
- Aucun paquet externe requis (utilise uniquement la bibliothèque standard).
- Idéal pour analyser des lignes de logs ou des en-têtes d'emails au format standard Mbox.

---

## 🚀 Utilisation

### Code source

```python
# Exemple de chaîne d'entrée (en-tête de message)
message = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

# 1. Trouver la position du caractère '@'
at_pos = message.find("@")

# 2. Trouver l'espace suivant l'arobase
space_pos = message.find(" ", at_pos)

# 3. Extraire la sous-chaîne correspondante au domaine
domain = message[at_pos + 1 : space_pos]

print(domain)
```

### Exécution

Lancez le script avec Python 3 :

```bash
python main.py
```

### Résultat attendu

```text
uct.ac.za
```

---

## 📋 Messages de commit recommandés

- `feat: extract email host domain using string slicing and find()`
- `docs: add comprehensive README with usage and examples`

---

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE).