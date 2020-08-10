import argparse

def argParser():    
    parser = argparse.ArgumentParser(
        prog='Photo Downloader (from Google)',
        epilog='Developed by Mustafa Emre Ozmen with <3. Feels free use and develop.'
    )
    parser.add_argument('--keyword', 
                        help='Keyword for download images.',
                        required=True,
                        type=str)
    
    parser.add_argument('--scrollQuantity', 
                        help='Scroll quantity for Google Image page. Default Scroll Quantity: 5',
                        default=5,
                        type=int)

    parser.add_argument('--quantity', 
                        help='Quantity for downloading. Default Quantity: 10', 
                        default=10, 
                        type=int)

    parser.add_argument('--width', 
                        help='Width for downloading images. Default Width: 800', 
                        default=800, 
                        type=int)

    parser.add_argument('--height', 
                        help='Height for downloading images. Default Height: 480', 
                        default=480, 
                        type=int)
    
    passedArgs = parser.parse_args()
    
    return passedArgs