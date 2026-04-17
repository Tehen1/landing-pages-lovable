# 🚀 Top 3 Lovable Apps — Landing Pages

Landing pages optimisées pour les 3 apps avec le meilleur potentiel MRR.

## 📱 Apps

| App | Category | MRR Score | Status | URL |
|-----|----------|-----------|--------|-----|
| **AI Poe Chat Verse** | AI/Chatbot | 6.7/10 | 🟢 Published | [Live Demo](https://ai-poe-chat-verse.lovable.app/) |
| **Fixie Dashboard Navigator** | Fitness/Web3 | 6.3/10 | 🟢 Published | [Live Demo](https://fixie-dashboard-navigator-25.lovable.app/) |
| **SEO SEA Guru** | SEO/Marketing | 6.1/10 | 🟢 Published | [Live Demo](https://seo-sea-guru.lovable.app/) |

## 🎯 Quick Start

### 1. Déployer sur Vercel

```bash
# Installer Vercel CLI
npm i -g vercel

# Déployer
vercel --prod
```

### 2. Setup Stripe (Revenus)

```bash
# 1. Récupérer ta clé API Stripe
# Dashboard: https://dashboard.stripe.com/apikeys

# 2. Tester en mode dry-run
python3 setup-stripe-products.py --api-key sk_test_xxx --dry-run

# 3. Créer les produits (mode TEST)
python3 setup-stripe-products.py --api-key sk_test_xxx

# 4. Passer en LIVE (quand prêt)
python3 setup-stripe-products.py --api-key sk_live_xxx
```

### 3. Intégrer Checkout

Les Price IDs sont sauvegardés dans `stripe-config.json`. Modifie les boutons dans les HTML :

```html
<!-- Exemple: AI Poe Chat Verse -->
<a href="https://checkout.stripe.com/pay/{PRICE_ID}" class="btn-primary">
  Démarrer gratuitement →
</a>
```

## 💰 Pricing Strategy

### AI Poe Chat Verse
- **Starter**: $29/mo — 1 chatbot, 1K conversations
- **Pro** ⭐: $79/mo — 5 chatbots, 10K conversations, API
- **Enterprise**: $199/mo — Illimité, SLA 99.9%, CSM

### Fixie Dashboard Navigator
- **Starter**: $29/mo — Tracking basique, NFT starter
- **Pro Rider** ⭐: $79/mo — Tracking avancé, gains x2, Strava sync
- **Elite**: $199/mo — Illimité, governance DAO, VIP support

### SEO SEA Guru
- **Starter**: $29/mo — 1 site, 50 keywords, rapports hebdo
- **Pro** ⭐: $79/mo — 10 sites, 500 keywords, Content AI
- **Agency**: $199/mo — Illimité, white-label, multi-accounts

## 📊 Analytics & Tracking

### Requis
- Google Analytics 4
- Mixpanel ou Amplitude (funnel analysis)
- Stripe Dashboard (revenus)

### KPIs à tracker
```javascript
// À ajouter dans les landing pages
// Page view
gtag('event', 'page_view', { app: 'ai-chat' });

// CTA clicks
gtag('event', 'cta_click', { tier: 'pro', location: 'hero' });

// Trial start (Stripe webhook)
// Conversion (Stripe webhook)
```

## 🔄 Funnel Optimization

### Current Flow
```
Landing Page → Stripe Checkout → Payment → App Dashboard
     ↓              ↓                ↓          ↓
  Analytics    Conversion      Revenue      Retention
```

### Recommended Improvements
1. **Add email capture** avant checkout (lead nurturing)
2. **Interactive demo** sans signup (activation)
3. **Social proof** dynamique (avis clients)
4. **Exit intent** popup (recovery)

## 📁 Structure

```
landing-pages/
├── ai-poe-chat-verse.html          # Landing page AI Chat
├── fixie-dashboard-navigator-25.html # Landing page Fixie
├── seo-sea-guru.html                 # Landing page SEO
├── landing-pages-config.json         # Configuration complète
├── setup-stripe-products.py          # Script setup Stripe
├── stripe-config.json                # Price IDs (auto-généré)
└── README.md                         # Ce fichier
```

## 🚀 Roadmap

### Semaine 1
- [x] Landing pages créées
- [x] Stripe products configurés
- [ ] Déploiement Vercel
- [ ] Analytics setup

### Semaine 2
- [ ] Beta testing (20 users/app)
- [ ] Email sequences (ConvertKit/Mailchimp)
- [ ] Retargeting pixels (Facebook/Google)

### Semaine 3
- [ ] Product Hunt launch (AI Chat)
- [ ] Influencer outreach (Fixie cycling)
- [ ] Content marketing (SEO guides)

## 🛠️ Development

### Modifier une landing page
```bash
# Éditer le HTML directement
open ai-poe-chat-verse.html

# Tester localement
python3 -m http.server 8000
# → http://localhost:8000/ai-poe-chat-verse.html
```

### Régénérer depuis la config
```bash
# Si tu veux modifier la config et régénérer
python3 ../landing-pages-generator.py
```

## 📞 Support

### Stripe
- Dashboard: https://dashboard.stripe.com
- Webhook testing: https://stripe.com/docs/webhooks/test
- Checkout docs: https://stripe.com/docs/payments/checkout

### Vercel
- Dashboard: https://vercel.com/dashboard
- Custom domains: https://vercel.com/docs/concepts/projects/custom-domains

## 🎯 Objectifs MRR

| App | MRR Mois 1 | MRR Mois 3 | MRR Mois 6 |
|-----|------------|------------|------------|
| AI Chat | $2K | $10K | $25K |
| Fixie | $1K | $5K | $12K |
| SEO | $1.5K | $6K | $15K |
| **TOTAL** | **$4.5K** | **$21K** | **$52K** |

---

**Lovable.dev** • Propulsé par ❤️ et beaucoup de café
