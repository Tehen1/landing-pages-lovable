# 🚀 Vercel Deployment + Custom Domain Guide

## 📍 Repository
**GitHub:** https://github.com/Tehen1/landing-pages-lovable

---

## Option 1: Deploy via Vercel CLI (Recommandé)

### 1.1 Installer Vercel CLI

```bash
npm i -g vercel
# ou
yarn global add vercel
# ou
pnpm add -g vercel
```

### 1.2 Login Vercel

```bash
vercel login
# Authentification via browser
```

### 1.3 Deploy

```bash
cd /Users/tehen/dev/projects/active/landing-pages

# Deploy preview (staging)
vercel

# Deploy production
vercel --prod
```

**Output attendu:**
```bash
🔍  Inspect: https://vercel.com/tehen1/landing-pages-lovable/xxxx [2s]
✅  Production: https://landing-pages-lovable.vercel.app [2s]
```

---

## Option 2: Deploy via GitHub Integration (Auto)

### 2.1 Connecter GitHub → Vercel

1. Aller sur https://vercel.com/new
2. Sélectionner **"Import Git Repository"**
3. Choisir `Tehen1/landing-pages-lovable`
4. Click **"Deploy"**

### 2.2 Configuration Auto-Deploy

```bash
# Dans les settings Vercel du projet:
Git → Production Branch: main
# Chaque push sur main = auto-deploy
```

---

## 🌐 Custom Domain Setup

### 3.1 Acheter/Ajouter Domain

```bash
# Option A: Acheter via Vercel
vercel domains buy ton-domaine.com

# Option B: Utiliser domaine existant
vercel domains add landing-pages-lovable ton-domaine.com
```

### 3.2 Configuration DNS

| Type | Nom | Valeur | TTL |
|------|-----|--------|-----|
| A | @ | 76.76.21.21 | 60 |
| CNAME | www | cname.vercel-dns.com | 60 |

**Pour sous-domaines:**
```bash
# Ex: apps.ton-domaine.com
vercel domains add landing-pages-lovable apps.ton-domaine.com
```

### 3.3 Vérifier Configuration

```bash
vercel domains inspect ton-domaine.com
```

---

## 🎯 URLs Par App (Proposition)

### Option A: Sous-domaines (Recommandé)
```
ai-chat.ton-domaine.com     → AI Poe Chat Verse
fixie.ton-domaine.com       → Fixie Dashboard Navigator
seo.ton-domaine.com       → SEO SEA Guru
```

### Option B: Path-based
```
ton-domaine.com/ai-chat   → AI Poe Chat Verse
ton-domaine.com/fixie     → Fixie Dashboard Navigator
ton-domaine.com/seo       → SEO SEA Guru
```

### Configuration Vercel (vercel.json)

Créer `vercel.json` à la racine:

```json
{
  "redirects": [
    {
      "source": "/ai-chat",
      "destination": "/ai-poe-chat-verse.html"
    },
    {
      "source": "/fixie",
      "destination": "/fixie-dashboard-navigator-25.html"
    },
    {
      "source": "/seo",
      "destination": "/seo-sea-guru.html"
    }
  ],
  "rewrites": [
    {
      "source": "/",
      "destination": "/index.html"
    }
  ]
}
```

---

## 📊 Analytics & Tracking

### 4.1 Ajouter Vercel Analytics

```bash
# Installer package
npm i @vercel/analytics

# Ajouter dans chaque HTML (avant </head>)
<script defer src="/_vercel/insights/script.js"></script>
```

### 4.2 Vitesse (Core Web Vitals)

Dashboard: https://vercel.com/tehen1/landing-pages-lovable/speed-insights

---

## 🔒 Environment Variables (Stripe)

### 5.1 Configurer dans Vercel Dashboard

```bash
1. Project Settings → Environment Variables
2. Ajouter:
   
   STRIPE_PUBLISHABLE_KEY = pk_live_xxxxx
   STRIPE_SECRET_KEY = sk_live_xxxxx
   
3. Scope: Production + Preview
```

### 5.2 Ou via CLI

```bash
vercel env add STRIPE_PUBLISHABLE_KEY production
vercel env add STRIPE_SECRET_KEY production
```

---

## 🔄 Workflow Complet

```bash
# 1. Modifier landing page
open ai-poe-chat-verse.html

# 2. Commit & Push
git add .
git commit -m "Update AI Chat CTA button"
git push origin main

# 3. Auto-deploy sur Vercel (via GitHub integration)
# → https://vercel.com/tehen1/landing-pages-lovable

# 4. Vérifier le déploiement
vercel --version
# ou check: https://ton-domaine.com/ai-chat
```

---

## 🎯 Commandes Récapitulatives

| Commande | Action |
|----------|--------|
| `vercel` | Deploy preview |
| `vercel --prod` | Deploy production |
| `vercel domains add <domain>` | Ajouter domain |
| `vercel env add <key>` | Ajouter env var |
| `vercel logs` | Voir logs |
| `vercel ls` | Liste deployments |

---

## 🚨 Troubleshooting

### Issue: "Command not found"
```bash
npm i -g vercel
# Redémarrer terminal
```

### Issue: "Not authorized"
```bash
vercel login
# Réauthentifier
```

### Issue: Domain déjà utilisé
```bash
# Vérifier ownership
vercel domains inspect ton-domaine.com

# Transfer si nécessaire
vercel domains transfer-in ton-domaine.com
```

---

## 📞 Support

- **Vercel Docs:** https://vercel.com/docs
- **Custom Domains:** https://vercel.com/docs/concepts/projects/custom-domains
- **CLI Reference:** https://vercel.com/docs/cli

---

**Next Step:** Créer `index.html` (hub page) + `vercel.json` (redirects)
