from django.http import HttpResponse

def cars_view(request):
    html = '''
            <html>
                <head>
                    <title>My Cars</title>
                </head>
                <body>
                    <h1>Cars of Junior</>
                    <h3> The best cars!</h3> 
                </body>
            </html>
    '''
    return HttpResponse(html) 
