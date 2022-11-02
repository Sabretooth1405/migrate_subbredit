import praw
# details of old account
reddit = praw.Reddit(
    client_id="CLIENT ID",
    client_secret="CLIENT SECRET",
    password="ACOOUNT PASSWORD",
    user_agent="USER AGENT NAME",
    username="USERNAME",
)
# details of new account
reddit2 = praw.Reddit(
    client_id="CLIENT ID",
    client_secret="CLIENT SECRET",
    password="ACOOUNT PASSWORD",
    user_agent="USER AGENT NAME",
    username="USERNAME",

)
subreddits = reddit.user.subreddits(limit=None)
for subreddit in subreddits:
    try:
        subreddit_name = subreddit.display_name
        subreddit_type = subreddit.subreddit_type

        # Add to destination account
        dest_sub = reddit2.subreddit(subreddit_name)

        if dest_sub.user_is_subscriber is False:
            if subreddit_type == "user":
                print(f"Following user: {subreddit_name}")
            elif subreddit_type == "public":
                print(f"Joining subreddit: {subreddit_name}")

            dest_sub.subscribe()
    except Exception as ex:
        print(
            ex, f"An error occurred while migrating the subreddit '{subreddit_name}' with id {subreddit.id}.")
