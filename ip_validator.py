class IPValidator:
    # def __init__(self, ip_address):
    #     self.ip_address = ip_address

    def is_valid_ipv4(self, ip_address):
        # pass  # Placeholder for IPv4 validation logic
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True

    # def is_valid_ipv6(self):
    #     parts = self.ip_address.split(':')
    #     if len(parts) != 8:
    #         return False
    #     for part in parts:
    #         if len(part) > 4 or not all(c in '0123456789abcdefABCDEF' for c in part):
    #             return False
    #     return True