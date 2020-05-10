from datetime import datetime
import time


def pom(work, rest, rounds):
    for i in range(1, rounds+1):
        print(f'Round Number: {i}')
        pom_timer(work, 'Work')
        pom_timer(rest, 'Rest')


def pom_timer(mins, round_str):
    start = datetime.today()
    remaining = round(mins * 60 - (datetime.today() - start).total_seconds())

    while remaining > 0:
        print(f'\r{round_str} - Time Remaining: {int(remaining / 60):02d}:{int(remaining % 60):02d}', end='')
        time.sleep(1)
        remaining = round(mins * 60 - (datetime.today() - start).total_seconds())

    print(f'\r{round_str} - Time Remaining: {int(remaining / 60):02d}:{int(remaining % 60):02d}')


def main(work=25, rest=5, rounds=4):
    pom(work, rest, rounds)


if __name__ == '__main__':
    main()
