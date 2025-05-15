from typing import Dict
import re


def parse_log(log: str) -> Dict[str, str]:
    
    res = {}
    patterns = {
        "client_ip": "\d+\.\d+\.\d+\.\d+",
        "date": "[0-9]{2}\/[A-Z][a-z]{2}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2} \++[0-9]{4}",
        "http_method": """(?<=")(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)(?=\s)""",
        "path": """(?<=\s)(\/[^"\s]+)(?=\sHTTP)""",
        "http_version": """(?<=HTTP/)[0-9]+\.[0-9]+(?=")""",
        "status": """(?<=" )[0-9]{3}(?= )""",
        "response_bytes": """(?<=[0-9]{3}\s)[0-9]+(?=\s")""",
        "user_agent": """(?<="-"\s").*(?=")"""
    }

    for key,pattern in patterns.items():
        m = re.search(pattern, log)
        res[key] = m.group() if m else None

    
    return res


if __name__ == "__main__":
    log_entry = (
        '122.176.223.19 - - [05/Feb/2024:08:29:40 +0000] '
        '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
        '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
    )

    parsed_log = parse_log(log_entry)
    print("Parsed log data:", parsed_log)