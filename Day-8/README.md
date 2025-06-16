# 🧪 Day 8: Caesar Cipher Project

This project is part of the **100 Days of Python** challenge. It implements a **Caesar Cipher** – one of the simplest and oldest methods of encryption. The project includes encoding, decoding, input validation, symbol handling, and a restart loop.

---

## ✅ Features

- 🔐 **Encrypt & Decrypt** messages using Caesar Cipher logic  
- 🔄 **Restart loop** for continuous use  
- 🧾 **Handles non-alphabet characters** like numbers, spaces, and symbols  
- 🧠 **Wraps around the alphabet** using modulo to avoid index errors  
- 🎨 **Includes ASCII art logo** for a fun touch  

---

## 💡 How It Works

- The Caesar Cipher shifts each letter in the message by a given number of positions in the alphabet.
- When decoding, the shift is reversed.
- Non-alphabet characters are **not modified**.
- Shift values greater than 26 are wrapped using the **modulo operator (`%`)**.

---