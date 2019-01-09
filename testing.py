from flask import Flask
app = Flask(__name__)
app.config.from_mapping(
	SECRET_KEY='dev'
)

@app.route('/')
def testing():
	return 'hello world'
if __name__ == "__main__":
	app.run(port='80')
