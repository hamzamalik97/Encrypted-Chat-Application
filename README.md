# Encrypted Chat Application

## Description

A secure multi-client chat application developed in Python that encrypts messages using AES encryption before transmission. This project demonstrates knowledge of client-server architecture, socket programming, symmetric encryption, and concurrency.

---

## Features

* Multi-client chat support
* AES encrypted messages
* Username-based messaging
* Join/leave notifications
* Message logging (chat.log)
* TCP socket communication

---

## Technologies Used

* Python 3.14
* PyCryptodome (AES Encryption)
* TCP Socket Programming
* Threading for concurrency
* Base64 for message encoding

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/Encrypted-Chat-Application.git
```

2. Navigate to the project folder:

```bash
cd Encrypted-Chat-Application
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Server

1. Run the server:

```bash
python server.py
```

2. The server will start listening on `127.0.0.1:12345`.

### Client

1. Run the client:

```bash
python client.py
```

2. Enter a username.
3. Start sending and receiving encrypted messages.

*Multiple clients can connect to the same server simultaneously.*

---

## Folder Structure

```
Encrypted-Chat-Application/
├── server.py
├── client.py
├── crypto_utils.py
├── requirements.txt
├── chat.log
├── Internship_Report.docx
```

---

## License

This project is licensed under the MIT License.

---

## Contact

Muhammad Hamza Siddique Shaker
Email: yeshhamzamalik@gmail.com
Organization: Syntecxhub
