import requests
import csv
from BeautifulSoup import BeautifulSoup

#diset html to see how to isolate the table, view source 

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2014&agency=931'

response = requests.get(url)

html = response.content

soup = BeautifulSoup(html) 
# print soup 
results_table = soup.find('table', attrs = {'id' : 'grdEmployees'})

output = []
# print results_table

for row in results_table.findAll('tr'):
	# print row
	output_row = [] #to put cleandata in later 

	for cell in row.findAll('td'):
		# print cell.text
		output_row.append(cell.text)

	output.append(output_row)
# # print output
# handle = open('Salaries.csv' , 'w') # write, read etc 
# outfile = csv.writer(handle) 
# outfile.writerows(output)
