from library_system import Book, EBook, PrintBook

def test_book_initialization():
    b = Book("Test Book", "Author A")
    assert b.title == "Test Book", "Book title not initialized correctly"
    assert b.author == "Author A", "Book author not initialized correctly"
    print("Book class initialization passed ✅")

def test_ebook_initialization():
    e = EBook("Digital Book", "Author B", 123)
    assert e.title == "Digital Book", "EBook title not initialized correctly"
    assert e.author == "Author B", "EBook author not initialized correctly"
    assert e.file_size == 123, "EBook file_size not initialized correctly"
    print("EBook class initialization passed ✅")

def test_printbook_initialization():
    p = PrintBook("Printed Book", "Author C", 321)
    assert p.title == "Printed Book", "PrintBook title not initialized correctly"
    assert p.author == "Author C", "PrintBook author not initialized correctly"
    assert p.page_count == 321, "PrintBook page_count not initialized correctly"
    print("PrintBook class initialization passed ✅")

if __name__ == "__main__":
    test_book_initialization()
    test_ebook_initialization()
    test_printbook_initialization()
