import ecapture as ec

banner = '''
    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠙⠛⠻⢿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣬⡁⠀⠀⠆⡆⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠮⢭⣙⠃⣤⠀⢸⡇⠀⣼⡇⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣄⠈⠃⣥⢸⣼⡇⠀⣿⡇⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣿⣦⣸⣿⡀⣿⡇⠀⠛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣯⣽⣻⣿⣿⠀⢀⠀⠀⠀⠀⠀⠀⠀⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣈⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⠿⠟⢛⣛⣯⣅⠀⢰⠄⠀⠀⠀⠀⠀⠀⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣽⣷⡿⠿⢟⣛⣭⣥⢠⠀⣦⠀⠀⠀⠀⠀⠀⢸⣿⣌⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⡀⠀⠀⠀⠀⡄⠀⠀⠀⣾⣿⣿⣿⣿
⣛⣭⣶⣾⣿⣿⣿⣿⠿⠘⣃⢹⣄⠀⠀⡄⠀⠀⠀⠹⣿⣷⣜⣷⣮⣝⠻⣿⣿⣿⣿⣿⠟⠡⢐⡛⠀⠀⠀⠀⢘⠃⠀⠀⡄⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⢟⣩⣶⣾⡇⢿⡆⢻⣇⡀⢠⠀⠀⠀⣷⣌⢿⣿⣿⣷⣶⣶⣿⡿⠟⢋⣵⡖⣿⣿⠇⠀⠀⠀⠀⣾⡀⠀⠸⢓⠘⣿⣿⣿⣛
⣿⡿⢟⣩⣶⣿⣿⣿⣿⣿⡌⣴⡷⣼⢳⣦⣄⠀⠀⢿⣿⣆⣙⣛⣛⣭⣭⣵⢆⣿⡎⣿⢰⡿⣣⠀⠀⢠⢆⣼⣿⣧⠀⢸⡿⠆⣿⣿⣿⣿
⠋⣶⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⠟⢃⣿⣿⣿⣦⣱⣼⣿⣿⣿⣟⠻⣿⣿⡏⣾⣿⡷⢠⣶⣾⠋⢀⣴⣯⣾⠿⣡⢏⣶⣾⡇⢸⣿⣿⣿⣿
⡸⡜⣿⣿⣿⣿⡟⣿⣿⣇⣿⡏⠀⣼⣌⠻⣿⣿⡏⣿⣿⣿⣿⣿⣿⣶⢋⣿⣿⣿⠇⣾⣿⣿⣾⡏⣿⢻⡟⣰⢏⣾⣿⣿⠀⣾⣿⣿⣿⣿

                    ₴ЇMЇИ Pутнои Caмёяa
                Dєvєlоpєґ : Mонaммad BaЬaёё
                 БїтHцЬ : @монaммad-вaвaёё
This App Is Published Under : GNU General Public License v3.0

    '''

print(banner)

print(''' 
    
    [1] Taking The Picture
    [2] Recording The Video


    ''')

user_input = str(input("> Please Select The Task By Enter The Number : "))

if user_input == "1":
    # The Photo Capturing section
    img_shot = ec.capture(0,"Take The Picture", "photo.png" , 3)

    print(img_shot)

elif user_input == "2":
    # The Video Recording Section
    vid_shot = ec.vidCapture(0,"Recording Video", "video.avi", "x" )

    print(vid_shot)
else:
    print("Somethings is wrong , Try Again ...")