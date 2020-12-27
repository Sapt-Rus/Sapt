import plyer


def push(text, name, icon, title):
    plyer.notification.notify(message=text,
    app_name=name,
    app_icon=icon,
    title=title)


