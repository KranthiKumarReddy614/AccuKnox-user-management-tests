import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from utils.test_data import test_user

@pytest.mark.asyncio
async def test_add_user(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    admin = AdminPage(page)

    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    await login.login("Admin", "admin123")
    await dashboard.go_to_admin()

    await admin.add_user(
        username=test_user["username"],
        role=test_user["role"],
        status=test_user["status"],
        employee_name=test_user["employee_name"],
        password=test_user["password"]
    )
