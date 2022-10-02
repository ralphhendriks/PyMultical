FROM python:3.10
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install pyserial
ADD pymultical.py .
# ENTRYPOINT ["python", "pymultical.py"]
CMD ["python","pymultical.py","/dev/ttyUSB1","60"]
