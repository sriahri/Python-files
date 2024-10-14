import re


leg_pulling = input()
# remove punctuation
leg_pulling = re.sub(r"[\.\?!,;]", r"", leg_pulling)

if leg_pulling.lower() in ["yes", "sure", "most definitely", "that's for sure"]:
    print("Well, at least you're honest.")
