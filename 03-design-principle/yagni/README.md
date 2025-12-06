## The Violation (Predicting the Future)

Imagine the client asks: "I need a function to upload a CSV file."
We think: "Maybe they will want JSON and XML later!"

```py
class FileUploader:
    def upload_csv(self, file):
        print("Uploading CSV...")

    # YAGNI Violation: Nobody asked for this yet!
    # Spent time writing, testing, and maintaining code that serves no purpose.
    def upload_json(self, file):
        print("Uploading JSON...")

    def upload_xml(self, file):
        print("Uploading XML...")
```

### The Solution (YAGNI)

Build exactly what is asked for. If they ask for JSON later, add it then.

```py
class FileUploader:
    def upload_csv(self, file):
        print("Uploading CSV...")
```
