from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import DATABASE_URL

motor = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=motor, autoflush=False, autocommit=False)