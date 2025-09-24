## ToSecret

This program is written in Python and uses the Fernet cryptography library to encrypt and decrypt files. The files are secured with a key derived from a password and a salt, so only users with the correct password can unlock the encrypted files.

### A few things are needed

- Terminal, Command Prompt or PowerShell to run the program

- Python version 3.8 or higher has been installed

### Documentation

ToSecret program has three menus, each with its own function, such as:

- Init - "It will create a "files" folder to store the files to be encrypted or decrypted, and create an "output" folder to store the results of the process.."

- Encryption - "Will run the encryption process when there are files in the "encryption" folder."

- Decryption - "Will run the decryption process when there are files in the "decryption" folder."

- Exit - "Will exit the program."

If you want to exit the process of entering the encryption and decryption password, just press the shortcut "CTRL + C" or "CTRL + D".

### How to run the program

#### 1. Clone repository

```bash
git clone https://github.com/angslhn/ToSecret.git
```

#### 2. Move to project

```bash
cd ToSecret
```

#### 3. Install the required packages

```bash
pip install -r requirements.txt
```

#### 4. Run program

```bash
python main.py
```

### Authors

- [@angslhn](https://www.github.com/angslhn)
