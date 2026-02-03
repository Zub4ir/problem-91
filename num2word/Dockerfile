FROM python:3.12.12

WORKDIR /usr/src/num2word

# copy over content
COPY . .

# installs
RUN pip install --no-cache-dir -r requirements.txt

# run tests
python3 -m pytest ./tests.py