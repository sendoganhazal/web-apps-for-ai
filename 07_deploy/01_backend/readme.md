1) Ön hazırlık
    python
    vs code
    git: https://git-scm.com/install/windows
    github hesabı: https://github.com/turkiyeyapayzekaakademisi
    docker desktop: https://docs.docker.com/desktop/setup/install/windows-install/
2) backend repo
    ai-roadmap-backend/
    ├── main.py # endpoint tanımlama
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    ├── .gitignore
    ├── README.MD
3) Backend kodları ve lokal çalıştırma
    pip install -r requirements.txt
    uvicorn main:app --reload
4) Backend dockerfile ve docker ile lokalde çalıştırma 
    docker build -t ai-roadmap-backend .
    docker run -p 8000:8000 ai-roadmap-backend
5) github push
    repo: python-web-uygulama-ai-roadmap-backend
    git init
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/turkiyeyapayzekaakademisi/python-web-uygulama-ai-roadmap-backend.git
    git push -u origin main
6) Render cloud deploy: https://render.com/
    https://python-web-uygulama-ai-roadmap-backend.onrender.com