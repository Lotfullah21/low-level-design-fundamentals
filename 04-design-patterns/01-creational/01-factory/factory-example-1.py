from abc import ABC, abstractmethod

# Products: Different document types
class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self):
        pass

class PDFDocument(Document):
    def open(self):
        print("Opening PDF document")
    
    def save(self):
        print("Saving PDF document")

class WordDocument(Document):
    def open(self):
        print("Opening Word document")
    
    def save(self):
        print("Saving Word document")

# (Factory) - Creator: Application
class Application(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        """Factory method - creates documents"""
        pass
    
    def new_document(self):
        """Uses the factory method"""
        doc = self.create_document()
        doc.open()
        doc.save()

# Concrete Creators: Specific applications
class PDFApplication(Application):
    def create_document(self) -> Document:
        return PDFDocument()

class WordApplication(Application):
    def create_document(self) -> Document:
        return WordDocument()

# Usage
pdf_app = PDFApplication()
pdf_app.new_document()
# Output: Opening PDF document

# word_app = WordApplication()
# word_app.new_document()
# # Output: Opening Word document