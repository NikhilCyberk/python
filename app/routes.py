from flask import request, jsonify
from app import app

books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'}
]
# home
@app.route('/')
def home():
    return 'Welcome to the book store!'

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    if type(request.json['title']) != str or type(request.json['author']) != str:
        return jsonify({'error': 'Title and author must be strings'}), 400
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(book)
    print(books)
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Not found'}), 404
    

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    if 'title' in request.json and type(request.json['title']) != str:
        return jsonify({'error': 'Title must be a string'}), 400
    if 'author' in request.json and type(request.json['author']) != str:
        return jsonify({'error': 'Author must be a string'}), 400

    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Not found'}), 404
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'result': True})
