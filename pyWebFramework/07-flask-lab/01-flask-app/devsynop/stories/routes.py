from flask import (Blueprint, render_template, url_for, flash, 
                    redirect, request, abort)
# flask auth functionality
from flask_login import current_user, login_required

from devsynop import db
from devsynop.models import Post
from devsynop.stories.forms import PostForm

stories = Blueprint('stories', __name__)

@stories.route("/post/create", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post is created', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title="Create Post", form=form, legend="Create post")


@stories.route("/post/<int:post_id>", methods=['GET', 'POST'])
def detail_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('detail_post.html', title=post.title, post=post)


@stories.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post has been updated!', 'success')
        return redirect(url_for('stories.detail_post', post_id=post.id))
    elif request.method == "GET":
        # filling the the form input with database data
        form.title.data = post.title
        form.content.data = post.content 

    return render_template('create_post.html', title="Update Post", form=form, legend="Update post")


@stories.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('main.index'))

