import os
import json

def get_film_file_path(f_path: str = None) -> str:
    if f_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        f_path = os.path.join(base_path, 'films.json')
    return f_path

def read_films_from_file(f_path: str) -> list:
    with open(f_path, 'r') as file:
        try:
            data = json.load(file)
            return data.get('films', [])
        except json.JSONDecodeError:
            return []

def write_films_to_file(films: list, f_path: str) -> None:
    with open(f_path, 'w') as file:
        json.dump({'films': films}, file, indent=4)

def get_films(f_path: str = None) -> list:
    f_path = get_film_file_path(f_path)
    return read_films_from_file(f_path)

def get_film(id: int = 0, f_path: str = None) -> dict:
    films = get_films(f_path)
    if 0 <= id < len(films):
        return films[id]
    return {}

def save_film(film: dict, f_path: str = None) -> bool:
    f_path = get_film_file_path(f_path)
    films = get_films(f_path)
    films.append(film)
    write_films_to_file(films, f_path)
    return True

def find_film_by_title(title: str, f_path: str = None) -> dict:
    films = get_films(f_path)
    for film in films:
        if title.lower() in film.get('title', '').lower():
            return film
    return {}

def find_films_by_partial_title(partial_title: str, f_path: str = None) -> list:
    films = get_films(f_path)
    matched_films = [film for film in films if partial_title.lower() in film.get('title', '').lower()]
    return matched_films

def delete_film(title: str, f_path: str = None) -> bool:
    f_path = get_film_file_path(f_path)
    films = get_films(f_path)
    film_to_delete = None

    for film in films:
        if film.get('title') == title:
            film_to_delete = film
            break

    if film_to_delete:
        films.remove(film_to_delete)
        write_films_to_file(films, f_path)
        return True
    return False

def update_film(title: str, updated_film: dict, f_path: str = None) -> bool:
    f_path = get_film_file_path(f_path)
    films = get_films(f_path)
    film_to_update = None

    for index, film in enumerate(films):
        if film.get('title') == title:
            film_to_update = index
            break

    if film_to_update is not None:
        films[film_to_update] = updated_film
        write_films_to_file(films, f_path)
        return True
    return False