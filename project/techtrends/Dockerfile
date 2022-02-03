FROM python:3.9
COPY ./project/techtrends /app
WORKDIR /app
RUN ls -la
RUN pip install -r requirements.txt
RUN python init_db.py
EXPOSE 3111
CMD ["python", "app.py"]
