import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

@pytest.mark.asyncio
async def test_search_user(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    admin = AdminPage(page)

    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    await login.login("Admin", "admin123")
    await dashboard.go_to_admin()

    found = await admin.search_user("testuser1")
    assert found, "User 'testuser1' should be found in the table"
