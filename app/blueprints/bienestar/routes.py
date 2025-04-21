from flask import Blueprint, render_template, request
import os

# Change the blueprint name from 'bienestar_bp' to 'main'
bienestar_bp = Blueprint('main', __name__, template_folder='../../templates')

# Set up path to posts data file
@bienestar_bp.record
def record_params(setup_state):
    app = setup_state.app
    # Set the posts file path in app config if not already set
    if 'POSTS_FILE' not in app.config:
        app.config['POSTS_FILE'] = os.path.join(app.static_folder, 'data', 'posts_bienestar.json')

# Main routes (from main.py)
@bienestar_bp.route('/bienestar', methods=['GET'])
def index():
    """Main page of the Bienestar module"""
    return render_template('bienestar/index.html')

@bienestar_bp.route('/manage-posts', methods=['GET'])
def manage_posts():
    return render_template('bienestar/manage-posts.html')

@bienestar_bp.route('/view-posts', methods=['GET'])
def view_posts():
    return render_template('bienestar/view-posts.html')

@bienestar_bp.route('/bienestar/post-detail', methods=['GET'])
def post_detail():
    """Post detail page"""
    post_id = request.args.get('id')
    return render_template('bienestar/post-detail.html', post_id=post_id)

@bienestar_bp.route('/bienestar/post-editor', methods=['GET'])
def post_editor():
    """Post editor page"""
    post_id = request.args.get('id', '')
    return render_template('bienestar/post-editor.html', post_id=post_id)