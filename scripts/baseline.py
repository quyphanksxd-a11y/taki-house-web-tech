"""Bounded public GET audit; no login, forms, crawling or remote writes."""
import datetime, hashlib, json, pathlib, time
import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'evidence' / datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
OUT.mkdir(parents=True)
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs): return None
class Meta(HTMLParser):
    def __init__(self): super().__init__(); self.canonical=[]; self.robots=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='link' and 'canonical' in a.get('rel','').lower().split(): self.canonical.append(a.get('href'))
        if tag=='meta' and a.get('name','').lower() in ('robots','googlebot'): self.robots.append(a)
opener=urllib.request.build_opener(NoRedirect())
results=[]
for url in ['http://takihouse.vn/','https://takihouse.vn/','https://takihouse.vn/robots.txt','https://takihouse.vn/sitemap_index.xml']:
    item={'url':url,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'GET','environment':'public via Work terminal','device':'HTTP client; no viewport'}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'TAKI-HOUSE-ReadOnly-Baseline/1.0'})
        try: r=opener.open(req,timeout=20)
        except urllib.error.HTTPError as e: r=e
        with r:
            data=r.read(2_000_001); item['status']=r.code
            item['headers']={k:v for k,v in r.headers.items() if k.lower() in ['content-type','location','server','x-robots-tag','cache-control','via','x-mitmproxy-blocked-reason']}
        item['truncated']=len(data)>2_000_000
        file=OUT/(str(len(results)+1)+'.body');file.write_bytes(data)
        item['body_file']=str(file.relative_to(ROOT));item['sha256']=hashlib.sha256(data).hexdigest()
        body=data.decode('utf-8',errors='replace')
        if url=='https://takihouse.vn/':
            p=Meta();p.feed(body);item['canonical']=p.canonical;item['meta_robots']=p.robots
        if 'robots.txt' in url: item['robots_text']=body[:10000]
        if r.code>=400: item['error_body_excerpt']=body[:800]
    except Exception as e: item['transport_error']=str(e)
    results.append(item)
    time.sleep(1)
(OUT/'baseline.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps({'evidence_directory':str(OUT),'results':results},ensure_ascii=False,indent=2))
