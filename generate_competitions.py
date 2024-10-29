#!/bin/python3

import datetime, sys, random, requests, argparse, json

def add_args(parser):
    parser.add_argument('--startDate', required=True, help='Start date to generate competitions from, in YYYYMMDD format')
    parser.add_argument('--numComps', required=True, type=int, help='Number of competitions to generate')
    parser.add_argument('--groupId', required=True, type=int, help='Group ID of Wise Old Man Group')
    parser.add_argument('--groupVerificationCode', required=True, help='Group Verification Code of Wise Old Man Group')
    parser.add_argument('--dryRun', required=False, action='store_true', help='Dry run script')

def get_random_metric(recent_args):
    metrics = ['attack', 'defence', 'strength', 'hitpoints', 'ranged', 'prayer', 'magic', 'cooking', 'woodcutting', 'fletching', 'fishing', 'firemaking', 'crafting', 'smithing', 'mining', 'herblore', 'agility', 'thieving', 'slayer', 'farming', 'runecrafting', 'hunter', 'construction']
    return random.choice([item for item in metrics if item not in recent_args[-5:]])

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
    generated_metrics = []
    payloads = []
    
    # Generate POST payload and submit to generate competition on repeat
    for i in range(numComps): 
        start_date_str = start_date.isoformat(timespec='milliseconds') + "Z"
        end_date_str = end_date.isoformat(timespec='milliseconds') + "Z"
        metric = get_random_metric(generated_metrics)
        payload = {
            "title": title,
            "metric": metric,
            "startsAt": start_date_str,
            "endsAt": end_date_str,
            "groupId": groupId,
            "groupVerificationCode": groupVerificationCode
        }

        print("Week " + str(i) + ": " + metric)
        payloads.append(payload)

        generated_metrics.append(metric)
        start_date = start_date + datetime.timedelta(days=7)
        end_date = end_date + datetime.timedelta(days=7)

    if not dryRun:
        while (True):
            answer = input("Would you like to generate these competitions? [y/n]")
            if answer.lower() in ["y", "yes"]:
                for payload in payloads:
                    x = requests.post(url, json = payload)
                    print(x.text)  
                break
            elif answer.lower() in ["n", "no"]:
                print("Exiting...")
                break
            else:
                print("Invalid input...try again")

if __name__ == '__main__':
    main()
