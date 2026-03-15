"""Tests for PIM Search functionality in OrangeHRM."""
import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


@pytest.fixture(autouse=True)
def setup_pim(page):
    """Login and navigate to PIM module before each test."""
    login_pg = LoginPage(page)

    login_pg.navigate()
    page.wait_for_load_state("domcontentloaded")

    login_pg.login("Admin", "admin123")

    page.wait_for_selector(".oxd-sidepanel", timeout=20000)

    page.get_by_role("link", name="PIM").click()

    page.wait_for_selector(".oxd-table-filter", timeout=20000)


def test_search_by_valid_name_and_id(page):
    """Positive: Search for an existing employee using both Name and ID."""
    pim_pg = PIMPage(page)

    target_name = "Charlotte"
    target_id = "00392"

    pim_pg.search_employee(name=target_name, emp_id=target_id)

    assert pim_pg.is_record_visible() is True, f"Employee {target_name} should be found."


def test_search_non_existent_employee(page):
    """Negative: Search for a fake ID."""
    pim_pg = PIMPage(page)

    pim_pg.search_employee(emp_id="9999999")

    assert pim_pg.has_no_results_message() is True, "Should display 'No Records Found'."
