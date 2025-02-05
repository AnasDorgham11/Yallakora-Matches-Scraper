# Yallakora-Matches-Scraper
This Python script allows you to scrape match data from Yallakora, a website that provides match scores, including details like competition title, round, and match time in Arabic language. When running the script, you’ll be prompted to enter a specific date, and it will fetch and display all the match data for that day. This is perfect for quickly gathering up-to-date match information from Yallakora in a structured format.

## Setup Instructions:

1. **Clone the Repository** <br />
   First, clone the repository to your local machine:
   ```bash
   git clone git@github.com:AnasDorgham11/Yallakora-Matches-Scraper.git
   cd Yallakora-Matches-Scraper
   ```
      <br />
2. **<mark>Optional:</mark> Create a Virtual Environment** <br />
   It's recommended to use a virtual environment to avoid conflicts with existing Python libraries or versions you may have installed globally. To create and activate a virtual environment, follow these steps:
- **<div style="display: flex; align-items: bottom;"><span>Linux/macOS </span><a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=linux&theme=light" alt="linux" width="20px" height="20px" style="position: relative; top: -10px;"/></a> :</div>** 
   ```
   python3 -m venv venv          # Create virtual environment
   source venv/bin/activate      # Activate virtual environment
   ```


- **<div style="display: flex; align-items: bottom;"><span>Windows </span><a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=windows&theme=light" alt="Windows" width="20px" height="20px" style="position: relative; top: -10px;"/></a> :</div>** 
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
     <br />
3. **Install Dependencies**<br />
   After activating the virtual environment, install the required libraries using the ```requirements.txt``` file:
   ```
   pip install -r requirements.txt
   ```

   If you encounter the error ```externally managed environment``` while trying to use ```pip install```, this is a common issue on Linux systems. You can resolve it by installing dependencies using your system package manager:
   ```
   sudo apt install -r requirements.txt
   ```

   <br />
4. **Run the Scraper**<br />
   Once the environment is set up and dependencies are installed, run the scraper to collect match data:
   ```
   python3 scraper.py
   ```

   <br />
5. **Find scraped matches**<br />
   You can find scraped matches in the folder "matches" which is created automatically after running the script and entering the date in the format ```MM/DD/YYYY``` where ```MM``` is the month, ```DD``` is the day and ```YYYY``` is the year.

   <br />
6. **<mark>Optional:</mark> Deactivate the Virtual Environment**<br />
   If you have activated the virtual environment as explained in step 2, when you're done, deactivate the virtual environment by running:
   ```deactivate```

   <br />
## Notes:
   - Scraped data are in Arabic.
   - Virtual Environment (venv) is optional but highly recommended. It helps avoid conflicts between different library versions that might already exist on your system.
   - Activating the virtual environment ensures that your project uses the correct dependencies, even if you already have other versions installed globally.
   - If you skip creating a virtual environment, make sure you're managing your dependencies manually to avoid version conflicts.
   - ```requirements.txt``` contains the libraries needed for the script.

