import requests
from bs4 import BeautifulSoup
response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    try:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})
        user_currency = input("Enter your currency \n 1(AUD), 2(AZN), \n 3(BYN), 4(BGN), \n 5(KRW), 6(HKD), \n"
                              " 7(DKK), 8(USD), \n 9(EUR), 10(EUR) \n")
        if user_currency == '1':
            res = soup_list[0]
            user_number = float(input("Enter digit in Australian dollar "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '2':
            res = soup_list[1]
            user_number = float(input("Enter digit in Azerbaijani manat "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '3':
            res = soup_list[2]
            user_number = float(input("Enter digit in Belarusian ruble "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '4':
            res = soup_list[3]
            user_number = float(input("Enter digit in Bulgarian lion "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '5':
            res = soup_list[4]
            user_number = float(input("Enter digit in KRW "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '6':
            res = soup_list[5]
            user_number = float(input("Enter digit in Hong Kong dollar "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '7':
            res = soup_list[6]
            user_number = float(input("Enter digit in Danish krone "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '8':
            res = soup_list[7]
            user_number = float(input("Enter digit in U.S. dollar "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '9':
            res = soup_list[8]
            user_number = float(input("Enter digit in Euro "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        elif user_currency == '10':
            res = soup_list[9]
            user_number = float(input("Enter digit in Egyptian pound "))
            print(round(float(res.text.replace(",", "."))) * user_number,"UAN")
        else:
            print("This currency is not in our list")
    except ValueError:
        print("You must enter digit ")
    except IndexError:
        print("IndexError")