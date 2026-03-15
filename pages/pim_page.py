"""Module for PIM Employee List Page Objects."""


class PIMPage:
    """Handle PIM page locators using robust scoped filters."""

    def __init__(self, page):
        self.page = page


        self._name_group = page.locator(".oxd-input-group").filter(has_text="Employee Name")
        self._id_group = page.locator(".oxd-input-group").filter(has_text="Employee Id")

        self._search_btn = page.get_by_role("button", name="Search")
        self._reset_btn = page.get_by_role("button", name="Reset")

    def search_employee(self, name=None, emp_id=None):
        """Perform search by targeting inputs within their respective groups."""
        self._reset_btn.click()

        if name:

            name_input = self._name_group.get_by_placeholder("Type for hints...")
            name_input.wait_for(state="visible")
            name_input.fill(name)

        if emp_id:

            id_input = self._id_group.locator("input")
            id_input.wait_for(state="visible")
            id_input.fill(emp_id)

        self._search_btn.click()

        self.page.wait_for_timeout(2000)

    def has_no_results_message(self):
        """Verify if 'No Records Found' span is visible in the table."""
        return self.page.locator("span").get_by_text("No Records Found").is_visible()

    def is_record_visible(self):
        """Verify if at least one employee record is displayed."""
        return not self.has_no_results_message()
