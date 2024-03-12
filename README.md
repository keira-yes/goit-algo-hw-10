# Обчислення значення інтеграла функції методом Монте-Карло

У цьому дослідженні ми використовували **метод Монте-Карло** для обчислення визначеного інтеграла функції $$f(x) = x^2$$ на інтервалі від 0 до 2. Для порівняння отриманих результатів ми використали результат, отриманий за допомогою функції **quad** з бібліотеки SciPy, яка надає аналітичні обчислення інтегралів.

## Результати обчислень

-   Метод Монте-Карло:
    Значення інтеграла: 2.6683
-   Функція quad (SciPy):
    Значення інтеграла: 2.6667

## Висновки

Результати, отримані методом Монте-Карло, досить точно відповідають результатам, отриманим за допомогою функції quad з бібліотеки SciPy. Різниця між обчисленими значеннями дуже невелика, що підтверджує правильність і ефективність обчислень методом Монте-Карло для даного інтеграла.

Метод Монте-Карло дозволяє наблизитися до аналітичного розв'язку інтегралів з будь-якою точністю, збільшуючи кількість випадкових точок. Цей метод особливо корисний у випадках, коли аналітичні розв'язки складні або недоступні, або коли інтегрування в багатовимірних просторах ускладнюється.

Таким чином, можемо зробити висновок, що метод Монте-Карло ефективний і точний для обчислення визначених інтегралів і може бути використаний для широкого спектру обчислювальних задач.
