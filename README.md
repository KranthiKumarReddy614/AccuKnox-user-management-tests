# AccuKnox-user-management-tests


This project contains end-to-end automated tests for the **User Management** module in [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login). The tests are written using **Playwright (Python)** and follow the **Page Object Model (POM)** design pattern.

---

## 📦 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests

2. Create Virtual Environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\\Scripts\\activate

3. Install Dependencies
   pip install -r requirements.txt
   If you don't have requirements.txt, install manually:
   pip install playwright pytest
   playwright install

4. How to Run the Tests
    Run all test cases:
   pytest tests/

Run a specific test case:
pytest tests/test_add_user.py
Optional: Run with headed browser (to see the browser)
bash
Copy
Edit
pytest tests/ --headed

5. Test Structure
   pages/ – Contains all POM classes like login_page.py, dashboard_page.py, admin_page.py
   tests/ – Contains Playwright test cases using pytest
   utils/ – Contains test data (test_data.py)
   conftest.py – Pytest configuration with Playwright fixtures

6. Credentials for Test
   URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
   Username: Admin
   Password: admin123

7. Playwright Version Used
   This project uses Playwright for Python v1.42.0

8. To check your version, run:
    playwright --version

9. Notes
   All tests are asynchronous (async def) and use Playwright's async API.

   Make sure the employee name used in add_user (e.g., Paul Collings) exists in the OrangeHRM demo system.
