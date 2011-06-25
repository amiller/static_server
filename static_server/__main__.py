from gevent import monkey
monkey.patch_all()
from bottle import route, run, static_file
import os
import argparse


static_path = os.path.abspath('.')


@route('/:path#.+#')
def server_static(path='.'):
    return static_file(path, root=static_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serve a directory")

    # Server port
    parser.add_argument('port', type=str, help='run webpy on this port',
                        default='8080')
    ARGS = parser.parse_args()

    run(host='0.0.0.0', port=ARGS.port, server='gevent', reloader=True)
