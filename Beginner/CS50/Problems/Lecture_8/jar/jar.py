class Jar:
    def __init__(self, capacity=12, cookies=0):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Hit the road Jack, Wrong capacity!")
        self._capacity = capacity
        self._cookies = cookies

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self.capacity:
            raise ValueError("Not enough space in the Jar.")
        self._cookies += n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("Not enough cookies in the Jar to withdraw.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
