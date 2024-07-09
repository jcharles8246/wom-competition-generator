# Wise Old Man Competition Generator

A small script that lets you generate multiple weekly Skill of the Week events in Wise Old Man.

## Requirements

* Python 3+ (Tested on Python 3.8.10)
* A Wise Old Man "Group" and the "Group Verification Code" matching

## Getting Started

The script comes with help text, but below is an example execution of the tool

```
./generate_competitions.py --startDate 20240709 --numComps 100 --groupId 0 --groupVerificationCode 100-100-100
```

You can dry run the script to see what it _would_ generate

```
./generate_competitions.py --startDate 20240709 --numComps 100 --groupId 0 --groupVerificationCode 100-100-100 --dryRun
```
