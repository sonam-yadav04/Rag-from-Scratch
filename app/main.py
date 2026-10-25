from fastapi import  FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World'}   

@app.get('/health')
def health_check():
    return {'message': 'OK'}    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='[IP_ADDRESS]', port=8000)



