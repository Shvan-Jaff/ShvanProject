from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head>
        <title>Shvan's Cosmic Space</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(to right, #0b0f2e, #1a1d42); /* Smooth Space Gradient */
                color: #e0e0e0; 
                margin: 0; 
                padding: 0; 
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container { 
                width: 85%;
                max-width: 800px; 
                padding: 25px; 
                background: #161a36; /* Dark but not black */
                border-radius: 12px; 
                box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3); /* Soft Modern Shadow */
            }
            header { 
                background: #4b0082; /* Indigo */
                color: #ffffff; 
                padding: 20px; 
                text-align: center; 
                font-size: 24px; 
                font-weight: bold;
                border-radius: 12px 12px 0 0;
            }
            section { 
                margin-bottom: 20px; 
                padding-bottom: 15px; 
                border-bottom: 1px solid rgba(255, 255, 255, 0.15); /* Subtle divider */
            }
            h2, h3 { 
                color: #f06292; /* Soft Neon Pink */
                margin-bottom: 10px;
            }
            ul { padding-left: 20px; list-style: none; }
            li { 
                color: #80d0c7; /* Cyan Blue */
                padding: 5px 0;
            }
            p {
                font-size: 16px;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>Hello, I Am Shvan!</header>
            <section>
                <h2>Who Am I?</h2>
                <p>Hey! I'm Shvan, an explorer of technology, design, and the universe of creativity.</p>
            </section>
            <section>
                <h3>Things I Love</h3>
                <ul>
                    <li>Deep Space & Astronomy</li>
                    <li>Sketching Futuristic Art</li>
                    <li>Cyberpunk & Sci-Fi Movies</li>
                </ul>
            </section>
            <section>
                <h3>Current Mission</h3>
                <p>I'm leveling up my graphic design, learning web development, and diving into digital painting.</p>
            </section>
            <section>
                <h3>Fun Fact</h3>
                <p>My dream is to design artwork inspired by space exploration and sci-fi worlds.</p>
            </section>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
