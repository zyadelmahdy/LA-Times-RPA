from shared.latimes import LATimes

with LATimes(teardown=True) as bot:
    bot.load_first_page()
    print('Successfully loaded LA Times first page.')
    bot.search('education')
    bot.filter()
    bot.sort_newest()
    bot.pull_data()
    bot.export()
    # Inside your main code
    # all_data = bot.pull_data()
    # bot.export(all_data)
