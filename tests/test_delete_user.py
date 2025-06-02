import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

@pytest.mark.asyncio
async def test_delete_user(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    admin = AdminPage(page)

    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    await login.login("Admin", "admin123")
    await dashboard.go_to_admin()

    await admin.delete_user("testuser1")
    user_still_exists = await admin.search_user("testuser1")
    assert not user_still_exists, "User 'testuser1' should be deleted"
