import sys
import re

def print_dialogues(user, log_file):

    dialogues = []

    with open(log_file, 'r') as log:
        for line in log:
            question = line.replace("Seeker: ", "").strip()
            answer = next(log, None)
            if answer:
                answer = answer.replace("TOB-STT: ", "").strip()

            print(f'{user},"{question}","{answer}"')

if __name__ == '__main__':

    log_file = sys.argv[1]

    user = re.search(r"user_?(\d*)_conversations", log_file).group(1)

    print_dialogues(user, log_file)

