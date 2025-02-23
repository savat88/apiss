from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    url = "http://45.144.165.187:8080/playidtv1/12345/17715"  # เปลี่ยนเป็น URL ที่ต้องการ
    headers = {"User-Agent": "ไม่อนุญาตแกะลิงค์"}
    
    r = requests.get(url, headers=headers, stream=True)
    
    return Response(r.iter_content(chunk_size=1024), content_type=r.headers.get('Content-Type', 'application/vnd.apple.mpegurl'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
