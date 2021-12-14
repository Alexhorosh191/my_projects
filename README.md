# Сonstruction mechanics: calculation for statically definable beams
# Строительная механика: расчет для статически определимых балок

**Ввод данных производится через input() (Где требуется ввести несколько значений, значения вводятся через пробел)**<br>
**Вывод данных через print()**<br><br>
### Пример работы программы:<br>

![Снимок](https://user-images.githubusercontent.com/84970248/144568401-7ed37993-4ede-4772-8872-344bbd929c9c.JPG)

### Пример ввода данных через консоль:<br>

Введите длину балки `10`<br>
Введите количество закреплений балки (1 - если имеется одна жесткая заделка, 2 - если имеется одно одностепенное и одно двухстепенное закрепление ) `2`<br>
Введите смещения для каждого крепления (0 - начало балки) `0 7`<br>
Введите расположение для каждого крепления (0 - сверху балки, 1 - снизу балки) `1 1`<br>
Введите количество приложенных сил `1`<br>
Введите направление для каждой силы (0 - сила приложена вниз, 1 - сила приложена вверх) `0`<br>
Введите величины для каждой силы `19`<br>
Введите смещения для каждой силы (0 - начало балки) `10`<br>
Введите количество приложенных моментов `1`<br>
Введите направление для каждого момента (0 - по часовой стрелки, 1 - против часовой стрелки) `1`<br>
Введите величины для каждого момента `15`<br>
Введите смещения для каждого момента (0 - начало балки) `10`<br>
Введите количество распределенных нагрузок `1`<br>
Введите направление для каждой распределенной нагрузки (0 - нагрузка направлена вниз, 1 - нагрузка направлена вверх) `0`<br>
Введите величины для каждой распределенной нагрузки `12`<br>
Введите смещения для каждой распределенной нагрузки (два числа через пробел, от 0 - начало балки до L - величина длины балки(конец балки)) `0 7`<br>

### Пример ответа:<br>

Значение реакций в точке А, Ya = `36.0`<br>
Значение реакций в точке B, Yb = `67.0`<br>




