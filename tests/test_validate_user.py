import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

@pytest.mark.asyncio
async def test_validate_user(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    admin = AdminPage(page)

    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    await login.login("Admin", "admin123")
    await dashboard.go_to_admin()

    is_valid = await admin.validate_user_details("testuser1", role="Admin", status="Disabled")
    assert is_valid, "User details do not match expected role and status"
