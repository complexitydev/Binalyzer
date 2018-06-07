import os
from binanalyzer import app
#
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run('192.99.0.166', port=port)