FROM python:3.10-slim as compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/HomeStatus/

RUN python -m venv /opt/HomeStatus/venv
# Enable venv
ENV PATH="/opt/HomeStatus/venv/bin:$PATH"

COPY ./requirements.txt /opt/HomeStatus/requirements.txt
RUN pip install -Ur requirements.txt

FROM python:3.10-slim as runner
WORKDIR /opt/HomeStatus/
COPY --from=compiler /opt/HomeStatus/venv /opt/HomeStatus/venv

# Enable venv
ENV PATH="/opt/HomeStatus/venv/bin:$PATH"
COPY . /opt/HomeStatus/
CMD ["python", "“availabilityWS.py", ]