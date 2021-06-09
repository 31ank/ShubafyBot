import praw

userAgent = ''

cID = ''

cSC= ''

userN = ''

userP =''


def main():
    reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

    print(reddit.user.me)

    subreddit = reddit.subreddit("")
    for comment in subreddit.stream.comments(skip_existing=True):
        print(comment.body)
        if(comment.body == "!shubafy"):
            parent = comment.parent_id
            # check if parent comment exists, if not skip comment
            if(parent[:3] != "t1_"):
                continue

            parentComment = reddit.comment(id=str(parent[3:]))
            # break code before bot starts spamming
            if(parentComment.body.find("!shubafy") != -1):
                comment.reply("already shubafied")
                continue

            reply = shubafy(parentComment.body)

            try:
                comment.reply(reply)
                print("=== SHUBAFIED ===")
                print(comment.body)
                print(reply)
                print("=================")
            except Exception as e:
                print("=== ERROR ===")
                print("Something went wrong: " + e)
                print ("============")
                continue

                
def shubafy(comment):
    found = 0
    foundSomething = False
    while(found != -1):
        found = comment.find(".", found, len(comment))
        if(found != -1):
            found = found + 1
            comment = comment[:found] + " shuba " + comment[found:]
            foundSomething = True
    if foundSomething == False:
        return comment + " shuba"
    if(comment[-6:] != "shuba "):
        comment = comment + " shuba"
    return comment

if __name__ == "__main__":
    main()