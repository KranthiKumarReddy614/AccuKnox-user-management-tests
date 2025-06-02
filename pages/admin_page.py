# pages/admin_page.py

class AdminPage:
    def __init__(self, page):
        self.page = page

    async def navigate_to_admin(self):
        """Navigate to the Admin module from any screen."""
        await self.page.get_by_role("link", name="Admin").click()
        await self.page.wait_for_selector("h6:has-text('System Users')")

    async def add_user(self, username, role, status, employee_name, password):
        """Add a new user with the given details."""
        await self.page.get_by_role("button", name="Add").click()
        await self.page.get_by_label("User Role").click()
        await self.page.get_by_role("option", name=role).click()

        await self.page.get_by_label("Status").click()
        await self.page.get_by_role("option", name=status).click()

        await self.page.get_by_placeholder("Type for hints...").fill(employee_name)
        await self.page.get_by_text(employee_name).click()

        await self.page.get_by_placeholder("Username").fill(username)
        await self.page.get_by_placeholder("Password").fill(password)
        await self.page.get_by_placeholder("Confirm Password").fill(password)

        await self.page.get_by_role("button", name="Save").click()
        await self.page.wait_for_timeout(2000)  # small wait to ensure save completes

    async def search_user(self, username):
        """Search for a user in the Admin table."""
        await self.page.get_by_label("Username").fill(username)
        await self.page.get_by_role("button", name="Search").click()
        await self.page.wait_for_timeout(2000)
        return await self.page.locator(f"text={username}").is_visible()

    async def edit_user(self, username, new_role=None, new_status=None):
        """Edit user details like role or status."""
        row_selector = f"//div[text()='{username}']/ancestor::div[contains(@class,'oxd-table-row')]"
        edit_button = self.page.locator(f"{row_selector}//button[1]")
        await edit_button.click()
        await self.page.wait_for_selector("h6:has-text('Edit User')")

        if new_role:
            await self.page.get_by_label("User Role").click()
            await self.page.get_by_role("option", name=new_role).click()

        if new_status:
            await self.page.get_by_label("Status").click()
            await self.page.get_by_role("option", name=new_status).click()

        await self.page.get_by_role("button", name="Save").click()
        await self.page.wait_for_timeout(2000)

    async def delete_user(self, username):
        """Delete a user by clicking the delete button and confirming."""
        row_selector = f"//div[text()='{username}']/ancestor::div[contains(@class,'oxd-table-row')]"
        delete_button = self.page.locator(f"{row_selector}//button[2]")
        await delete_button.click()

        await self.page.get_by_role("button", name="Yes, Delete").click()
        await self.page.wait_for_timeout(2000)

    async def validate_user_details(self, username, role=None, status=None):
        """Validate that user details like role and status match."""
        await self.search_user(username)
        row = self.page.locator(f"//div[text()='{username}']/ancestor::div[contains(@class,'oxd-table-row')]")

        match = True
        if role:
            match = match and await row.locator(f"div:has-text('{role}')").is_visible()
        if status:
            match = match and await row.locator(f"div:has-text('{status}')").is_visible()

        return match