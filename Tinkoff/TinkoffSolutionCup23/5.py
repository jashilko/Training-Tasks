# python 3.10
import json
from datetime import date



def filter_data(text: str) -> str:
    today = date.today()
    ans = json.loads(text)
    print(ans)
    for one in ans:
        if "admin" in one['roles']:
            y, m, d = list(one['profile']['dob'].split('-'))
            age = today.year - int(y) - ((today.month, today.day) < (int(m), int(d)))
            if age >0:
                yc =one['createdAt'][:4]
                mc = one['createdAt'][5:7]
                dc = one['createdAt'][8:10]
                print(yc, mc, dc)


if __name__ == "__main__":
    input_str = input()
    print(filter_data(input_str))
