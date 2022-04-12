from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Nymo
from myapp.nymos.forms import NymoPostForm

nymos = Blueprint('nymos', __name__)

@nymos.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = NymoPostForm()
    if form.validate_on_submit():
        nymo_post = Nymo(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(nymo_post)
        db.session.commit()
        flash('Nymo Created')
        print('Nymo was created')
        return redirect(url_for('core.index'))
    return render_template('index.html', form=form)

    # Make sure the blog_post_id is an integer!

@nymos.route('/<int:nymo_id>')
def nymo(nymo_id):
    nymo = Nymo.query.get_or_404(nymo_id) 
    return render_template('blog_post.html', title=nymo.title, date=nymo.date, post=nymo)

@nymos.route('/<int:nymo_id>/update',methods=['GET','POST'])
@login_required
def update(nymo_id):
    nymo = Nymo.query.get_or_404(nymo_id)

    if nymo.author != current_user:
        abort(403)

    form = NymoPostForm()

    if form.validate_on_submit():
        nymo.title = form.title.data
        nymo.text = form.text.data
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('nymos.nymos',nymo_id=nymo.id))

    elif request.method == 'GET':
        form.title.data = nymo.title
        form.text.data = nymo.text

    return render_template('create_nymo.html',title='Updating',form=form)

@nymos.route('/<int:nymo_id>/delete',methods=['GET','POST'])
@login_required
def delete_nymo(nymo_id):

    nymo = Nymo.query.get_or_404(nymo_id)
    if nymo.author != current_user:
        abort(403)

    db.session.delete(nymo)
    db.session.commit()
    flash('Nymo Deleted')
    return redirect(url_for('core.index'))