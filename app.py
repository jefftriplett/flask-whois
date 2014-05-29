import pythonwhois

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def whois_app():
    domain = request.args.get('domain', None)
    format = request.args.get('format', 'raw')
    if domain:
        data = pythonwhois.net.get_whois_raw(domain)
        if format == 'json':
            parsed = pythonwhois.parse.parse_raw_whois(data, normalized=True)
            return jsonify(parsed)
        elif format == 'raw':
            return '<pre>{0}</pre>'.format(data[0])
        else:
            return data[0]

    return 'No ?domain= specified!'


if __name__ == '__main__':
    whois_app.run(debug=True)
