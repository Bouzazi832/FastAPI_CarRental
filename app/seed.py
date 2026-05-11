"""
Seed script to populate the database with fake data for testing
"""
from faker import Faker
from sqlmodel import Session, select
from database import Locataire, Voiture, engine, create_tables
import random

fake = Faker('fr_FR')  # Using French locale for realistic data

# Sample car brands and models for a car rental company
CAR_DATA = [
    {"marque": "Peugeot", "modele": "208", "prix_location": 45.00},
    {"marque": "Peugeot", "modele": "3008", "prix_location": 65.00},
    {"marque": "Renault", "modele": "Clio", "prix_location": 40.00},
    {"marque": "Renault", "modele": "Megane", "prix_location": 55.00},
    {"marque": "Citroen", "modele": "C3", "prix_location": 35.00},
    {"marque": "Citroen", "modele": "C5", "prix_location": 70.00},
    {"marque": "Toyota", "modele": "Yaris", "prix_location": 50.00},
    {"marque": "Toyota", "modele": "RAV4", "prix_location": 75.00},
    {"marque": "Volkswagen", "modele": "Golf", "prix_location": 60.00},
    {"marque": "BMW", "modele": "320i", "prix_location": 85.00},
    {"marque": "Audi", "modele": "A3", "prix_location": 80.00},
    {"marque": "Mercedes", "modele": "C-Class", "prix_location": 95.00},
    {"marque": "Fiat", "modele": "500", "prix_location": 38.00},
    {"marque": "Hyundai", "modele": "i20", "prix_location": 42.00},
    {"marque": "Kia", "modele": "Picanto", "prix_location": 40.00},
]


def generate_fake_locataires(session: Session, count: int = 15):
    """Generate fake locataires (tenants) and add them to the database"""
    print(f"\n📝 Generating {count} fake locataires...")
    
    locataires = []
    for i in range(count):
        locataire = Locataire(
            nom=fake.last_name(),
            prenom=fake.first_name(),
            adresse=fake.address().replace('\n', ', ')
        )
        locataires.append(locataire)
        session.add(locataire)
    
    session.commit()
    print(f"✅ Added {count} locataires to database")
    return locataires


def generate_fake_voitures(session: Session, count: int = 20):
    """Generate fake voitures (cars) and add them to the database"""
    print(f"\n🚗 Generating {count} fake voitures...")
    
    voitures = []
    num_imma_base = 75000000  # Starting point for registration numbers
    
    for i in range(count):
        car_template = random.choice(CAR_DATA)
        voiture = Voiture(
            num_imma=num_imma_base + i,
            marque=car_template["marque"],
            modele=car_template["modele"],
            kilometrage=random.randint(1000, 150000),
            etat=random.choice([0, 0, 0, 1]),  # More cars available (etat=0) than rented (etat=1)
            prix_location=car_template["prix_location"],
            id_loc=None  # No owner initially
        )
        voitures.append(voiture)
        session.add(voiture)
    
    session.commit()
    print(f"✅ Added {count} voitures to database")
    return voitures


def assign_cars_to_renters(session: Session):
    """Assign some cars to renters (simulate rentals)"""
    print(f"\n🔗 Assigning some cars to renters...")
    
    # Get rented cars (etat=1)
    stmt = select(Voiture).where(Voiture.etat == 1)
    rented_cars = session.exec(stmt).all()
    
    # Get all locataires
    stmt = select(Locataire)
    locataires = session.exec(stmt).all()
    
    if not locataires:
        print("⚠️  No locataires found to assign cars to")
        return
    
    assigned_count = 0
    for car in rented_cars:
        locataire = random.choice(locataires)
        car.id_loc = locataire.id_loc
        session.add(car)
        assigned_count += 1
    
    session.commit()
    print(f"✅ Assigned {assigned_count} cars to renters")


def seed_database():
    """Main function to seed the database"""
    print("\n" + "="*50)
    print("🌱 Starting Database Seeding Process...")
    print("="*50)
    
    # Create tables first
    print("\n📦 Creating tables...")
    create_tables()
    print("✅ Tables created/verified")
    
    # Create session
    with Session(engine) as session:
        # Check if database is already populated
        stmt = select(Locataire)
        existing_locataires = session.exec(stmt).all()
        
        if existing_locataires:
            print(f"\n⚠️  Database already contains {len(existing_locataires)} locataires!")
            response = input("Do you want to clear the database and reseed? (yes/no): ").strip().lower()
            if response != 'yes':
                print("❌ Seeding cancelled")
                return
            else:
                print("\n🗑️  Clearing existing data...")
                # Delete all existing data
                session.query(Voiture).delete()
                session.query(Locataire).delete()
                session.commit()
                print("✅ Database cleared")
        
        # Generate and add fake data
        locataires = generate_fake_locataires(session, count=15)
        voitures = generate_fake_voitures(session, count=20)
        assign_cars_to_renters(session)
    
    print("\n" + "="*50)
    print("✅ Database seeding completed successfully!")
    print("="*50)
    print("\n📊 Summary:")
    print(f"   • Locataires created: 15")
    print(f"   • Voitures created: 20")
    print(f"   • Cars currently rented: ~5")
    print("\n")


if __name__ == "__main__":
    seed_database()
