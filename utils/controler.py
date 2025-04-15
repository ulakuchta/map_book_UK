def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.')


def add_user(users_data: list) -> None:
    new_name: str = input('Podaj imię nowego znajomego: ')
    new_location: str = input('Podaj lokalizację: ')
    new_posts: str = input('Podaj liczbę postów nowego znajomego: ')
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts}, )


def remove_user(users_data: list) -> None:
    user_name: str = input('Podaj imię znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)
