# Symmetrische Encryptie/Decryptie App

## Overzicht
Dit is een eenvoudige Python command-line app voor symmetrische encryptie en decryptie van tekst, met behulp van de `cryptography` library. De app ondersteunt de volgende functies:
- Versleutelen van tekst
- Ontsleutelen van tekst
- Genereren van een nieuwe sleutel

## Uitleg van de app:

- Versleutelen: De gebruiker voert de tekst in, waarna de applicatie deze versleutelt met een symmetrische sleutel en het resultaat toont.
- Ontsleutelen: De gebruiker voert de versleutelde tekst in, en de applicatie decrypt deze weer naar de oorspronkelijke tekst.
- Sleutelbeheer: De gebruiker kan een nieuwe symmetrische sleutel genereren en opslaan in een bestand genaamd secret.key.


## Vereisten
- Python 3
- cryptography

## Installatie
1. Clone de repository:
   ```bash
   git clone https://github.com/omer-1080314/security-week5-encryptie
   cd security-week5-encryptie
   ```

## Gebruik

Run de app:

```bash
python encryptie_app.py
```

Kies uit de opties in de terminal om tekst te versleutelen, ontsleutelen of een nieuwe sleutel te genereren.

## Encryptiemethode

Deze app gebruikt symmetrische encryptie met behulp van de cryptography library. Het Fernet-algoritme wordt gebruikt, dat zowel encryptie als integriteitscontrole biedt.

### Opmerking:

**De sleutel wordt opgeslagen in een bestand secret.key. Bewaar dit veilig, want deze sleutel is nodig om de gegevens te ontsleutelen.**