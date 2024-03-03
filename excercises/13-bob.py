# https://exercism.org/tracks/python/exercises/bob
# 13. Bob
# Your task is to determine what Bob will reply
# to someone when they say something to him or ask him a question.
responses = [
    "Sure",
    "Whoa, chill out!",
    "Calm down, I know what I'm doing!",
    "Fine. Be that way!",
    "Whatever.",
]
question = input(">").strip()

if not question:
    print(responses[3])
elif question[-1]=='?':
    if question.isupper():
        print(responses[2])
    else:
        print(responses[0])
elif question.isupper():
    print(responses[1])
else:
    print(responses[4])