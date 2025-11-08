# Driver Registration Web App - Usage Guide

## Application is Running!

The web application is now running at:
- **Local URL**: http://127.0.0.1:5000
- **Network URL**: http://192.168.3.5:5000

## How to Use

### 1. Home Page
Navigate to: http://localhost:5000

You'll see two buttons:
- **Register** - Takes you to URL1 (registration page)
- **Check Status** - Takes you to URL2 (status page)

### 2. URL1 - Registration Page
Navigate to: **http://localhost:5000/register**

This page allows you to:
1. Enter a username
2. Select whether you are a new driver (Yes/No)
3. Click "Register" to save your information

After registration, you'll be redirected to a success page.

### 3. URL2 - Status Page
Navigate to: **http://localhost:5000/status**

This page allows you to:
1. Enter a username
2. Click "Check Status"
3. View the result:
   - If the user is a new driver: Shows "Username is a NEW DRIVER"
   - If the user is not a new driver: Shows "Username is NOT a new driver (experienced driver)"
   - If the user doesn't exist: Shows error message prompting to register

## Example Usage Flow

### Scenario 1: New Driver Registration
1. Go to http://localhost:5000/register
2. Enter username: "john_doe"
3. Select: "Yes, I am a new driver"
4. Click "Register"
5. Go to http://localhost:5000/status
6. Enter username: "john_doe"
7. Result: "john_doe is a NEW DRIVER"

### Scenario 2: Experienced Driver Registration
1. Go to http://localhost:5000/register
2. Enter username: "jane_smith"
3. Select: "No, I am not a new driver"
4. Click "Register"
5. Go to http://localhost:5000/status
6. Enter username: "jane_smith"
7. Result: "jane_smith is NOT a new driver (experienced driver)"

## Data Storage

All user data is stored in `users_data.json` in the same directory as the application.

Example content:
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

## Stopping the Application

To stop the web server:
- Press `Ctrl+C` in the terminal where the app is running

## Testing the URLs Directly

You can also test the URLs directly in your browser:

- **URL1 (Registration)**: http://localhost:5000/register
- **URL2 (Status)**: http://localhost:5000/status

## Features

- ✅ Clean, responsive UI
- ✅ Form validation
- ✅ Persistent data storage (JSON file)
- ✅ Session support for convenience
- ✅ User-friendly error messages
- ✅ Color-coded status display

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use port 5001 instead
```

### Cannot Access from Network
- Make sure your firewall allows connections on port 5000
- Use the network URL: http://192.168.3.5:5000

### Data Not Persisting
- Check that `users_data.json` is being created in the `driver_app` directory
- Ensure the application has write permissions to the directory
