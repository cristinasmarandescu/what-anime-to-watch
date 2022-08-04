from anime_data import AnimeData
from notification_manager import NotificationManager

notification_manager = NotificationManager()
random_anime_data = AnimeData().get_random_anime()
while random_anime_data is None:
    random_anime_data = AnimeData().get_random_anime()


def send_anime_details():
    """
    Sends a text (SMS) message with the anime details.
    """
    notification_manager.send_sms(
        message=f"You can watch the following anime: {random_anime_data['Name']}\n"
                f"Genre: {random_anime_data['Genre']}\n"
                f"Episodes: {random_anime_data['Episodes']}\n"
                f"Score: {random_anime_data['Score']}"
    )


def ask_user():
    """
    Asks the user if they want to watch anime, in order to send them the anime details.
    """
    user_input = input("Do you want to watch some anime today?\n")

    if user_input.lower() == "yes":
        send_anime_details()
        return "Cool! I've sent the details on your phone."
    else:
        return "Ok, maybe next time!"


ask_user()