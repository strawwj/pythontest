#!/usr/bin/env python
"""
    Usage: apacheLog.py logFile
"""
import re
import sys

log_line_re = re.compile('''(?P<remote_host>\S+)  #IP
                            \s+  #wp
                            \S+  #logname
                            \s+  #wp
                            \S+  #user
                            \s+  #wp
                            \[[^\[\]]+\]     #time
                            \s+ #wp
                            "[^"]+" 
                            \s+ #wp
                            (?P<ststus>\d+) #ststus
                            \s+ #wp
                            (?P<bytes_sent>-|\d+) #bytes
                            \s* #wp
                            ''',re.VERBOSE)
def split_log(line):
    m = log_line_re.match(line)
    if m:
        groupdict = m.groupdict()
        if groupdict['bytes_sent'] == '-':
            groupdict['bytes_sent'] = '0'
        return groupdict
    else:
        return {'remote_host': None,
                'status': None,
                'bytes_sent': '0',
        }

def generate_report(logfileobj):
    report_dict = {}
    for line in logfileobj:
        line_dict = split_log(line)
        print line_dict
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            continue
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
    return report_dict

def main():
    if not len(sys.argv)> 1:
        print __doc__
        sys.exit(1)
    infile_path = sys.argv[1]
    try:
        infile = open(infile_path, 'r')
    except IOError:
        print ' file path is not exsits'
        print __doc__
        sys.exit(1)
    log_report = generate_report(infile)
    print log_report
    infile.close()

if __name__ == "__main__":
    main()
