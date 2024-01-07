from app import app

if __name__ == '__main__':
    # The host='0.0.0.0' argument exposes the server publicly
    # If running in a production environment, you might want to remove it
    # or replace it with a host name or IP
    app.run(debug=True, host='0.0.0.0', port=5123)
