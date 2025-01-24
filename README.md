# OpenWeatherMap Email Service

This script allows you to send an email with details about the OpenWeatherMap service along with an attached `.docx` file.

## Requirements

- Python 3.x
- `smtplib` (Python standard library)
- `ssl` (Python standard library)
- A valid Gmail account
- A `.docx` file named `OpenWeatherMap service.docx` in the same directory as the script

## Setup

1. Install the required Python dependencies:
    ```bash
    pip install email
    ```

2. Save your Gmail account password in a `credentials.py` file with the following content:
    ```python
    password = 'your_password_here'
    ```

3. Update the script with your sender and recipient email addresses:
    ```python
    sender = "Your Gmail address here"
    recipient = "Recipient's email address here"
    ```

4. Ensure the file `OpenWeatherMap service.docx` is present in the same directory as the script.

## Usage

Simply run the script to send the email:

```bash
python your_script_name.py
