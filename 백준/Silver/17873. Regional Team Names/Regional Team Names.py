if (len(team_name := input().split("-")) > 1
    and 1 < len(team_name[0]) <= 8
    and 1 <= len("-".join(team_name[1:])) <= 24):
    print("YES")
else:
    print("NO")