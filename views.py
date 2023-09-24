from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html> 
    <head> 
        <meta cherset='UTF-8'>
        <meta name = "viewport" content="device-width, initial-scale=1.0">
        <title>FIRST DJANGO WEB APP</title> 
        <style> 
            body { 
                front-family: Arial, sans-serif;
                line-height = 1.5; 
                margin: 0; 
                padding: 20px; 
            }
            
        </style> 
    </head> 
    <body>  
        <h1> ABOUT THIS WEB-APP</h2> 
        <p> THIS MY FIRST APP ON DJANGO FRAMEWORK!!!</p>
        
        <p><a href="/about"> Обо мне </a></p>
    </body>
    </html>
    """
    logger.info(f'Index page accessed: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
        <!DOCTYPE html> 
        <head> 
            <meta cherset='UTF-8'>
            <meta name = "viewport" content="device-width, initial-scale=1.0">
            <title>FIRST DJANGO WEB APP</title> 
            <style> 
                body { 
                    front-family: Arial, sans-serif;
                    line-height = 1.5; 
                    margin: 0; 
                    padding: 20px; 
                }

            </style> 
        </head> 
        <body>  
            <h1> ABOUT ME</h2> 
            <p> MY NAME IS KIRILL ALLYANOV AND I AM JUNIOR PYTHON DEVELOPER!!!</p>

            <p><a href="/about"> Обо мне </a></p>
        </body>
        </html>
        """
    logger.info(f'Index page accessed: {datetime.now()}')
    return HttpResponse(html)
