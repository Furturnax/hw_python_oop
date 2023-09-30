from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE_ON_FINTES_TRACKER: str = ('Тип тренировки: {training_type}; '
                                      'Длительность: {duration:.3f} ч.; '
                                      'Дистанция: {distance:.3f} км; '
                                      'Ср. скорость: {speed:.3f} км/ч; '
                                      'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        """Вернуть информационное сообщение о конкретной тренировке."""
        return self.MESSAGE_ON_FINTES_TRACKER.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    SEC_IN_MIN: float = 60

    def __init__(self,
                 action: float,
                 duration: float,
                 weight: float) -> None:
        self.action: float = action
        self.duration: float = duration
        self.duration_minutes: float = duration * self.SEC_IN_MIN
        self.weight: float = weight

    def get_distance(self) -> float:
        """Получить и вернуть дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить и вернуть среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Метод переопределен в %s'
                                  % type(self).__name__)

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: float = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        """Вернуть количество затраченных калорий."""
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                / self.M_IN_KM * (self.duration * self.SEC_IN_MIN))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    CALORIES_WEIGHT_SHIFT: float = 0.029
    KM_HOUR_TO_METR_SEC: float = round(Training.M_IN_KM
                                       / (Training.SEC_IN_MIN * 60), 3)
    SM_IN_M: float = 100

    def __init__(self,
                 action: float,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height: float = height
        self.height_metre: float = height / self.SM_IN_M

    def get_spent_calories(self) -> float:
        """Вернуть количество затраченных калорий."""
        return ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight
                + ((self.get_mean_speed() * self.KM_HOUR_TO_METR_SEC) ** 2
                 / self.height_metre) * self.CALORIES_WEIGHT_SHIFT
                * self.weight) * self.duration_minutes)


class Swimming(Training):
    """Тренировка: плавание."""

    CALORIES_MEAN_SPEED_SHIFT: float = 1.1
    CALORIES_MEAN_SPEED_MULTIPLIER: float = 2
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: float,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:
        """Вернуть среднюю скорость движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Вернуть количество затраченных калорий."""
        return ((self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight
                * self.duration)


TYPES_TRAINING: dict[str, type[Training]] = {
    'SWM': Swimming,
    'RUN': Running,
    'WLK': SportsWalking
}


def read_package(workout_type: str, data: list[int]) -> Training:
    """Возвращать данные полученные от датчиков."""
    if workout_type not in TYPES_TRAINING:
        raise ValueError('Неожиданный тип тренировки %c' % (workout_type))
    return TYPES_TRAINING[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages: list[tuple[str, list[int]]] = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        main(read_package(workout_type, data))
