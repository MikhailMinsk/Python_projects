from sys import exit

import colorama
import tweepy

colorama.init()  # init colored text


def error_message(error):
    print(colorama.Fore.RED + 'Something wrong. Try again. Error:', error)
    print(colorama.Style.RESET_ALL)  # reset colored text


def print_tweet(tweet):
    print(colorama.Fore.BLUE + str(tweet.created_at), colorama.Fore.GREEN + str(tweet.source),
          colorama.Fore.WHITE + str(tweet.text))
    print(colorama.Style.RESET_ALL)


def connect_to_twitter():
    """
    connection to tweeter via API
    :return: api
    """
    ACCESS_TOKEN = ''
    ACCESS_SECRET = ''
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''

    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    except Exception as error:
        error_message(error)


api = connect_to_twitter()


def my_tweets(api):
    """
    print tweets from my stream
    """
    try:
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print_tweet(tweet)
    except Exception as error:
        error_message(error)
    finally:
        main()


def new_tweet(api):
    """
    create new tweet
    """
    tweet = input('Input your tweet: ')
    try:
        api.update_status(status=tweet)
        print(colorama.Fore.GREEN + '     Tweet is published !')
        print(colorama.Style.RESET_ALL)
    except Exception as error:
        error_message(error)
    finally:
        main()


def user_tweets(api):
    """
    show user tweets
    """
    user_name = input('Input name of user: ')
    try:
        user_tweets = api.user_timeline(user_name)
        for tweet in user_tweets:
            print_tweet(tweet)
    except Exception as error:
        error_message(error)
    finally:
        main()


def find_tag(api):
    """
    shows last tweets for the last week by tag
    """
    for_search = input('Input tag for search: ')
    limit_messages = int(input('Input the number of messages to be displayed: '))
    try:
        tag_tweets = tweepy.Cursor(api.search, q=for_search).items(limit_messages)
        for tweet in tag_tweets:
            print_tweet(tweet)
    except Exception as error:
        error_message(error)
    finally:
        main()


def main():
    """
    main function
    """
    print('   Select an action:  ')
    print('1: Write new tweet \n'
          '2: Show my tweets \n'
          '3: Show tweets another user \n'
          '4: Find by tags \n'
          'q: For exit')
    value = input('Input value: ')
    if value == '1':
        new_tweet(api)
    elif value == '2':
        my_tweets(api)
    elif value == '3':
        user_tweets(api)
    elif value == '4':
        find_tag(api)
    elif value == 'q':
        exit()
    else:
        print(colorama.Fore.RED + '\n    WRONG INPUT  !!! \n')
        print(colorama.Style.RESET_ALL)
        main()


if __name__ == '__main__':
    main()
