import requests


class HttpClient:
    @staticmethod
    def get(
            url,
            params=None,
            allow_redirects=True,
            auth=None,
            cert=None,
            cookies=None,
            headers=None,
            proxies=None,
            stream=None,
            timeout=None,
            verify=None
    ):
        return requests.get(
            url,
            params=params,
            allow_redirects=allow_redirects,
            auth=auth,
            cert=cert,
            cookies=cookies,
            headers=headers,
            proxies=proxies,
            stream=stream,
            timeout=timeout,
            verify=verify
        )

    @staticmethod
    def post(
            url,
            data=None,
            json=None,
            files=None,
            allow_redirects=True,
            auth=None,
            cert=None,
            cookies=None,
            headers=None,
            proxies=None,
            stream=None,
            timeout=None,
            verify=None
    ):
        return requests.post(
            url,
            data=data,
            json=json,
            files=files,
            allow_redirects=allow_redirects,
            auth=auth,
            cert=cert,
            cookies=cookies,
            headers=headers,
            proxies=proxies,
            stream=stream,
            timeout=timeout,
            verify=verify
        )

    @staticmethod
    def put(
            url,
            data=None,
            json=None,
            files=None,
            allow_redirects=True,
            auth=None,
            cert=None,
            cookies=None,
            headers=None,
            proxies=None,
            stream=None,
            timeout=None,
            verify=None
    ):
        return requests.put(
            url,
            data=data,
            json=json,
            files=files,
            allow_redirects=allow_redirects,
            auth=auth,
            cert=cert,
            cookies=cookies,
            headers=headers,
            proxies=proxies,
            stream=stream,
            timeout=timeout,
            verify=verify
        )
