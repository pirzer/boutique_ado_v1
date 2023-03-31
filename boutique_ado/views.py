from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

# added 404 - all this file views py
# added 404 - templates/errors/404.html
# added 404 - urls.py line 1, 32, 33


