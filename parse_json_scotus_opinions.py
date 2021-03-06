import csv, json, os, re
import pandas as pd
from bs4 import BeautifulSoup

DATA_PATH = ".\\data\\scotus_opinions\\"
INPUT_PATH = os.path.join(DATA_PATH,"json\\")
OUTPUT_PATH = os.path.join(DATA_PATH,"scotus_opinions.csv")

#get the US citation from the first two lines of the opinion text
#use regular expression with 1-3 decimal digits, followed by U.S.,
#followed by 1-3 decimal digits
US_CITE_RE = "\d{1,3} U.S. \d{1,3}"
def scrape_citation(opinion_text):
    first = re.findall(US_CITE_RE,opinion_text.split('\n')[0])
    second = re.findall(US_CITE_RE,opinion_text.split('\n')[1])
    if len(first) > 0:
        return first[0]
    elif len(second) > 0:
        return second[0]
    else:
        return None

#load json files and write to csv file
def json_opins_to_csv():
    data_dict = {'citation': [],'case_name': [],'date': [], 'opinion': []}

    #each json file contributes a row to the big csv file
    processed = 0
    total_files = 64_184
    for file in os.listdir(INPUT_PATH):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            with open(os.path.join(INPUT_PATH, filename),encoding='utf-8') as opinion_json:
                #load data from json
                json_data = json.load(opinion_json)

                #try getting CASE NAME, from absolute_url
                abs_url = str(json_data['absolute_url'])
                case_name = abs_url.split('/')[-2]

                #get date
                date = ""

                #retrieve opinion text from CourtListener data
                #opinion stored in one of three fields:
                opin_plain = str(json_data['plain_text'])
                opin_html = str(json_data['html'])
                opin_html_cite = str(json_data['html_with_citations'])

                if opin_html_cite != "":
                    soup = BeautifulSoup(opin_html_cite, 'html.parser')
                    #try getting citation
                    for tag in soup.find_all('p',class_='case_cite'):
                        citation = tag.text
                    #try getting date
                    for tag in soup.find_all('p',class_='date'):
                        date = tag.text
                    #try getting parties/case name
                    for tag in soup.find_all('p',class_='parties'):
                        case_name = tag.text
                    #get opinion text
                    opinion = soup.get_text().rstrip()
                elif opin_html != "":
                    soup = BeautifulSoup(opin_html, 'html.parser')
                    #try getting citation
                    for tag in soup.find_all('p',class_='case_cite'):
                        citation = tag.text
                    #try getting date
                    for tag in soup.find_all('p',class_='date'):
                        date = tag.text
                    #try getting parties/case name
                    for tag in soup.find_all('p',class_='parties'):
                        case_name = tag.text
                    #get opinion text
                    opinion = soup.get_text().rstrip()
                elif opin_plain != "":
                    opinion = opin_plain.rstrip()

                #get U.S. citation by scraping beginning of opinion text
                citation = scrape_citation(opinion)

                #write row to csv file
                data_dict['citation'].append(citation)
                data_dict['case_name'].append(case_name)
                data_dict['date'].append(date)
                data_dict['opinion'].append(opinion)

                #print status
                if opinion != "":
                    processed += 1
                per_complete = 100*round(processed/total_files,4)
                print(per_complete,"%")

                #for testing
                #if processed == 100: break

        else:
            continue

    #store data dictionary in pandas df
    opin_df = pd.DataFrame.from_dict(data=data_dict)

    #write dataframe to file
    opin_df.to_csv(OUTPUT_PATH, encoding='utf-8')

if __name__ == '__main__':
    json_opins_to_csv()
