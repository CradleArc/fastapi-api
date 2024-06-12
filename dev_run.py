import uvicorn

from app.main import app

# 运行项目：开发模式

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
