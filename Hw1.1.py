#Второй — без использования «Решета Эратосфена».
import cProfile

n = 100  # n- колличество значений, чтоб не использовать input


def Fib_search():
    a = []
    for i in range(n + 1):
        a.append(i)

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    i = 2
    while i <= n:
        j = i + 1
        if a[i] != 0:
            while j <= n:
                if (a[j] % a[i]) == 0:
                    a[j] = 0
                j += 1
        i += 1

    a = set(a)

    a.remove(0)


cProfile.run(Fib_search())
