import time


class User:
    """
    Класс пользователя, содержащий атрибуты: имя, пароль и возраст.
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    """
    Класс Видео, содержащий атрибуты: заголовок, время видео, начальное время, возрастное ограничение.
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = bool(adult_mode)

    def __str__(self):
        return self.title


class UrTube:
    """
    Класс УрбанТуб.
    Содержащий атрибуты: Пользователя, видео, текущего пользователя.
    Содержащий методы: Регистрация, выполнения входа, добавление видео, проверки видео в списке заголовка, поиск видео

    """
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    # Метод регистрации
    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = self.users[nickname]

    # Метод входа
    def log_in(self, nickname, password):
        if nickname in self.users and self.users[nickname].password == hash(password):
            self.current_user = self.users[nickname]
            print(f'{nickname}, Здравствуйте!')
        else:
            print(f'Пользователь {nickname}, не найден.')

    def log_out(self):
        self.current_user = None

    # Метод добавления видео
    def add(self, *args):
        for video in args:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
            else:
                print('Видео с таким заголовком уже существует.')

    # Метод проверки видео по заголовкам
    def get_videos(self, keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    # Метод проверки: авторизации текущего пользователя, поиска видео, ограничения возраста в видео.
    # Выполнение воспроизведения видео с отсчётом секунд.
    def watch_video(self, title):

        if self.current_user is None:
            print('Войдите в аккаунт, для просмотра видео.')
            return
        video = next((v for v in self.videos if v.title == title), None)

        if video is None:
            print('Видео не найдено.')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, покиньте страницу.')
            return

        print(f'Начинаем воспроизведение: {video.title}.')
        for second in range(video.duration):
            time.sleep(1)
            print(f'Секунда {second + 1}')
        print('Конец видео.')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
