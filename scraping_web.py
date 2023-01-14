import requests
from bs4 import BeautifulSoup
import time
def format_name(s):
    s = str(s)
    ls  = s.split(' ')
    name = ''
    # print(ls)
    for letter in ls:
        if letter == ''or  letter == ' ': continue
        letter = letter.replace(' ', '')
        name += letter + ' '
    return name
def check_skill(skill, skills_):
    for x in skills_:
        if x in skill:
            return False
    return True
## Input

print("Put some skill unfamiliar with: ")

ls_unskill = []
unfa_skill = input('> ')
while unfa_skill:
    ls_unskill.append(unfa_skill)
    unfa_skill = input('> ')


print('Filtering Out')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    # Convert Beautifull Soup

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        ## Get posted_date

        posted_date = job.find('span', class_="sim-posted").span.text

        if 'few' not in posted_date: continue
        ## Get company name  

        company_name = format_name(job.find('h3', class_= "joblist-comp-name").text)

        ## Get skill

        skill = format_name(job.find('span', class_="srp-skills").text)

        ## Get more info

        more_info = job.header.h2.a['href']
        if  check_skill(skill, ls_unskill):
            # print('-----------------------')
            # print(f'\nCompany name: {company_name.strip()} \nRequires Skill: {skill.strip()} \nTime post: {posted_date.strip()}\nMore Info: {more_info}')
            # Save in file 
            with open (f'Post/{index}.txt', 'w') as f:
                f.write(f'\nCompany name: {company_name.strip()} \nRequires Skill: {skill.strip()} \nTime post: {posted_date.strip()}\nMore Info: {more_info}')
                print(f'Save file {index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        print("Waiting 10 minius ...")
        time.sleep(600)