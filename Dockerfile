FROM python:3
ADD ./src /
RUN pip install ply
CMD ["python", "main.py"]
