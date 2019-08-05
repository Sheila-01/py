@app.route('/user/<username>')
def show_user_profile(username):
return 'User %s' % escape(username)                         # show the user profile for that user

@app.route('/post/<int:post_id>')
def show_post(post_id):
return 'Post %d' % post_id                                 # show the post with the given id, the id is an integer

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
return 'Subpath %s' % escape(subpath)                     # show the subpath after /path/