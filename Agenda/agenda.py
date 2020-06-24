# -*- coding: utf-8 -*-


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add (self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete (self, name):
        for idx, contact in enumerate(self._contacts):

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Tele ono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')


def run():

     contact_book = ContactBook()

     while True:
         command = str(raw_input('''
            Que desea hacer?

            [a]ñadir
            [ac]tualizar
            [b]uscar
            [e]liminar
            [l]istar contactos
            [s]alir
        '''))

     if command == 'a':
         name = str(raw_input('Ingrese el nombre del contacto: '))
         phone = str(raw_input('Ingrese el numerp de celular: '))
         email = str(raw_input('Ingrese email de contacto: '))

         contact_book.add(name, phone, email)

     elif command == 'ac':
        print('actualizar contacto')

     elif command == 'b':
        print('buscar contacto')

     elif command == 'e':
         name = str(raw_input('Ingrese el nombre del contacto: '))

         contact_book.delete(name)

     elif command == 'l':

         contact_book.show_all()

     elif command == 's':
         sys.exit()

     else:

        print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()
