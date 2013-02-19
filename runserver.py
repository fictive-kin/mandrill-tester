import argparse as ap
from tester import app

parser = ap.ArgumentParser()
parser.add_argument('--host',
                    dest='host',
                    default='0.0.0.0')
parser.add_argument('--port',
                    type=int,
                    dest='port',
                    default=7102)
ns = parser.parse_args()

app.run(host=ns.host, port=ns.port)
