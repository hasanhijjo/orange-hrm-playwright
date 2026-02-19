from playwright.sync_api import Page, expect

def test_add_employee(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=10000)

    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name="Add").click()

    page.get_by_role("textbox", name="First Name").fill("Hassan")
    page.get_by_role("textbox", name="Middle Name").fill("Hassan")
    page.get_by_role("textbox", name="Last Name").fill("Hijjo")

    page.get_by_role("button", name="Save").click()

    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible(timeout=10000)
