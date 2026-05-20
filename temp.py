from source.blog.models import Post
import json

with open("post.json") as f:
    post_json = json.load(f)

for post in post_json:
    Post.objects.create(
        title=post["title"], content=post["content"], author=post["user_id"]
    )
