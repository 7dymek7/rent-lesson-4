import pytest

from pydantic import ValidationError
from src.models import Apartment
from src.models import Tenant


def test_apartment_fields():
    data = Apartment(
        key="apart-test",
        name="Test Apartment",
        location="Test Location",
        area_m2=50.0,
        rooms={
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    )
    assert data.key == "apart-test"
    assert data.name == "Test Apartment"
    assert data.location == "Test Location"
    assert data.area_m2 == 50.0
    assert len(data.rooms) == 2
    
def test_all_fields_full():
    tenant = Tenant(
        name="Jan Nowak",
        apartment="apart-polanka",
        room="room-bigger",
        rent_pln=1500.0,
        deposit_pln=3000.0,
        date_agreement_from="2024-01-01",
        date_agreement_to="2024-12-31"
    )

    assert tenant.name == "Jan Nowak"
    assert tenant.apartment == "apart-polanka"
    assert tenant.room == "room-bigger"
    assert tenant.rent_pln == 1500.0
    assert tenant.deposit_pln == 3000.0
    assert tenant.date_agreement_from == "2024-01-01"
    assert tenant.date_agreement_to == "2024-12-31"
    
def test_from_dict():
    data = {
        "name": "Adam Kowalski",
        "apartment": "apart-polanka",
        "room": "room-medium",
        "rent_pln": 1400.0,
        "deposit_pln": 2900.0,
        "date_agreement_from": "2024-01-01",
        "date_agreement_to": "2024-12-31"
    }

    tenant = Tenant(**data)

    assert tenant.name == "Adam Kowalski"
    assert tenant.apartment == "apart-polanka"
    assert tenant.room == "room-medium"
    assert tenant.rent_pln == 1400.0

    invalid_data = {
        "name": "",
        "apartment": "apart-polanka",
        "room": "",
        "rent_pln": None,
        "deposit_pln": 0,
        "date_agreement_from": "",
        "date_agreement_to": ""
    }

    with pytest.raises(ValidationError):
        Tenant(**invalid_data)


        
def test_apartment_from_dict():
    data = {
        "key": "apart-test",
        "name": "Test Apartment",
        "location": "Test Location",
        "area_m2": 50.0,
        "rooms": {
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    }
    apartment = Apartment(**data)
    assert apartment.key == data["key"]
    assert apartment.name == data["name"]
    assert apartment.location == data["location"]
    assert apartment.area_m2 == data["area_m2"]
    assert len(apartment.rooms) == len(data["rooms"])

    data['area_m2'] = "25m2" # Invalid field
    with pytest.raises(ValidationError):
        wrong_apartment = Apartment(**data)
