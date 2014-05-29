import datetime
import json
import pythonwhois

from flask import Flask, request


def json_fallback(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        return obj


app = Flask(__name__)


@app.route('/')
def hello_world():
    domain = request.args.get('domain', None)
    format = request.args.get('format', 'raw')
    if domain:
        data = pythonwhois.net.get_whois_raw(domain)
        if format == 'json':
            parsed = pythonwhois.parse.parse_raw_whois(data, normalized=True)
            return json.dumps(parsed, default=json_fallback)
        elif format == 'raw':
            return '<pre>{0}</pre>'.format(data[0])
        else:
            return data[0]

    return 'No ?domain= specified!'


if __name__ == '__main__':
    app.run(debug=True)
