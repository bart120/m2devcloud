# TP – Pipeline asynchrone avec Azure Blob Trigger, Service Bus et tagging automatique

## Objectif

Mettre en place un pipeline de traitement asynchrone en deux étapes :

1. une première Azure Function déclenchée par l’arrivée d’un fichier dans Blob Storage ;
2. une deuxième Azure Function déclenchée par un message Azure Service Bus.

La deuxième Function réalise le tagging automatique du document et met à jour Cosmos DB.

---

## Architecture cible

```
Blob Storage
   |
   | fichier déposé dans input/
   v
Azure Function 1
Blob Trigger
   |
   | message JSON
   v
Azure Service Bus Queue
   |
   v
Azure Function 2
Service Bus Trigger
   |
   v
Cosmos DB
```

---

## Function 1 – Blob Trigger

La première Function est déclenchée lorsqu’un fichier est ajouté dans le dossier :

```
input/
```

Son rôle est uniquement de publier un message dans Azure Service Bus.

Elle ne doit pas faire le traitement métier.

---

## Message envoyé dans Service Bus

```json
{
  "documentId": "123",
  "fileName": "cv_amine_azure.pdf",
  "blobName": "input/123_cv_amine_azure.pdf",
  "size": 248392,
  "uploadedAt": "2026-04-27T10:45:00Z"
}
```

---

## 📁 Format attendu du blob

```
input/{documentId}_{fileName}
```

Exemple :

```
input/123_cv_amine_azure.pdf
```

---

## ⚙️ Function 2 – Service Bus Trigger

La deuxième Function est déclenchée par le message reçu dans la queue Service Bus.

Elle doit :

- lire le message ;
- vérifier si le fichier est vide ;
- retrouver le document dans Cosmos DB ;
- générer les tags ;
- mettre à jour Cosmos DB.

---

## Règles

### Fichier vide

```
status = ERROR
```

### Document introuvable

```
status = ERROR
```

### Succès

```json
{
  "id": "123",
  "fileName": "cv_amine_azure.pdf",
  "status": "PROCESSED",
  "tags": ["azure", "cloud", "cv", "document", "pdf", "rh"],
  "processedAt": "2026-04-27T10:45:00Z"
}
```

---

## Tagging

### Extensions

- .pdf → pdf, document
- .docx → word, document
- .png → image

### Mots-clés

- cv → cv, rh
- facture → facture, comptabilite
- contrat → contrat, administratif
- azure → azure, cloud
- docker → docker, devops

---

## Tests

- input/123_cv_amine_azure.pdf → PROCESSED
- input/127_vide.pdf → ERROR
- input/999_test.pdf → ERROR
