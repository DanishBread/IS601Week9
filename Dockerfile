
FROM python:3

ADD src /src

#RUN pip3 install pandas

CMD [ "python", "/src/CalculatorTests.py" ]