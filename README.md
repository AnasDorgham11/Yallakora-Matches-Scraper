# Yallakora-Matches-Scraper
This Python script allows you to scrape match data from Yallakora, a website that provides match scores, including details like competition title, round, and match time in Arabic language. When running the script, you’ll be prompted to enter a specific date, and it will fetch and display all the match data for that day. This is perfect for quickly gathering up-to-date match information from Yallakora in a structured format.

## Setup Instructions:

1. ###Clone the Repository
   First, clone the repository to your local machine:
   ```bash
   git clone git@github.com:AnasDorgham11/Yallakora-Matches-Scraper/.git
   cd Yallakora-Matches-Scraper
  
2. **<mark>Optional:</mark> Create a Virtual Environment** 
   It's recommended to use a virtual environment to avoid conflicts with existing Python libraries or versions you may have installed globally. To create and activate a virtual environment, follow these steps:
- **Linux/macOS:**
   ```
   python3 -m venv venv          # Create virtual environment
   source venv/bin/activate      # Activate virtual environment
   ```
- **Windows <span> <a href="https://skillicons.dev"> <img src="https://skillicons.dev/icons?i=windows&theme=light" alt="Windows" width="30px" height="30px" style="vertical-align: bottom;" /> </a> </span> :** 
    - Command Prompt (CMD):
    ```
    python -m venv venv          # Create virtual environment
    venv\Scripts\activate        # Activate virtual environment
    ```
    - PowerShell:
    ```
    python -m venv venv          # Create virtual environment
    .\venv\Scripts\Activate.ps1  # Activate virtual environment
    ```

3. **Install Dependencies**
   After activating the virtual environment, install the required libraries using the ```requirements.txt``` file:
   ```
   pip install -r requirements.txt
   ```

   If you encounter the error ```externally managed environment``` while trying to use ```pip install```, this is a common issue on Linux systems. You can resolve it by installing dependencies using your system package manager:
   ```
   sudo apt install -r requirements.txt
   ```
4. **Run the Scraper**
   Once the environment is set up and dependencies are installed, run the scraper to collect match data:
   ```
   python3 scraper.py
   ```
5. **Find scraped matches**
   You can find scraped matches in the folder "matches" which is created automatically after running the script and entering the date in the format ```M/D/Y``` where ```M``` is the month, ```D``` is the day and ```Y``` is thre year where       each one could be in multiple digits if required like the format "MM/DD/YYYY".
    
6. **<mark>Optional:</mark> Deactivating the Virtual Environment**
   If you have activated it as explained in step 2, when you're done, deactivate the virtual environment, if you have activated it as in step 2, by running:
   ```deactivate```

## Notes:
   - Scraped data are in Arabic.
   - Virtual Environment (venv) is optional but highly recommended. It helps avoid conflicts between different library versions that might already exist on your system.
   - Activating the virtual environment ensures that your project uses the correct dependencies, even if you already have other versions installed globally.
   - If you skip creating a virtual environment, make sure you're managing your dependencies manually to avoid version conflicts.
   - ```requirements.txt``` contains the libraries needed for the script.

