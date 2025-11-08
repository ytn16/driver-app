# Driver Registration Web App

A simple Flask web application that allows users to register and specify whether they are new drivers, then displays their driver status.

## Features

- **URL1 (Registration)**: `/register` - Users can register and specify if they're a new driver
- **URL2 (Status)**: `/status` - Displays whether a user is or is not a new driver
- Data is stored in a JSON file for persistence
- Clean, responsive UI

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install Flask
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## URL Structure

- **Home**: `http://localhost:5000/`
- **URL1 (Registration)**: `http://localhost:5000/register`
- **URL2 (Status Check)**: `http://localhost:5000/status`

## How It Works

1. **Registration** (`/register`):
   - User enters their username
   - User selects whether they are a new driver (Yes/No)
   - Data is saved to `users_data.json`

2. **Status Check** (`/status`):
   - User enters their username
   - App displays: "Username is a NEW DRIVER" or "Username is NOT a new driver"
   - If user not found, shows error message

## Data Storage

User data is stored in `users_data.json` in the following format:
```json
{
  "john_doe": {
    "is_new_driver": true
  },
  "jane_smith": {
    "is_new_driver": false
  }
}
```

## Production Deployment

For production use:
1. Change the `secret_key` in `app.py` to a secure random value
2. Set `debug=False` in `app.run()`
3. Use a production WSGI server like Gunicorn or uWSGI
4. Consider using a proper database instead of JSON file storage
