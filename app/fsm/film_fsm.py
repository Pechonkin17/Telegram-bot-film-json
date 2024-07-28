from aiogram.fsm.state import State, StatesGroup


class FilmCreateUpdateForm(StatesGroup):
    title = State()
    desc = State()
    url = State()
    photo = State()
    rating = State()

class FilmDeleteForm(StatesGroup):
    title = State()

class FilmFindForm(StatesGroup):
    title = State()

class FilmUpdateForm(StatesGroup):
    title = State()