Реализовать автотест для github.com, который заходит на страницу, ищет кнопку Sign In, и нажимает на нее (авторизоваться не нужно);
Параметризовать тест различным размером окна браузера;
Обратить внимание, что для мобильной версии сайта потребуется другой автотест из-за изменения структуры локаторов;
Сделайть два варианта пропуска неподходящих параметров и тестов.

Три варианта тестов:
1. Пропустить мобильный тест, если соотношение сторон десктопное (и наоборот);
2. Переопределить параметр с помощью indirect;
3. Сделать разные фикстуры для каждого теста.
