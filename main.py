import utilitiesA as utilA
import utilitiesB as utilB

def main():
    a = 7
    b = 5

    c = utilA.sumaA(a, b)

    print(f"El valor de la suma de a y b es: {c}")


    d = utilB.restaB(a, b)
    print(f"El valor de la resta de a y b es: {d}")

    #================ Saludos
    print("Hola mundo desed A")
    print("Hola mundo somos el equipo AB")


if __name__ == "__main__":
    main()

