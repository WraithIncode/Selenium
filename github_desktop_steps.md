# How to Upload to GitHub using GitHub Desktop

Since you already have the files in `d:\Code\Python\Selenium`, follow these exact steps:

1.  **Open GitHub Desktop**.
2.  Go to the menu bar: **File** > **Add Local Repository...** (Ctrl+O).
3.  Click **Choose...** and select your folder: `d:\Code\Python\Selenium`.
4.  Click **Add Repository**.
5.  You will see a message saying: *"This directory does not appear to be a Git repository."*
    *   Click the blue text link that says **create a repository**.
6.  A **"Create a New Repository"** dialog will appear.
    *   **Name**: It should default to `Selenium`. You can change it to `selenium-keep-alive` if you prefer.
    *   **Local Path**: Ensure it says `d:\Code\Python` (so the full path is `d:\Code\Python\Selenium`).
    *   **Git Ignore**: Select **None** (We already created a `.gitignore` file manually).
    *   **License**: None.
    *   Click **Create Repository**.
7.  **Publish the Repository**:
    *   Click the blue **Publish repository** button in the top right corner.
    *   **Name**: `selenium-keep-alive` (This will be the name on GitHub).
    *   **Keep this code private**: **CHECK** this box (Keep it checked).
    *   **Organization**: None.
    *   Click **Publish Repository**.

## Final Step: Add the Secrets?
Actually, you **don't need to add Secrets** anymore because we updated the code to use `links.txt`!
*   The workflow will just read the links from the file in your private repo.
*   The `STREAMLIT_URL` secret is now optional.

**You are done!** The action will run automatically every 6 hours.
