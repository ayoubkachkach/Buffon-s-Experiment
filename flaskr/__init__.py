from flask import Flask, current_app

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev'
	)

	@app.route('/')
	def index():
		return 'Hello'

	return app
