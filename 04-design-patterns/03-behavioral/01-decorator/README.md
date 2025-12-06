## Decorator

Add behavior to functions without modifying them

Where in Django: Where: Authentication, logging, permissions

@login_required, @csrf_exempt, @cache_page.

Benefit: Reusable, clean separation

Cons: stack can be hard to trace; order matters.

```py
# Without Decorator
def my_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    # actual logic...

# With Decorator
@login_required
def my_view(request):
    # actual logic only
    pass
```
