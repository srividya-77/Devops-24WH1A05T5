# Devops-24WH1A05T5

A registration form with a Python backend that saves submissions to a local file.

## What it does

The HTML form collects personal and professional details — name, email, password, phone, education, address, gender, skills, experience, certifications, projects, LinkedIn, GitHub, and availability. On submit, it validates the password match and phone number in the browser, then sends the data as JSON to a backend API. The Python server listens on port 8000 and appends each submission as a line to `registrations_log.txt`.

> **Note:** The form's fetch URL (`http://127.0.0`) is incomplete, so submissions will currently fail to reach the backend. The backend itself works correctly if you fix the URL to `http://127.0.0.1:8000/api/v1/register`.

## Built with

- HTML, CSS, vanilla JavaScript (frontend)
- Python standard library — `http.server`, `json` (backend, no third-party packages)

## How to run

**Backend:**
```bash
cd Devops-24WH1A05T5
python3 main.py
# Server starts at http://127.0.0.1:8000
```

**Frontend:**

Open `registration.html` directly in a browser. Fix the fetch URL in the `<script>` block to `http://127.0.0.1:8000/api/v1/register` before submitting.
