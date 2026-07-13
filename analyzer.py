import re
logs = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]

pattern= r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

timestamp_pattern= r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

#for pattern like FileNotFoundError, IndexError
error_pattern= r"[A-Z][a-zA-Z]+Error"
def counting(file_path):
    count = {}
    ip_addresses=set()
    timestamps=[]
    exception_types=set()

    # Initialize all log levels to 0
    for log in logs:
        count[log] = 0

    try:
        with open(file_path, "r") as f:
            for line in f:
                for word in logs:
                    if word in line:
                        count[word] += 1
                
                ip_match=re.search(pattern,line)
                if ip_match:
                    ip=ip_match.group()
                    ip_addresses.add(ip)
                
                timestamp_match=re.search(timestamp_pattern, line)
                if timestamp_match:
                    timestamp=timestamp_match.group()
                    timestamps.append(timestamp)
                    
                error_match=re.search(error_pattern, line)
                if error_match:
                    error=error_match.group()
                    exception_types.add(error)
    
    except FileNotFoundError as e:
        print("Error:",e)
    
    except PermissionError as e:
        print("Error:",e)
    

    return {
        "log_counts": count,
        "ip_addresses": sorted(ip_addresses),
        "timestamps": timestamps,
        "exceptions": sorted(exception_types)
        
    }

