FROM python:3.6.2-jessie

#RUN pip install -e git+https://github.com/earthquakesan/fox-py#egg=foxpy
#RUN pip install -e git+https://github.com/dice-group/TAIPAN#egg=TAIPAN
#RUN pip install -e git+https://github.com/earthquakesan/agdistispy#egg=agdistispy
RUN pip install python-dateutil
RUN pip install flask==0.12.2
RUN pip install numpy
RUN pip install SPARQLWrapper
RUN pip install rdflib
RUN pip install scipy
RUN pip install scikit-learn
RUN pip install requests

#For debug only
RUN pip install ipdb

ADD startup.sh /startup.sh
RUN chmod +x /startup.sh

CMD ["/startup.sh"]
