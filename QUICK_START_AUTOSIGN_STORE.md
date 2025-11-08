# Quick Start: Deploy to autosign.store

This is the **easiest way** to get your app live on autosign.store.

## Recommended: Use Render.com (Free Tier)

Render.com offers free hosting for web apps and makes it very easy to connect custom domains.

### Step 1: Sign Up for Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended) or email

### Step 2: Push Your Code to GitHub

First, create a GitHub repository:

1. Go to https://github.com/new
2. Create a new repository called "driver-registration-app"
3. Don't initialize with README (we have code already)

Then push your code:

```bash
cd d:/VS_Code_Claude/driver_app

# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/driver-registration-app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Create Web Service on Render

1. Log into Render dashboard
2. Click "New +" button → "Web Service"
3. Connect your GitHub account (if not already)
4. Select your "driver-registration-app" repository
5. Configure:
   - **Name**: autosign-driver-app
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"

Your app will deploy automatically! It will be live at:
`https://autosign-driver-app.onrender.com`

### Step 4: Set Environment Variables

In Render dashboard:
1. Go to your web service
2. Click "Environment" in left menu
3. Add environment variable:
   - **Key**: `SECRET_KEY`
   - **Value**: Generate a random key (see below)

To generate a secret key, run this on your computer:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it as the SECRET_KEY value.

### Step 5: Connect autosign.store Domain

In Render dashboard:
1. Go to your web service
2. Click "Settings"
3. Scroll to "Custom Domain"
4. Click "Add Custom Domain"
5. Enter: `autosign.store`
6. Click "Add"
7. Add another: `www.autosign.store`

Render will show you DNS records to add.

### Step 6: Update DNS in GoDaddy

1. Log into GoDaddy
2. Go to "My Products" → Find your domain "autosign.store"
3. Click "DNS" or "Manage DNS"
4. Add/Update these records:

**For the root domain (autosign.store):**
- Type: `CNAME`
- Name: `@` (or leave blank)
- Value: (the value Render gave you, something like `autosign-driver-app.onrender.com`)
- TTL: `600` (10 minutes)

**For www subdomain:**
- Type: `CNAME`
- Name: `www`
- Value: (the value Render gave you)
- TTL: `600`

**Note**: Some registrars don't allow CNAME for root domain. If GoDaddy doesn't allow it, use:
- Type: `A`
- Name: `@`
- Value: Get the IP from Render support or use their A records

5. Click "Save"

### Step 7: Wait for DNS Propagation

- Wait 10-60 minutes for DNS to update
- Check status at: https://dnschecker.org
- Enter your domain: `autosign.store`

### Step 8: Enable SSL (HTTPS)

Render automatically provides free SSL certificates!
- Once DNS is configured, Render will auto-generate SSL
- Your site will be accessible at: `https://autosign.store`

---

## Alternative: Use Railway.app (Also Free)

Railway is another great option:

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Flask and deploys
6. Add custom domain in settings
7. Update GoDaddy DNS records

---

## Testing Your Live Site

Once deployed:

1. **Register a user**:
   - Go to https://autosign.store/register
   - Enter username and driver status
   - Click Register

2. **Check status**:
   - Go to https://autosign.store/status
   - Your status should appear automatically!

3. **Test on phone**:
   - Open https://autosign.store/register on your phone
   - Register
   - Go to https://autosign.store/status
   - Status appears automatically on your phone!

---

## Troubleshooting

### Site not loading?
- Check DNS propagation at https://dnschecker.org
- Wait up to 48 hours (usually much faster)
- Verify DNS records in GoDaddy match what Render gave you

### 404 Error?
- Check that your app is running on Render
- Look at Render logs for errors
- Make sure requirements.txt includes all dependencies

### Session not persisting?
- Make sure you set the SECRET_KEY environment variable
- Check browser cookies are enabled
- Try clearing cookies and registering again

### HTTPS not working?
- Wait for Render to provision SSL (can take 10-15 minutes after DNS)
- Check that DNS is fully propagated
- Contact Render support if it takes longer than 24 hours

---

## Cost Summary

- **Render Free Tier**: $0/month
  - Includes: 750 hours/month (enough for 24/7)
  - Limitations: Sleeps after 15 min inactivity (wakes on first request)

- **GoDaddy Domain**: ~$12/year (you already have this)

- **Total**: $0/month + domain cost

**To avoid sleep/wake delay**, upgrade to Render paid ($7/month)

---

## Files Checklist

Make sure these files are in your repository:

- ✅ `app.py` (main application)
- ✅ `requirements.txt` (dependencies)
- ✅ `Procfile` (tells Render how to start app)
- ✅ `runtime.txt` (specifies Python version)
- ✅ `templates/` folder with all HTML files
- ✅ `.gitignore` (optional, to exclude users_data.json)

Create `.gitignore`:
```
users_data.json
__pycache__/
*.pyc
.env
venv/
```

---

## Next Steps After Deployment

1. **Test thoroughly** on desktop and mobile
2. **Share the link** with your users
3. **Monitor** the Render dashboard for errors
4. **Backup** your users_data.json periodically

Need help with any step? Let me know!
