# Yallakora-Matches-Scraper
A Python script to scrape matches data (score, competition title, round, time, etc.) from Yallakora for a specific date.

# Yallakora Matches Scraper

This Python project scrapes match data from Yallakora, providing details like competition title, round, and match time for a specific date. The project allows you to easily gather match information from the site with just a few simple commands.

## Setup Instructions:

1. **Clone the Repository**
   First, clone the repository to your local machine:
   ```bash
   git clone git@github.com:AnasDorgham11/Yallakora-Matches-Scraper/.git
   cd repository-name
  
2. **Optional: Create a Virtual Environment** 
   It's recommended to use a virtual environment to avoid conflicts with existing Python libraries or versions you may have installed globally. To create and activate a virtual environment, follow these steps:
  - Linux/macOS:
   ```
   python3 -m venv venv      # Create virtual environment
   source venv/bin/activate   # Activate virtual environment
   ```
  - Windows:
    - Command Prompt (CMD):
    ```
    python -m venv venv       # Create virtual environment
    venv\Scripts\activate     # Activate virtual environment
    ```
   - PowerShell:
    ```
    python -m venv venv       # Create virtual environment
    .\venv\Scripts\Activate.ps1  # Activate virtual environment
    ```

3. **Install Dependencies**
After activating the virtual environment, install the required libraries using the ```requirements.txt``` file:
```
pip install -r requirements.txt
```

If you encounter the error externally managed environment while trying to use pip install, this is a common issue on Linux systems. You can resolve it by installing dependencies using your system package manager:
```
sudo apt install -r requirements.txt
```
