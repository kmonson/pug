import webbrowser

webbrowser.open("https://google.com", new=1, autoraise=False)

webbrowser.open_new_tab("https://google.com")

controller = webbrowser.get("safari")

controller.open("https://google.com", new=1)