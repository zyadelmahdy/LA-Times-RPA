from shared.yahoo import Yahoo

with Yahoo(teardown=True) as bot:
    bot.load_first_page()
    print('Successfully loaded Yahoo News first page.')