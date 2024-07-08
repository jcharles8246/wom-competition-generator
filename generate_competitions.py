#!/bin/python3

import datetime, sys, random, requests, argparse, json

def add_args(parser):
    parser.add_argument('--startDate', required=True, help='Start date to generate competitions from, in YYYYMMDD format')
    parser.add_argument('--numComps', required=True, type=int, help='Number of competitions to generate')
    parser.add_argument('--groupId', required=True, type=int, help='Group ID of Wise Old Man Group')
    parser.add_argument('--groupVerificationCode', required=True, help='Group Verification Code of Wise Old Man Group')
    parser.add_argument('--dryRun', required=False, action='store_true', help='Dry run script')

def main():
    parser = argparse.ArgumentParser(description='Generate SOTW competitions on Wise Old Man for a group')
    add_args(parser)
    args = parser.parse_args()

    # Inputs
    numComps = args.numComps
    groupId = args.groupId
    groupVerificationCode = args.groupVerificationCode
    startDateInput = args.startDate
    dryRun = args.dryRun

    start_date = datetime.datetime(int(startDateInput[0:4]), int(startDateInput[4:6]), int(startDateInput[6:8]), 18)
    end_date = start_date + datetime.timedelta(days=6)

    url = "https://api.wiseoldman.net/v2/competitions"
    title = "Skill of the week"
    metrics = ["attack",
            "strength",
            "defence",
            "hitpoints",
            "ranged",
            "prayer",
            "magic",
            "cooking",
            "woodcutting",
            "fletching",
            "fishing",
            "firemaking",
            "crafting",
            "smithing",
            "mining",
            "herblore",
            "agility",
            "thieving",
            "slayer",
            "farming",
            "runecraft",
            "hunter",
            "construction"
    ]
    random.shuffle(metrics)
   
    # Generate POST payload and submit to generate competition on repeat
    for i in range(numComps): 
        if i % 23 == 0:
            random.shuffle(metrics)
        start_date_str = start_date.isoformat(timespec='milliseconds') + "Z"
        end_date_str = end_date.isoformat(timespec='milliseconds') + "Z"
        payload = {
            "title": title,
            "metric": random.choice(metrics),
            "startsAt": start_date_str,
            "endsAt": end_date_str,
            "groupId": groupId,
            "groupVerificationCode": groupVerificationCode
        }
        print(json.dumps(payload, indent=4))
        print()
        if not dryRun:
            x = requests.post(url, json = payload)
            print(x.text)
        print("~~~~~~~~~~~~~~~~~~~~")

        start_date = start_date + datetime.timedelta(days=7)
        end_date = end_date + datetime.timedelta(days=7)

if __name__ == '__main__':
    main()
