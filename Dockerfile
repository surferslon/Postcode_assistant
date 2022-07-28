FROM python:3.8

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m pip install flask gunicorn wheel pytest

ADD api /usr/app
ADD postcode_assistant /usr/postcode_assistant

WORKDIR /usr/postcode_assistant
RUN python setup.py bdist_wheel

RUN python -m pip install dist/postcode_assistant-0.1-py3-none-any.whl

WORKDIR /usr/app

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "app:app"]
