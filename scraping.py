# import module 
import requests 
from bs4 import BeautifulSoup 
import json
import csv
  
HEADERS = ({'User-Agent': 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
            'Accept-Language': 'en-US, en;q=0.5'}) 
  
# user define function 
# Scrape the data 
def getdata(url): 
    r = requests.get(url, headers=HEADERS) 
    return r.text 
  
  
def html_code(url): 
  
    # pass the url 
    # into getdata function 
    htmldata = getdata(url) 
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code 
    return (soup) 
  
  
url = "https://www.flipkart.com/bruton-combo-pack-2-sports-shoes-running-men/product-reviews/itm29d7821ff5155?pid=SHOGHK9QVFG9KNJV&lid=LSTSHOGHK9QVFG9KNJVDKMTH6&marketplace=FLIPKART"
  
soup = html_code(url) 
# print(soup) 


def cus_data(soup): 
    # find the Html tag 
    # with find() 
    # and convert into string 
    data_str = "" 
    cus_list = [] 
  
    for item in soup.find_all("p", class_="_2sc7ZR _2V5EHH _1QgsS5"): 
    # for item in soup.find_all("div", class_="_6K-7Co"): 
   
        data_str = data_str + item.get_text() 
        cus_list.append(data_str) 
        data_str = "" 
    return cus_list 


def cusi_data(soup): 
    # find the Html tag 
    # with find() 
    # and convert into string 
    data_str = "" 
    cus_list = [] 
  
    # for item in soup.find_all("p", class_="_2sc7ZR _2V5EHH _1QgsS5"): 
    for item in soup.find_all("div", class_="_6K-7Co"): 
   
        data_str = data_str + item.get_text() 
        cus_list.append(data_str) 
        data_str = "" 
    return cus_list 

  

cus_r = cusi_data(soup)
cus_res = cus_data(soup) 
print(cus_res) 
print(cus_r)

customer = {}

for key, value in zip(cus_res,cus_r):
    customer[key] = value


print(customer)

# json_data = json.dumps(customer, indent=2)
# print(json_data)


# import pandas as pd

# def dict_to_excel(input_dict, excel_file):
#     # Create a DataFrame from the dictionary
#     df = pd.DataFrame(list(input_dict.items()), columns=['Key', 'Value'])

#     # Write the DataFrame to an Excel file
#     df.to_excel(excel_file, index=False)

#     print(f'Excel file "{excel_file}" created successfully.')

# # Example usage:

# output_excel_file = 'output.xlsx'

# # Call the function
# dict_to_excel(customer, output_excel_file)












# def cus_rev(soup): 
#     # find the Html tag 
#     # with find() 
#     # and convert into string 
#     data_str = "" 
    
#     for item in soup.find_all("p", class_ = "_6K-7Co"): 
#         data_str = data_str + item.get_text() 
  
#     result = data_str.split("\n") 
#     return (result) 
  
  
# rev_data = cus_rev(soup) 
# rev_result = [] 
# for i in rev_data: 
#     if i == "": 
#         pass
#     else: 
#         rev_result.append(i) 
# rev_result 