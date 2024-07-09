import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepositoy
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()

def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepositoy(conn)

    trips_infos = {
        'id': str(uuid.uuid4()),
        'destination': 'Fortaleza',
        'start_date': datetime.strptime("09/07/2024", "%d/%m/%Y"),
        'end_date': datetime.strptime("09/07/2024", "%d/%m/%Y") + timedelta(days=5),
        'owner_name': 'Willian',
        'owner_email': "willian@email.com"
    }

    trips_repository.creat_trip(trips_infos)    