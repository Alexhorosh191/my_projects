try:
    L = int(input("Введите длину балки "))
    if L >= 1:
        pass
    else:
        raise ValueError()

    number_fix = int(input('Введите количество закреплений балки (1 - если имеется одна жесткая заделка, 2 - если '
                           'имеется одно одностепенное и одно двухстепенное закрепление ) '))
    if 1 <= number_fix < 3:
        pass
    else:
        raise ValueError

    if number_fix == 2:
        list_arm_fix = [int(item) for item in input('Введите смещения для каждого крепления '
                                                    '(0 - начало балки) ').split()]
        if len(list_arm_fix) != number_fix:
            raise ValueError()
        for item in list_arm_fix:
            if 0 <= item <= L and sum(list_arm_fix)/len(list_arm_fix) != item:
                pass
            else:
                raise ValueError()

        list_dir_fix = [int(item) for item in input('Введите расположение для каждого крепления (0 - сверху балки, '
                                                    '1 - снизу балки) ').split()]
        if len(list_dir_fix) != number_fix:
            raise ValueError()
        for item in list_dir_fix:
            if 0 <= item <= 1:
                pass
            else:
                raise ValueError()

    elif number_fix == 1:
        list_arm_fix = [int(item) for item in input('Введите смещение для жесткой заделки (0 - начало балки или '
                                                    'величина длины балки - конец балки) ').split()]
        if len(list_arm_fix) != number_fix:
            raise ValueError()
        for item in list_arm_fix:
            if item == L or item == 0:
                pass
            else:
                raise ValueError()

    number_power = int(input('Введите количество приложенных сил '))
    if number_power >= 0:
        pass
    else:
        raise ValueError

    if number_power >= 1:
        list_dir_power = [int(item) for item in input('Введите направление для каждой силы (0 - сила приложена вниз, '
                                                      '1 - сила приложена вверх) ').split()]
        if len(list_dir_power) != number_power:
            raise ValueError()
        for item in list_dir_power:
            if 0 <= item <= 1:
                pass
            else:
                raise ValueError()

        list_power_power = [int(item) for item in input('Введите величины для каждой силы ').split()]
        if len(list_power_power) != number_power:
            raise ValueError()
        for item in list_power_power:
            if 0 < item:
                pass
            else:
                raise ValueError()

        list_arm_power = [int(item) for item in input('Введите смещения для каждой силы (0 - начало балки) ').split()]
        if len(list_arm_power) != number_power:
            raise ValueError()
        for item in list_arm_power:
            if 0 <= item <= L:
                pass
            else:
                raise ValueError()

    number_moment = int(input('Введите количество приложенных моментов '))
    if number_moment >= 0:
        pass
    else:
        raise ValueError

    if number_moment >= 1:
        list_dir_moment = [int(item) for item in input('Введите направление для каждого момента '
                                                       '(0 - по часовой стрелки, 1 - против часовой стрелки) ').split()]
        if len(list_dir_moment) != number_moment:
            raise ValueError()
        for item in list_dir_moment:
            if 0 <= item <= 1:
                pass
            else:
                raise ValueError()

        list_power_moment = [int(item) for item in input('Введите величины для каждого момента ').split()]
        if len(list_power_moment) != number_moment:
            raise ValueError()
        for item in list_power_moment:
            if 0 < item:
                pass
            else:
                raise ValueError()

        list_arm_moment = [int(item) for item in input('Введите смещения для каждого момента '
                                                       '(0 - начало балки) ').split()]
        if len(list_arm_moment) != number_moment:
            raise ValueError()
        for item in list_arm_moment:
            if 0 <= item <= L:
                pass
            else:
                raise ValueError()

    number_disload = int(input('Введите количество распределенных нагрузок '))
    if number_disload >= 0:
        pass
    else:
        raise ValueError

    if number_disload >= 1:
        list_dir_disload = [int(item) for item in input('Введите направление для каждой распределенной нагрузки '
                                                        '(0 - нагрузка направлена вниз, '
                                                        '1 - нагрузка направлена вверх) ').split()]
        if len(list_dir_disload) != number_disload:
            raise ValueError()
        for item in list_dir_disload:
            if 0 <= item <= 1:
                pass
            else:
                raise ValueError()

        list_power_disload = [int(item) for item in input('Введите величины для каждой распределенной '
                                                          'нагрузки ').split()]
        if len(list_power_disload) != number_disload:
            raise ValueError()
        for item in list_power_disload:
            if 0 < item:
                pass
            else:
                raise ValueError()

        list_arm_disload = []
        for i in range(number_disload):
            list_arm_disload.append([int(item) for item in input('Введите смещения для каждой распределенной нагрузки '
                                                                 '(от 0 - начало балки до '
                                                                 'L - величина длины балки(конец балки)) ').split()])
        if len(list_arm_disload) != number_disload:
            raise ValueError()

        for item in list_arm_disload:
            if len(item) == 2:
                pass
            else:
                raise ValueError()
            for i in item:
                if 0 <= i <= L and sum(item) / len(item) != i:
                    pass
                else:
                    raise ValueError
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
    exit()

if number_fix == 2:
    start_point = min(list_arm_fix)    # точка А
    last_point = max(list_arm_fix)     # точка Б
    first_power = 0                    # первое искомое значение реакции Yb
    second_power = 0                   # второе искомое значение реакции Ya

    # вычисляем силы
    for i_dir, i_arm, i_power in zip(list_dir_power, list_arm_power, list_power_power):
        if i_arm > start_point and i_dir == 0:      # сила приложена вниз и справа от точки
            first_power += i_power * (i_arm - start_point)
        elif i_arm > start_point and i_dir == 1:    # сила приложена вверх и справа от точки
            first_power -= i_power * (i_arm - start_point)
        elif i_arm < start_point and i_dir == 0:    # сила приложена вниз и слева от точки
            first_power -= i_power * (start_point - i_arm)
        elif i_arm < start_point and i_dir == 1:    # сила приложена вверх и слева от точки
            first_power += i_power * (start_point - i_arm)

    # вычисляем моменты
    for i_dir, i_power in zip(list_dir_moment, list_power_moment):
        if i_dir == 0:      # момент по часовой стрелки
            first_power += i_power
        elif i_dir == 1:    # момент против часовой стрелки
            first_power -= i_power

    # вычисляем распределенные нагрузки
    for i_dir, i_arm, i_power in zip(list_dir_disload, list_arm_disload, list_power_disload):
        if sum(i_arm) / 2 > start_point and i_dir == 0:    # сила приложена вниз и справа от точки
            first_power += i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))
        elif sum(i_arm) / 2 > start_point and i_dir == 1:  # сила приложена вверх и справа от точки
            first_power -= i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))
        elif sum(i_arm) / 2 < start_point and i_dir == 0:  # сила приложена вниз и слева от точки
            first_power -= i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))
        elif sum(i_arm) / 2 < start_point and i_dir == 1:  # сила приложена вверх и слева от точки
            first_power += i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))

    first_power /= (last_point - start_point)

    for i_arm, i_dir in zip(list_arm_fix, list_dir_fix):
        if i_arm == max(list_arm_fix) and i_dir == 1:
            first_power = first_power
        elif i_arm == max(list_arm_fix) and i_dir == 0:
            first_power = -first_power

    # на данной строке вычислили значение реакций в точке В

    # вычисляем силы
    for i_power, i_dir in zip(list_power_power, list_dir_power):
        if i_dir == 1:
            second_power -= i_power
        elif i_dir == 0:
            second_power += i_power

    # вычисляем распределенные нагрузки
    for i_power, i_dir, i_arm in zip(list_power_disload, list_dir_disload, list_arm_disload):
        if i_dir == 1:
            second_power -= i_power * (max(i_arm) - min(i_arm))
        elif i_dir == 0:
            second_power += i_power * (max(i_arm) - min(i_arm))

    second_power -= first_power

    for i_arm, i_dir in zip(list_arm_fix, list_dir_fix):
        if i_arm == min(list_arm_fix) and i_dir == 1:
            first_power = first_power
        elif i_arm == min(list_arm_fix) and i_dir == 0:
            first_power = -first_power

    # на данной строке вычислили значение реакций в точке А

    print('Значение реакций в точке А, Ya =', second_power)
    print('Значение реакций в точке B, Yb =', first_power)


if number_fix == 1:
    start_point = min(list_arm_fix)  # точка А
    first_power = 0                  # искомое значение реакции Ya
    first_moment = 0                 # искомое значение момента Ma

    # вычисляем силы
    for i_power, i_dir in zip(list_power_power, list_dir_power):
        if i_dir == 1:
            first_power -= i_power
        elif i_dir == 0:
            first_power += i_power

    # вычисляем распределенные нагрузки
    for i_power, i_dir, i_arm in zip(list_power_disload, list_dir_disload, list_arm_disload):
        if i_dir == 1:
            first_power -= i_power * (max(i_arm) - min(i_arm))
        elif i_dir == 0:
            first_power += i_power * (max(i_arm) - min(i_arm))

    # меняем знак если величины реакций оказались отрицательными
    if first_power < 0:
        first_power *= -1

    # на данной строке вычислили значение реакций в точке А

    # вычисляем силы
    for i_dir, i_arm, i_power in zip(list_dir_power, list_arm_power, list_power_power):
        if i_arm > start_point and i_dir == 0:  # сила приложена вниз и справа от точки
            first_moment += i_power * (i_arm - start_point)
        elif i_arm > start_point and i_dir == 1:  # сила приложена вверх и справа от точки
            first_moment -= i_power * (i_arm - start_point)
        elif i_arm < start_point and i_dir == 0:  # сила приложена вниз и слева от точки
            first_moment -= i_power * (start_point - i_arm)
        elif i_arm < start_point and i_dir == 1:  # сила приложена вверх и слева от точки
            first_moment += i_power * (start_point - i_arm)

    # вычисляем моменты
    for i_dir, i_power in zip(list_dir_moment, list_power_moment):
        if i_dir == 0:  # момент по часовой стрелки
            first_moment += i_power
        elif i_dir == 1:  # момент против часовой стрелки
            first_moment -= i_power

    # вычисляем распределенные нагрузки
    for i_dir, i_arm, i_power in zip(list_dir_disload, list_arm_disload, list_power_disload):
        if sum(i_arm) / 2 > start_point and i_dir == 0:  # сила приложена вниз и справа от точки
            first_moment += i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))
        elif sum(i_arm) / 2 > start_point and i_dir == 1:  # сила приложена вверх и справа от точки
            first_moment -= i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))
        elif sum(i_arm) / 2 < start_point and i_dir == 0:  # сила приложена вниз и слева от точки
            first_moment -= i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))
        elif sum(i_arm) / 2 < start_point and i_dir == 1:  # сила приложена вверх и слева от точки
            first_moment += i_power * (sum(i_arm) / 2 - start_point) * (max(i_arm) - min(i_arm))

    # меняем знак если величины реакций оказались отрицательными
    if first_moment < 0:
        first_moment *= -1

    # на данной строке вычислили значение момента в точке А

    print('Значение реакций в точке А, Ya =', first_power)
    print('Значение момента в точке А, Ma =', first_moment)






