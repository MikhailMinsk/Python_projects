# Making an anonymous blog
# User can write post with title and content.
# Users can leave comments under the post.
# You must use text templates to display your blog.


from app import app, db
import models
import views

if __name__ == '__main__':
    app.run()
