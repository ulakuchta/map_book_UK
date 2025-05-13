from utils.model import users
from utils.controler import get_user_info, add_user, remove_user, update_user, get_map


def main():
    print('=============MENU===========')
    print('0 - zakończ program')
    print('1 - wyświetl co u znajomych')
    print('2 - dodaj znajomego')
    print('3 - usuń znajomego')
    print('4 - zaktualizuj dane znajomego')
    print('5 - Wygeneruj mapę znajomych')
    print('============================')
    while True:
        choice: str = input('Wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_map(users)


if __name__ == '__main__':
    main()
def get_coordinates(city_name:str)->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(url).text
    response_html = BeautifulSoup(response, "html.parser")
    longitude=float(response_html.select(".longitude")[1].text.replace(",","."))
    latitude=float(response_html.select(".latitude")[1].text.replace(",","."))
    print(longitude)
    print(latitude)
    return [latitude, longitude]

def get_map(user_data:list)->None:
    import folium
    m = folium.Map(location=(52.23, 21.0), zoom_start=6)
    for user in users:
        folium.Marker(location=get_coordinates(user['location']),popup='<img src="https://geoforum.pl/upload3/news_pl/picture/328_geodeta_artykul6.jpg"/>').add_to(m)
    m.save('index.html')
