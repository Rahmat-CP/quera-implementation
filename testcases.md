<details>
<summary>291607 google-calendar-cli</summary>

### test case num 1:

##### input:
```bash
7
ADD --date 2025-06-01 --start 09:00 --end 10:00 --title "Morning Standup"
ADD --start 09:30 --end 11:00 --date 2025-06-01 --title "Client Call"
ADD --date 2025-06-01 --start 13:00 --end 14:00 --title "Lunch with Team"
CONFLICTS --date 2025-06-01
SEARCH --keyword call
REMOVE --date 2025-06-01 --start 09:30
LIST --date 2025-06-01
```
##### output:
```bash
Created event at 2025-06-01 09:00
Created event at 2025-06-01 09:30
Created event at 2025-06-01 13:00
Conflict Detected:
| 2025-06-01 | 09:00-10:00 | Morning Standup |
| 2025-06-01 | 09:30-11:00 | Client Call |
Search Results:
| 2025-06-01 | 09:30-11:00 | Client Call |
Removed event at 2025-06-01 09:30
Day View: 2025-06-01
| 2025-06-01 | 09:00-10:00 | Morning Standup |
| 2025-06-01 | 13:00-14:00 | Lunch with Team |
```
### test case num 2:

##### input:
```bash
6
ADD --title "Project Kickoff" --date 2025-07-01 --start 10:00 --end 11:00
ADD --date 2025-07-03 --start 14:00 --end 15:00 --title "Code Review"
ADD --start 09:00 --end 10:30 --title "Client Feedback" --date 2025-07-10
EDIT --date 2025-07-03 --start 14:00 --title "Team Sync"
WEEK --date 2025-07-01
MONTH --month 2025-07
```
##### output:
```bash
Created event at 2025-07-01 10:00
Created event at 2025-07-03 14:00
Created event at 2025-07-10 09:00
Edited event at 2025-07-03 14:00
Week View (2025-07-01 to 2025-07-07):
| 2025-07-01 | 10:00-11:00 | Project Kickoff |
| 2025-07-03 | 14:00-15:00 | Team Sync |
Month View: 2025-07
| 2025-07-01 | 10:00-11:00 | Project Kickoff |
| 2025-07-03 | 14:00-15:00 | Team Sync |
| 2025-07-10 | 09:00-10:30 | Client Feedback |
```


</details>

