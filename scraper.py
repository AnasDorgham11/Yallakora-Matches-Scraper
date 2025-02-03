import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


date = input("Please, enter the date in the format MM/DD/YYYY: ")

URL = f'https://www.yallakora.com/match-center/?date={date}#'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")
cards = soup.css.select('div[class*="matchCard matchesList"]')

match_details = []

for card in cards:
    title_block = card.find_all("div", {"class" : "title"})
    for i in title_block:
        title = i.find('h2').text.strip()
        matches = card.find_all("div", {"class":"item finish liItem"})
        counter = 0
        for match in matches:
            match_round = match.find("div", {"class":"date"}).text.strip()
            
            team_A = match.find("div", {"class" : "teams teamA"}).text.strip()
            team_B = match.find("div", {"class" : "teams teamB"}).text.strip()
            
            result = match.find("div", {"class" : "MResult"})
            score = result.find_all("span", {"class":"score"})
            scoreA = score[0].text.strip()
            scoreB = score[1].text.strip()
            
            
            penalty = result.find("div", {"class" : "penaltyRes"})
            if penalty:
                penalty_res = penalty.find('span').text.strip().replace('(','').replace(')','')
                penalty_splitter = penalty_res.split(" - ")
                penaltyA = penalty_splitter[0]
                penaltyB = penalty_splitter[1]
            else:
                penaltyA = '_'
                penaltyB = '_'
            
            time = result.find("span", {"class":"time"}).text.strip()

            match_details.append({'Competition':title , 'Round':match_round, 'Team A':team_A, 'Score A': scoreA, 'Score B' : scoreB,'Team B':team_B, 'Penalty A': penaltyA, 'Penalty B': penaltyB, 'Time': time})
            counter += 1



df = pd.DataFrame(match_details, index = None)
df = df.rename(columns={"Competition":"البطولة", "Round": "الجولة/الدور", "Score A":"هدف أ", "Score B":"هدف ب","Penalty A":"ض.ج أ","Penalty B":"ض.ج ب","Team A":"فريق أ","Team B":"فريق ب","Time":"التوقيب"})
df.to_csv(f"matches/{date.replace('/','-')}_Matches.csv")