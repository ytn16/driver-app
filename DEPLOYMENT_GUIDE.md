# Deploying to autosign.store (GoDaddy Domain)

This guide will help you deploy your Driver Registration web app to your autosign.store domain.

## Deployment Options

You have several options for hosting your Flask app with a GoDaddy domain:

### Option 1: Use a VPS/Cloud Provider (Recommended)
- DigitalOcean, Linode, AWS, Google Cloud, or Azure
- Full control, scalable, professional
- Point your GoDaddy domain to the VPS

### Option 2: Use a Platform-as-a-Service (Easiest)
- Heroku, PythonAnywhere, Render, or Railway
- Very easy deployment, good for small apps
- Point your GoDaddy domain to the platform

### Option 3: GoDaddy Web Hosting
- Use GoDaddy's own hosting (if you purchased it)
- Limited Python support, may require VPS upgrade

---

## RECOMMENDED: Deploy to PythonAnywhere (Free Tier Available)

PythonAnywhere is the easiest option for Flask apps and has a free tier.

### Step 1: Sign Up for PythonAnywhere

1. Go to https://www.pythonanywhere.com
2. Click "Start running Python online in less than a minute"
3. Choose the **Free** plan (Beginner account)
4. Create your account

### Step 2: Upload Your Code

1. Log into PythonAnywhere dashboard
2. Go to **Files** tab
3. Click "Upload a file"
4. Upload all files from your `driver_app` folder:
   - `app.py`
   - `requirements.txt`
   - All files in `templates/` folder

Or use Git:
```bash
# In PythonAnywhere Bash console
git clone <your-git-repo-url>
cd driver_app
```

### Step 3: Set Up Virtual Environment

In PythonAnywhere **Bash console**:

```bash
cd driver_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Configure Web App

1. Go to **Web** tab in PythonAnywhere
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select **Python 3.10** (or latest available)
5. Click "Next"

### Step 5: Configure WSGI File

1. In the **Web** tab, click on the WSGI configuration file link
2. Delete everything and replace with:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/driver_app'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variable for Flask
os.environ['FLASK_APP'] = 'app.py'

# Import Flask app
from app import app as application
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

### Step 6: Set Virtual Environment Path

1. In the **Web** tab, find "Virtualenv" section
2. Enter the path: `/home/YOUR_USERNAME/driver_app/venv`
3. Click the checkmark

### Step 7: Reload Web App

1. Scroll to top of **Web** tab
2. Click the green "Reload" button
3. Your app is now live at: `YOUR_USERNAME.pythonanywhere.com`

### Step 8: Connect Your Custom Domain (autosign.store)

**Note**: Custom domains require a paid PythonAnywhere account ($5/month)

1. Upgrade to a paid account on PythonAnywhere
2. In PythonAnywhere **Web** tab:
   - Add `autosign.store` and `www.autosign.store` to the web app

3. In your **GoDaddy account**:
   - Go to DNS Management for autosign.store
   - Add these DNS records:

```
Type: A
Name: @
Value: <PythonAnywhere IP address>
TTL: 600

Type: CNAME
Name: www
Value: YOUR_USERNAME.pythonanywhere.com
TTL: 600
```

4. Wait 24-48 hours for DNS propagation

---

## ALTERNATIVE: Deploy to Heroku

Heroku is another easy option but requires a credit card (free tier available).

### Step 1: Install Heroku CLI

Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Create Production Files

You need to add these files to your `driver_app` folder:

**Procfile** (no extension):
```
web: gunicorn app:app
```

**runtime.txt**:
```
python-3.11.9
```

**Updated requirements.txt**:
```
Flask==3.0.0
gunicorn==21.2.0
```

### Step 3: Initialize Git Repository

```bash
cd driver_app
git init
git add .
git commit -m "Initial commit"
```

### Step 4: Create Heroku App

```bash
heroku login
heroku create autosign-driver-app
```

### Step 5: Deploy to Heroku

```bash
git push heroku main
```

Your app will be live at: `autosign-driver-app.herokuapp.com`

### Step 6: Connect Custom Domain

```bash
heroku domains:add autosign.store
heroku domains:add www.autosign.store
```

Heroku will give you DNS targets. Add them to GoDaddy:

1. Go to GoDaddy DNS Management
2. Add the CNAME records Heroku provides

---

## ALTERNATIVE: Deploy to a VPS (Most Control)

If you want full control, use a VPS like DigitalOcean.

### Step 1: Create a Droplet

1. Sign up at https://www.digitalocean.com
2. Create a "Droplet" (VPS)
3. Choose **Ubuntu 22.04**
4. Choose the $6/month plan
5. Note the IP address

### Step 2: Connect via SSH

```bash
ssh root@YOUR_DROPLET_IP
```

### Step 3: Install Dependencies

```bash
apt update
apt upgrade -y
apt install python3 python3-pip python3-venv nginx -y
```

### Step 4: Upload Your Code

```bash
mkdir -p /var/www/driver_app
cd /var/www/driver_app
# Upload your files here via SCP or Git
```

### Step 5: Set Up Python Environment

```bash
cd /var/www/driver_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

### Step 6: Create Systemd Service

Create `/etc/systemd/system/driver_app.service`:

```ini
[Unit]
Description=Driver App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/driver_app
Environment="PATH=/var/www/driver_app/venv/bin"
ExecStart=/var/www/driver_app/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```

Start the service:
```bash
systemctl start driver_app
systemctl enable driver_app
```

### Step 7: Configure Nginx

Create `/etc/nginx/sites-available/driver_app`:

```nginx
server {
    listen 80;
    server_name autosign.store www.autosign.store;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Enable the site:
```bash
ln -s /etc/nginx/sites-available/driver_app /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

### Step 8: Point GoDaddy Domain to VPS

1. Go to GoDaddy DNS Management
2. Update A record:
   - Type: A
   - Name: @
   - Value: YOUR_DROPLET_IP
   - TTL: 600

3. Update CNAME record:
   - Type: CNAME
   - Name: www
   - Value: @
   - TTL: 600

### Step 9: Set Up SSL (HTTPS)

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d autosign.store -d www.autosign.store
```

---

## Important: Production Configuration Changes

Before deploying, update `app.py`:

```python
import os

app = Flask(__name__)

# Use environment variable for secret key
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key-change-me')

# Set to False for production
debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'

if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
```

Generate a secure secret key:
```python
import secrets
print(secrets.token_hex(32))
```

Set it as an environment variable on your hosting platform.

---

## DNS Propagation Time

After updating DNS records in GoDaddy:
- **Minimum**: 30 minutes
- **Typical**: 4-8 hours
- **Maximum**: 24-48 hours

Check propagation status at: https://dnschecker.org

---

## Recommended Approach for Beginners

**For easiest deployment:**

1. **Sign up for PythonAnywhere** (free tier)
2. **Upload your code** using their web interface
3. **Configure the web app** following their wizard
4. **Test it** at your-username.pythonanywhere.com
5. **Upgrade to paid** ($5/month) to use autosign.store
6. **Configure DNS** in GoDaddy to point to PythonAnywhere

**Total cost**: $5/month (PythonAnywhere) + domain cost

---

## Need Help?

If you need specific help with any of these steps, let me know which hosting option you'd like to use and I can provide more detailed instructions!
