#!/usr/bin/env python3
"""
Setup Stripe Products & Prices pour les 3 Top Lovable Apps
Usage: python3 setup-stripe-products.py --api-key sk_test_...
"""
import argparse
import json
import stripe
from pathlib import Path

# Configuration des 3 apps avec pricing
PRODUCTS_CONFIG = [
    {
        "name": "AI Poe Chat Verse",
        "description": "Chatbot IA avancé pour entreprises et développeurs",
        "metadata": {"app": "ai-poe-chat-verse", "category": "ai-chatbot"},
        "tiers": [
            {
                "name": "Starter",
                "price": 2900,  # cents ($29)
                "interval": "month",
                "features": ["1 chatbot", "1K conversations/mois", "Support email"]
            },
            {
                "name": "Pro",
                "price": 7900,  # cents ($79)
                "interval": "month",
                "popular": True,
                "features": ["5 chatbots", "10K conversations/mois", "Priority support", "API access"]
            },
            {
                "name": "Enterprise",
                "price": 19900,  # cents ($199)
                "interval": "month",
                "features": ["Chatbots illimités", "Conversations illimitées", "SLA 99.9%", "Customer Success Manager dédié"]
            }
        ]
    },
    {
        "name": "Fixie Dashboard Navigator",
        "description": "Dashboard Web3 pour cyclistes - Track rides & earn tokens",
        "metadata": {"app": "fixie-dashboard", "category": "web3-fitness"},
        "tiers": [
            {
                "name": "Starter",
                "price": 2900,
                "interval": "month",
                "features": ["Tracking basique", "NFT starter pack", "Accès communauté"]
            },
            {
                "name": "Pro Rider",
                "price": 7900,
                "interval": "month",
                "popular": True,
                "features": ["Tracking avancé", "Gains tokens x2", "NFT premium", "Sync Strava"]
            },
            {
                "name": "Elite",
                "price": 19900,
                "interval": "month",
                "features": ["Illimité", "Early NFT drops", "Governance DAO", "Support VIP"]
            }
        ]
    },
    {
        "name": "SEO SEA Guru",
        "description": "Suite SEO propulsée par l'IA pour PME et agences",
        "metadata": {"app": "seo-sea-guru", "category": "seo-marketing"},
        "tiers": [
            {
                "name": "Starter",
                "price": 2900,
                "interval": "month",
                "features": ["1 site", "50 mots-clés", "Rapports hebdomadaires"]
            },
            {
                "name": "Pro",
                "price": 7900,
                "interval": "month",
                "popular": True,
                "features": ["10 sites", "500 mots-clés", "Content AI", "API access"]
            },
            {
                "name": "Agency",
                "price": 19900,
                "interval": "month",
                "features": ["Sites illimités", "White-label", "Multi-accounts", "Support prioritaire"]
            }
        ]
    }
]

def create_product_with_prices(stripe_key, product_config, dry_run=False):
    """Crée un produit Stripe avec ses prix"""
    if dry_run:
        print(f"\n[DRY RUN] Création produit: {product_config['name']}")
        for tier in product_config['tiers']:
            price_str = f"${tier['price']/100:.0f}/{tier['interval']}"
            popular = " [POPULAR]" if tier.get('popular') else ""
            print(f"  └── {tier['name']}: {price_str}{popular}")
        return None
    
    stripe.api_key = stripe_key
    
    # Créer le produit
    product = stripe.Product.create(
        name=product_config['name'],
        description=product_config['description'],
        metadata=product_config['metadata']
    )
    
    print(f"\n✅ Produit créé: {product.name} (ID: {product.id})")
    
    # Créer les prix pour chaque tier
    prices_created = []
    for tier in product_config['tiers']:
        price_data = {
            'product': product.id,
            'unit_amount': tier['price'],
            'currency': 'usd',
            'recurring': {
                'interval': tier['interval'],
                'interval_count': 1
            },
            'metadata': {
                'tier': tier['name'],
                'features': json.dumps(tier['features']),
                'popular': str(tier.get('popular', False))
            }
        }
        
        price = stripe.Price.create(**price_data)
        prices_created.append({
            'tier': tier['name'],
            'price_id': price.id,
            'amount': tier['price'],
            'popular': tier.get('popular', False)
        })
        
        popular_marker = " ⭐" if tier.get('popular') else ""
        print(f"  └── {tier['name']}: ${tier['price']/100:.0f}/{tier['interval']}{popular_marker}")
    
    return {
        'product_id': product.id,
        'name': product.name,
        'prices': prices_created
    }

def create_checkout_sessions_config(stripe_key, products_data, dry_run=False):
    """Génère les URLs de checkout pour chaque produit"""
    checkout_config = {}
    
    for product in products_data:
        app_key = product['name'].lower().replace(' ', '-')
        checkout_config[app_key] = {
            'product_id': product['product_id'],
            'tiers': {}
        }
        
        for price in product['prices']:
            tier_key = price['tier'].lower().replace(' ', '_')
            checkout_config[app_key]['tiers'][tier_key] = {
                'price_id': price['price_id'],
                'amount': price['amount'],
                'popular': price['popular']
            }
    
    # Sauvegarder la config
    config_path = Path('/Users/tehen/dev/projects/active/landing-pages/stripe-config.json')
    with open(config_path, 'w') as f:
        json.dump(checkout_config, f, indent=2)
    
    print(f"\n📁 Configuration Stripe sauvegardée: {config_path}")
    return checkout_config

def generate_checkout_urls_example(checkout_config):
    """Génère des exemples d'URLs de checkout"""
    print("\n" + "="*70)
    print("🔗 EXEMPLES D'URLs DE CHECKOUT STRIPE")
    print("="*70)
    
    for app_name, config in checkout_config.items():
        print(f"\n{app_name.upper()}:")
        for tier_name, tier_config in config['tiers'].items():
            price_id = tier_config['price_id']
            url = f"https://checkout.stripe.com/pay/{price_id}"
            print(f"  └── {tier_name}: {url}")

def main():
    parser = argparse.ArgumentParser(description='Setup Stripe products for Top 3 Lovable Apps')
    parser.add_argument('--api-key', required=True, help='Stripe API key (sk_test_... or sk_live_...)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without creating products')
    args = parser.parse_args()
    
    print("="*70)
    print("💳 SETUP STRIPE PRODUCTS — Top 3 Lovable Apps")
    print("="*70)
    
    if args.dry_run:
        print("\n🔍 MODE DRY-RUN (pas de création réelle)")
    
    # Créer les produits
    products_data = []
    for product_config in PRODUCTS_CONFIG:
        result = create_product_with_prices(args.api_key, product_config, args.dry_run)
        if result:
            products_data.append(result)
    
    # Générer la config de checkout
    if products_data and not args.dry_run:
        checkout_config = create_checkout_sessions_config(args.api_key, products_data)
        generate_checkout_urls_example(checkout_config)
    
    print("\n" + "="*70)
    if args.dry_run:
        print("✅ DRY-RUN terminé. Lance sans --dry-run pour créer les produits.")
    else:
        print("✅ Setup Stripe terminé avec succès!")
        print("\n⚠️  IMPORTANT: Copie les Price IDs dans tes landing pages:")
        print("   - Modifie les boutons 'Démarrer gratuitement'")
        print("   - Ajoute les liens checkout Stripe")
        print("   - Teste en mode TEST avant de passer en LIVE")
    print("="*70)

if __name__ == '__main__':
    main()
