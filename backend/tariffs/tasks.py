import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import Tariff

@shared_task
def scrape_operator_data():
    try:
        url = 'https://moscow.megafon.ru/tariffs/all/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Пример парсинга данных с проверкой наличия элементов
        title_tag = soup.find('div', {'class': 'tariffs-card-header-v4__title'})
        title = title_tag.text.strip() if title_tag else 'N/A'

        # Преобразование строки цены
        price_tag = soup.find('div', {'class': 'tariffs-card-buy-v4__price'})
        price_text = price_tag.text.strip(' ₽') if price_tag else '0'
        price = int(price_text.replace(' ', '')) if price_text else 0

        # Преобразование строки минут
        minutes_tag = soup.find('div', {'class': 'tariffs-card-additional-params-v4__value'}, text=lambda x: 'минут' in x)
        minutes_text = minutes_tag.text.strip(' минут') if minutes_tag else '0'
        minutes = int(minutes_text.replace(' ', '')) if minutes_text else 0

        # Преобразование строки гигабайтов
        gigabytes_tag = soup.find('div', {'class': 'tariffs-card-additional-params-v4__value'}, text=lambda x: 'ГБ' in x)
        gigabytes_text = gigabytes_tag.text.strip(' ГБ') if gigabytes_tag else '0'
        gigabytes = int(gigabytes_text.replace(' ', '')) if gigabytes_text else 0

        # Преобразование строки SMS
        sms_tag = soup.find('div', {'class': 'tariffs-card-additional-params-v4__value'}, text=lambda x: 'SMS' in x)
        sms_text = sms_tag.text.strip(' SMS') if sms_tag else '0'
        sms = int(sms_text.replace(' ', '')) if sms_text else 0

        head = 'Мегафон'
        operator = 'megafon'

        # Сохранение данных в базу
        Tariff.objects.create(
            name=title,
            price=price,
            minutes=minutes,
            gigabytes=gigabytes,
            sms=sms,
            operator=operator,
            head=head
        )
        print("Data scraped and saved successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")