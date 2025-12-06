## Middleware Pattern (Chain of Responsibility)

What: Pass request through chain of handlers
Where:Request/response middleware stack.
Benefit: Add functionality without touching views
Pros: clean cross-cutting concerns (auth, compression, timing).
Cons: ordering pitfalls; debugging across the chain can be tricky.

### How it differs from a decorator

Scope: Middleware = global (every request); Decorator = per-view opt-in.

Timing: Middleware wraps the whole request/response cycle; Decorator wraps only that view call.

Control: Middleware can block before a view is chosen and modify any response; Decorator only affects the decorated view’s response.

Composition: Middleware ordering is managed in settings; Decorators are stacked on the function/class.

### Rule of thumb:

Use middleware for policies that should apply to (almost) every request.

Use decorators for behavior needed by specific endpoints only.

```py
# Request goes through each middleware
Request → SecurityMiddleware → SessionMiddleware → AuthMiddleware →  View

# Each can modify or stop the request
class CustomMiddleware:
    def __call__(self, request):
        # Do something before view
        response = self.get_response(request)
        # Do something after view
        return response
```

```py
# myproject/middleware.py
import time
class TimingMiddleware:
    def __init__(self, get_response): self.get_response = get_response
    def __call__(self, request):
        start = time.monotonic()
        resp = self.get_response(request)
        resp["X-Elapsed"] = f"{time.monotonic() - start:.3f}s"
        return resp
```
