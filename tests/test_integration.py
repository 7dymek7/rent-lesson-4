from src.models import Apartment
from src.manager import Manager
from src.models import Parameters
from src.models import Tenant


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_all_tenants_in_manager():
    parameters = Parameters()
    manager = Manager(parameters)
    
    expected_tenant_names = {
        "Jan Nowak",
        "Adam Kowalski",
        "Ewa Adamska",
    }
    
    manager_tenant_names = {tenant.name for tenant in manager.tenants.values()}
    
    for name in expected_tenant_names:
        assert name in manager_tenant_names
