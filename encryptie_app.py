import subprocess
import sys


# Functie om te controleren of cryptography is geïnstalleerd
def check_and_install_cryptography():
    try:
        import cryptography
    except ImportError:
        print("De 'cryptography' module is niet geïnstalleerd. Installatie wordt gestart...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
        print("'cryptography' is succesvol geïnstalleerd.")


# Functie om een nieuwe sleutel te genereren en op te slaan
def generate_key():
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# Functie om de sleutel uit bestand te laden
def load_key():
    return open("secret.key", "rb").read()


# Functie om tekst te versleutelen
def encrypt_message(message):
    from cryptography.fernet import Fernet
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


# Functie om tekst te ontsleutelen
def decrypt_message(encrypted_message):
    from cryptography.fernet import Fernet
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


def main():
    check_and_install_cryptography()  # Controleer en installeer cryptography indien nodig

    print("Welkom bij de Encryptie/Decryptie App")

    while True:
        print("\nMaak een keuze:")
        print("1. Versleutel een bericht")
        print("2. Ontsleutel een bericht")
        print("3. Genereer een nieuwe sleutel")
        print("4. Exit")

        choice = input("\nVoer je keuze in (1/2/3/4): ")

        if choice == "1":
            message = input("\nVoer de tekst in die je wilt versleutelen: ")
            encrypted_message = encrypt_message(message)
            print(f"Versleutelde tekst: {encrypted_message.decode()}")

        elif choice == "2":
            encrypted_message = input("\nVoer de versleutelde tekst in die je wilt ontsleutelen: ").encode()
            try:
                decrypted_message = decrypt_message(encrypted_message)
                print(f"Ontsleutelde tekst: {decrypted_message}")
            except Exception as e:
                print(f"Fout bij het ontsleutelen: {str(e)}")

        elif choice == "3":
            generate_key()
            print("Nieuwe sleutel gegenereerd en opgeslagen als 'secret.key'")

        elif choice == "4":
            print("Programma beëindigd.")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    main()
