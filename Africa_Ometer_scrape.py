#import request module and request the site's server for content
import requests
from requests import get
url = 'https://www.worldometers.info/coronavirus/'
response = get(url)
print(response.text[:500])

#import beautiful soup to parse the site by html elements
from bs4 import BeautifulSoup
html_soup =BeautifulSoup(response.text, 'html.parser')
type(html_soup)

 
import re



#make each countries data an item in a list
country_containers = html_soup.find_all('tr')
#print(type(country_containers))
#print(len(country_containers))

#row titles(last 3 items is one)
print(country_containers[0].text.split())
#get all the countries in africa in a list
africa_country_list = open("africa_countries.txt").read().splitlines() 
african_list = []
#print(africa_country_list)

#for each country data, put the text in a list and if the data is for an African country, print it

for i in range(len(country_containers)):
    country = country_containers[i]
    cc_no_space_1 = str(country_containers[i]).replace("> ", ">N/A")
    cc_no_space_2 = cc_no_space_1 .replace("><", ">N/A<")
    #the weird characters in re.sub are a regular expression that specifies to remove all things between <>
    country_info = re.sub('<[^>]+>', '', cc_no_space_2)
    country_info_list_i = country_info.split()
    index_num = i
    for i in africa_country_list:
        if(i==country_info_list_i[0]): 
            print("Overall country index number: " + str(index_num) + "-" + str(country_info_list_i))
            african_list.append(country_info_list_i)
    
print(african_list)
print(len(african_list))
#ex. get country from african country list and then specific data from country data list(first index number is for african country list, second is for specific data list)
print(african_list[0][0])

#make files for each piece of data; try for each country in african list, for each item in country, write file for item
for i in range(len(african_list)):
    for q in range(len(african_list[i])):
        if q == 0:
            file = open("country_name" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 1:
            file = open("total_cases" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 2:
            file = open("new_cases" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 3:
            file = open("total_deaths" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 4:
            file = open("new_deaths" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 5:
            file = open("total_recovered" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 6:
            file = open("active_cases" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 7:
            file = open("serious_critical" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()
        if q == 8:
            file = open("tot_cases_1m_pop" + str(i) + ".txt", "w+")
            file.write(str(african_list[i][q]))
            file.close()

        











