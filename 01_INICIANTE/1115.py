while True:
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        break

    quadrantes = {
        (True, True): "primeiro",
        (False, True): "segundo",
        (False, False): "terceiro",
        (True, False): "quarto",
    }

    print(quadrantes[(x > 0, y > 0)])
