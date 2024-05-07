#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip_list = []
        for ch in address:
            ip_list.append(ch)
        new_list = []
        for index, char in enumerate(ip_list):
            if char == ".":
                new_list.append("[.]")
            else:
                new_list.append(char)
        ip_list = new_list
        ip_string = "".join(ip_list)
        return ip_string
