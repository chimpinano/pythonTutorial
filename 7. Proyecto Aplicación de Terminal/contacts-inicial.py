# -*- coding: utf-8 -*-



def run():

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            print('añadir contacto')

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')

        elif command == 'l':
            print('listar contactos')

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
    