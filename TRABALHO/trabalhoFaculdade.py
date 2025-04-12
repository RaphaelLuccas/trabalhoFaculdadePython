#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Book:
    """Classe Model: representa um livro no sistema"""

    def __init__(self, title, author, year, id=None):
        """Inicializa um novo livro"""
        self.title = title
        self.author = author
        self.year = year
        self.id = id

    def __str__(self):
        """Retorna uma representação em string do livro"""
        return f"Livro: {self.title}, Autor: {self.author}, Ano: {self.year}, ID: {self.id}"


class View:
    """Classe View: responsável pela interface com o usuário"""

    def show_menu(self):
        """Exibe o menu principal"""
        print("\n===== SISTEMA DE CADASTRO DE LIVROS =====")
        print("1. Adicionar livro")
        print("2. Buscar livro por ID")
        print("3. Buscar livro por título")
        print("4. Listar todos os livros")
        print("5. Remover livro")
        print("0. Sair")
        return input("Escolha uma opção: ")

    def get_book_info(self):
        """Obtém informações para cadastrar um novo livro"""
        print("\n--- Cadastro de Livro ---")
        title = input("Título: ")
        author = input("Autor: ")
        year = input("Ano de publicação: ")
        return title, author, year

    def get_book_id(self):
        """Obtém o ID de um livro"""
        return input("\nInforme o ID do livro: ")

    def get_book_title(self):
        """Obtém o título de um livro"""
        return input("\nInforme o título do livro: ")

    def show_book(self, book):
        """Exibe informações de um livro"""
        if book:
            print(f"\n{book}")
        else:
            print("\nLivro não encontrado!")

    def show_books(self, books):
        """Exibe uma lista de livros"""
        if not books:
            print("\nNenhum livro cadastrado!")
            return

        print("\n--- Lista de Livros ---")
        for book in books:
            print(book)

    def show_message(self, message):
        """Exibe uma mensagem para o usuário"""
        print(f"\n{message}")


class Controller:
    """Classe Controller: gerencia as interações entre Model e View"""

    def __init__(self):
        """Inicializa o controlador"""
        self.view = View()
        self.books = {}  # Dicionário para armazenar os livros (id: book)
        self.next_id = 1  # Próximo ID disponível

    def run(self):
        """Inicia a execução do sistema"""
        while True:
            option = self.view.show_menu()

            if option == '1':
                self.add_book()
            elif option == '2':
                self.find_book_by_id()
            elif option == '3':
                self.find_book_by_title()
            elif option == '4':
                self.list_books()
            elif option == '5':
                self.remove_book()
            elif option == '0':
                self.view.show_message("Encerrando o sistema...")
                break
            else:
                self.view.show_message("Opção inválida!")

    def add_book(self):
        """Adiciona um novo livro ao sistema"""
        title, author, year = self.view.get_book_info()
        try:
            year = int(year)
            book = Book(title, author, year, self.next_id)
            self.books[self.next_id] = book
            self.next_id += 1
            self.view.show_message(f"Livro adicionado com sucesso! ID: {book.id}")
        except ValueError:
            self.view.show_message("Erro: Ano deve ser um número inteiro!")

    def find_book_by_id(self):
        """Busca um livro pelo ID"""
        id_str = self.view.get_book_id()
        try:
            book_id = int(id_str)
            book = self.books.get(book_id)
            self.view.show_book(book)
        except ValueError:
            self.view.show_message("Erro: ID deve ser um número inteiro!")

    def find_book_by_title(self):
        """Busca livros pelo título (pesquisa parcial)"""
        title = self.view.get_book_title().lower()
        found_books = [book for book in self.books.values()
                       if title in book.title.lower()]
        self.view.show_books(found_books)

    def list_books(self):
        """Lista todos os livros cadastrados"""
        self.view.show_books(list(self.books.values()))

    def remove_book(self):
        """Remove um livro do sistema"""
        id_str = self.view.get_book_id()
        try:
            book_id = int(id_str)
            if book_id in self.books:
                del self.books[book_id]
                self.view.show_message(f"Livro com ID {book_id} removido com sucesso!")
            else:
                self.view.show_message(f"Livro com ID {book_id} não encontrado!")
        except ValueError:
            self.view.show_message("Erro: ID deve ser um número inteiro!")


# Execução do programa
if __name__ == "__main__":
    controller = Controller()
    controller.run()
