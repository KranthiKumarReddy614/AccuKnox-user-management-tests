# pages/dashboard_page.py

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")

    async def go_to_admin(self):
        """Navigates from Dashboard to Admin Module."""
        await self.admin_menu.click()
    async def go_to_pim(self):
        await self.page.get_by_role("link", name="PIM").click()

    async def go_to_dashboard(self):
        await self.page.get_by_role("link", name="Dashboard").click()
