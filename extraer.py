#!/usr/bin/env python

import argparse
import urllib.request
from datetime import datetime, timedelta

def main(domain, filename):
    url = f'https://{domain}/wp-content/ai1wm-backups/{filename}'
    try:
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        f = urllib.request.urlopen(req)
        i = f.info()

        last_modified = i['Last-Modified']

        timestamp = datetime.strptime(last_modified, "%a, %d %b %Y %H:%M:%S %Z")
        time_ymd = timestamp.strftime("%Y%m%d")
        time_hms = timestamp.strftime("%H%M%S")

        print(f"https://{domain}/wp-content/ai1wm-backups/{domain}-{time_ymd}-{time_hms}-000.wpress")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"El archivo no se encuentra en la URL: {url}")
        else:
            print(f"Error al acceder a la URL: {url}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verifica la existencia de un archivo en un dominio.")
    parser.add_argument("domain", help="Dominio en el que buscar el archivo")
    parser.add_argument("filename", help="Nombre del archivo a verificar")

    args = parser.parse_args()
    main(args.domain, args.filename)
