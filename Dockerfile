FROM python:3.6.2-jessie

RUN pip install -e git+https://github.com/earthquakesan/fox-py#egg=fox-py
RUN pip install -e git+https://github.com/dice-group/TAIPAN#egg=TAIPAN
RUN pip install python-dateutil
RUN pip install flask==0.12.2
RUN pip install -e git+https://github.com/earthquakesan/agdistispy#egg=agdistispy

#For debug only
RUN pip install ipdb

CMD ["python", "/taipanserver/run.py"]
