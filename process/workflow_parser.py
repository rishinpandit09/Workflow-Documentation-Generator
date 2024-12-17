import json

def parse_logs(logs):
    workflows = []
    requests = {}

    static_extensions = ('.css', '.js', '.png', '.jpg', '.woff2', '.svg', '.ico')

    for log in logs:
        try:
            message = json.loads(log['message'])['message']
            method = message.get('method', '')
            params = message.get('params', {})

            if method == 'Network.requestWillBeSent':
                request_id = params.get('requestId')
                request = params.get('request', {})
                url = request.get('url')

                # Exclude static resources and irrelevant URLs
                if not url.lower().endswith(static_extensions) and "google" not in url.lower():
                    requests[request_id] = {
                        'url': url,
                        'method': request.get('method'),
                        'timestamp': params.get('timestamp'),
                        'response_status': None,
                        'response_time': None
                    }

            elif method == 'Network.responseReceived':
                request_id = params.get('requestId')
                if request_id in requests:
                    response = params.get('response', {})
                    requests[request_id]['response_status'] = response.get('status')
                    requests[request_id]['response_time'] = response.get('responseTime')
        except Exception as e:
            print(f"Error parsing log: {e}")

    workflows = sorted(requests.values(), key=lambda x: x['timestamp'] or 0)
    return workflows
