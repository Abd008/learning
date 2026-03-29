from django.http import HttpResponse

def create_table_of_squares(request, s, n):
    result = ""
    for i in range(1, n+1):
        result += f"<p>{s} * {i} = {s*i}</p>"
    return HttpResponse(result)