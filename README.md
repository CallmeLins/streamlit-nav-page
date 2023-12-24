# streamlit-nav-page
A simple streamlit navigation page 

## config streamlit

Ref: [streamlit Configuration](https://docs.streamlit.io/library/advanced-features/configuration)

In this project I config it in the project root path as local config (.streamlit/config.toml)

## config ngnix

Ref: [How to use Streamlit with Nginx?](https://discuss.streamlit.io/t/how-to-use-streamlit-with-nginx/378/31?page=2)

Notice: 
1. "dashboard" is config in streamlit config file
2. "_stcore" is config for streamlit endpoint, otherwise, whenyou visit your page, it will keep in "Please wait" 

```bash
server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;

        ssl_certificate /etc/ssl/cert.pem;
        ssl_certificate_key /etc/ssl/key.pem;
        ssl_client_certificate /etc/ssl/cloudflare.crt;
        ssl_verify_client on;
        ssl_session_timeout 1d;
        ssl_session_cache shared:MozSSL:10m;  # about 40000 sessions
        ssl_session_tickets off;

        # intermediate configuration
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
        ssl_prefer_server_ciphers off;

        # HSTS (ngx_http_headers_module is required) (63072000 seconds)
        add_header Strict-Transport-Security "max-age=63072000" always;

        root /var/www/example.com/html;
        index index.html index.htm index.nginx-debian.html;

        server_name home.example.com;

        location / {
                try_files $uri $uri/ =404;
        }

        location /dashboard {
            proxy_pass http://localhost:8501/dashboard;
        }
        location /dashboard/_stcore/static {
                proxy_pass http://localhost:8501/dashboard/_stcore/static/;
        }
        location /dashboard/_stcore/healthz {
                proxy_pass http://localhost:8501/dashboard/_stcore/healthz;
        }
        location /dashboard/_stcore/vendor {
                proxy_pass http://localhost:8501/dashboard/_stcore/vendor;
        }
        location /dashboard/_stcore/stream {
                proxy_pass http://localhost:8501/dashboard/_stcore/stream;
                proxy_set_header   Host      $host;
                proxy_set_header   X-Real-IP $remote_addr;
                proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Proto $scheme;
                proxy_buffering    off;
                proxy_http_version 1.1;
                # Also requires websocket:
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_read_timeout 86400;
        }
}
```

## visit it

You can visit it use url "example.com/dashboard"