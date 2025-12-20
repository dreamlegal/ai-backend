module.exports = {
  apps: [{
    name: "ai-backend",
    cwd: "/root/ai-backend",
    script: "/root/ai-backend/venv/bin/uvicorn",
    args: "main:app --host 0.0.0.0 --port 8000",
    interpreter: "/root/ai-backend/venv/bin/python3",
    env: {
      PATH: "/root/ai-backend/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    }
  }]
}
