import sys
import datetime
import requests as re
from bs4 import BeautifulSoup as bs


def requests_url(url, headers):
    flipkart_api = re.get(url, headers=headers)
    return flipkart_api


print(f"Program started : {datetime.datetime.now()}")
flipkart_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
flipkart_headers = {'content-type': 'text/html'}

get_api = requests_url(flipkart_url, flipkart_headers)

iPhone_model = []
iPhone_rating = []
iPhone_rating_count = []
iPhone_review = []
iPhone_original_price = []
iPhone_discount_price = []
try:
    if get_api.status_code == 200:
        print("API STATUS RESPONSE SUCCESSFUL")
    else:
        sys.exit()
except Exception as e:
    print(f"Error : {e}")

try:
    soup = bs(get_api.text, "html.parser")

    mobile_name_rating = soup.findAll(class_="col col-7-12")

    for details in mobile_name_rating:
        mobile_name = details.find_all(class_="_4rR01T")
        for name in mobile_name:
            name = name.text
            iPhone_model.append(name)
            # print(f"Mobile Name : {name}")

        mobile_rating = details.find_all(class_="gUuXy-")
        for rating in mobile_rating:
            rating = rating.find_all(class_="_1lRcqv")
            for rate in rating:
                rate = rate.text
                iPhone_rating.append(rate)
            # print(f"Mobile rating : {rate}")
        for rating in mobile_rating:
            rating_count = rating.find_all(class_="_2_R_DZ")
            for rate_count in rating_count:
                rate_count = rate_count.text
                iPhone_rating_count.append(rate_count)
            # print(f"Mobile rating count and reviews : {rate_count}")
    print("Extracted Mobile Name,Rating,Rating Count,Reviews")

    mobile_price_details = soup.findAll(class_="col col-5-12 nlI3QM")

    for price_details in mobile_price_details:
        discount_mobile_price = price_details.find_all(class_="_30jeq3 _1_WHN1")
        for discount_price in discount_mobile_price:
            discount_price = discount_price.text
            iPhone_discount_price.append(discount_price)
            # print(f"Mobile discount_price : {discount_price}")

        original_mobile_price = price_details.find_all(class_="_3I9_wc _27UcVY")
        for original_price in original_mobile_price:
            original_price = original_price.text
            iPhone_original_price.append(original_price)
            #print(f"Mobile original_price : {original_price}")
    print("Extracted Mobile Original Price and Discount Price ")
    print(f"Program Ended : {datetime.datetime.now()}")
except Exception as e:
    print(f"Error : {e}")
