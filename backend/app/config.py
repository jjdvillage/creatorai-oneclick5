import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY','')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY','')
STRIPE_PRICE_ID = os.getenv('STRIPE_PRICE_ID','')
JWT_SECRET = os.getenv('JWT_SECRET','devsecret_change_me')
JWT_ALGO = 'HS256'
DATABASE_URL = os.getenv('DATABASE_URL','sqlite:///./data.db')
CLIENT_URL = os.getenv('CLIENT_URL','*')
FREE_MONTHLY_GENERATIONS = int(os.getenv('FREE_MONTHLY_GENERATIONS','100'))
PRO_MONTHLY_GENERATIONS = int(os.getenv('PRO_MONTHLY_GENERATIONS','5000'))
RESEND_API_KEY = os.getenv('RESEND_API_KEY','')
