class TJS_Posts:
    def __init__(self) -> None:
        self.__posts = {}

    def add_post(self, post):
        self.__posts[post.lower()] = self.__posts.get(post.lower(), 0) + 1

    def __str__(self) -> str:
        return f"{self.__posts}"

    def __getitem__(self, post):
        return self.__posts.get(post.lower(), 0)

    def __setitem__(self, post, count):
        self.__posts[post.lower()] = count


# driver
online_blog = TJS_Posts()
online_blog.add_post("Watchmen")
online_blog.add_post("watchmen")

online_blog.add_post("doomsday clock")
print(online_blog)

print(f"Watchmen comics count: {online_blog['watchmen']}")

online_blog.__setitem__("watchmeN", 3)
print(f"Watchmen (+ tv series) count: {online_blog['watchmen']}")

# dict that holds all the class attributes
print(online_blog.__dict__)
