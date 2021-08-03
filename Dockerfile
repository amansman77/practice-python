FROM python:3.7

# COPY kafka-python/requirements.txt .
# COPY aiokafka/requirements.txt .
COPY directory/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["/bin/bash"]
