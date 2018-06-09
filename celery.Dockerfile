FROM continuumio/miniconda3
RUN pip install celery
COPY tasks.py /
COPY pusher.py /
CMD ["celery","-A","tasks","worker","--loglevel=info"]
