import subprocess, re


def ping_command():
    res = subprocess.run("ping google.com", capture_output=True)
    str_res = res.stdout.decode('utf-8')
    str_pattern = r'Sent = ([0-9]*).*Received = ([0-9]*).*Lost = ([0-9]*).*Minimum = ([0-9]*).*Maximum = ([0-9]*)'
    search_res = re.search(str_pattern, str_res, re.DOTALL)
    Sent, Received, Lost, Minimum, Maximum = search_res.groups()
    print("Sent = {}, Received = {}, Lost = {}\nMinimum = {}, Maximum = {}".format(
        Sent, Received, Lost, Minimum, Maximum
    ))
ping_command()