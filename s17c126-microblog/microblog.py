from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from app import create_app, db, cli
from app.models import User, Post
from app.search import add_to_index, remove_from_index, query_index


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User,
            'Post': Post,
            'generate_password_hash': generate_password_hash,
            'check_password_hash': check_password_hash,
            'md5': md5,
            'add_to_index': add_to_index,
            'remove_from_index': remove_from_index,
            'query_index': query_index
            }
